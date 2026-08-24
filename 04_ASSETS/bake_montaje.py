# -*- coding: utf-8 -*-
"""
Hornea los IFC de montaje y fundacion para el deck PAC 7.0.
  ecopilote.ifc      -> pieza 1 de la slide 06 (solido sombreado, malla por familia)
  crujia_montaje.ifc -> slide 07 en 5 fases (wireframe con TODAS las aristas de la malla)
Uso: python bake_montaje.py
"""
import ifcopenshell, ifcopenshell.geom, re, json, base64, sys
import numpy as np
from collections import defaultdict

S = ifcopenshell.geom.settings(); S.set(S.USE_WORLD_COORDS, True)
LIB = "../02_SLIDES_HTML/lib/"

def familia(nm):
    n = (nm or '').lower()
    if 'danpal' in n: return 'danpal'
    if 'acero negro' in n: return 'subestructura'      # antes que cualquier regla de diametro
    if 'ecopilote' in n: return 'pilote'
    if 'aligerada' in n: return 'viga'
    if 'tron' in n: return 'tubular'
    if any(k in n for k in ['plate','connection','bolts','conexi']): return 'nudo'
    if 'muro' in n or 'wall' in n: return 'muro'
    if 'vidrio' in n or 'termopanel' in n: return 'ventana'
    if 'cubierta' in n or 'roof' in n: return 'cubierta'
    if 'piso' in n or 'slab' in n: return 'losa'
    return 'otro'

def leer(path):
    """devuelve lista de (nombre, tipo, familia, verts Nx3, faces Mx3, zmin, zmax)"""
    f = ifcopenshell.open(path); out = []
    for p in f.by_type('IfcProduct'):
        if p.is_a() in ('IfcSite','IfcBuilding','IfcBuildingStorey','IfcOpeningElement'): continue
        try: sh = ifcopenshell.geom.create_shape(S, p)
        except Exception: continue
        v = np.array(sh.geometry.verts, dtype=np.float64).reshape(-1,3)
        fa = np.array(sh.geometry.faces, dtype=np.int64).reshape(-1,3)
        if len(v) == 0: continue
        nm = (p.Name or '').replace('Direct Shape:',''); nm = re.sub(r':\d+$','',nm); nm = re.sub(r' id\d+$','',nm)
        out.append((nm, p.is_a(), familia(nm), v, fa, v[:,2].min(), v[:,2].max()))
    return out

def soldar(v, fa, mm=2000):
    """suelda vertices duplicados a 0.5mm y quita triangulos degenerados"""
    q = np.round(v*mm).astype(np.int64)
    uq, inv = np.unique(q, axis=0, return_inverse=True)
    f2 = inv[fa]
    ok = (f2[:,0]!=f2[:,1]) & (f2[:,1]!=f2[:,2]) & (f2[:,0]!=f2[:,2])
    return uq/float(mm), f2[ok]

def aristas(fa):
    """TODAS las aristas unicas de la malla (cada triangulo aporta 3)"""
    e = np.vstack([fa[:,[0,1]], fa[:,[1,2]], fa[:,[2,0]]])
    e = np.sort(e, axis=1)
    return np.unique(e, axis=0)

def b64(a): return base64.b64encode(a.tobytes()).decode()

# ---------------------------------------------------------------- 1) ECOPILOTE
print("== ecopilote.ifc -> pieza 1 de la Anatomia (solido) ==")
els = leer('modelos_3d/ecopilote.ifc')
todos = np.vstack([e[3] for e in els]); c = (todos.min(0)+todos.max(0))/2
dims = todos.max(0)-todos.min(0)
fam = defaultdict(lambda: {'v':[], 'f':[], 'n':0})
for nm, tipo, fm, v, fa, zi, za in els:
    g = fam[fm]; off = len(g['v'])
    g['v'].append(v - c); g['f'].append(fa + off if off==0 else fa + sum(len(x) for x in g['v'][:-1]))
    g['n'] += 1
meta = {'dims':[round(float(d),3) for d in dims], 'fams':{}}
js = "/* ecopilote.ifc horneado (solido por familia, mm int16, IFC Z-up) */\n"
for k, g in fam.items():
    V = np.vstack(g['v']); F = []
    off = 0
    for vv, ff in zip(g['v'], [x for x in g['f']]):
        pass
    # reconstruir indices correctamente
    V_list, F_list, off = [], [], 0
    for nm, tipo, fm, v, fa, zi, za in els:
        if fm != k: continue
        V_list.append(v - c); F_list.append(fa + off); off += len(v)
    V = np.vstack(V_list); F = np.vstack(F_list)
    V, F = soldar(V, F)
    vi = np.clip(np.round(V*1000), -32767, 32767).astype(np.int16)
    idx = F.ravel().astype(np.uint16) if len(V) < 65535 else F.ravel().astype(np.uint32)
    meta['fams'][k] = {'n':g['n'], 'tri':len(F), 'nv':len(V), 'i32':int(idx.dtype==np.uint32)}
    js += f'const ECOPILOTE_{k.upper()}_V="{b64(vi)}";\n'
    js += f'const ECOPILOTE_{k.upper()}_F="{b64(idx)}";\n'
js += 'const ECOPILOTE_META=' + json.dumps(meta) + ';\n'
js += 'const ECOPILOTE_DATA={' + ','.join(
    f'{k}:{{v:ECOPILOTE_{k.upper()}_V,f:ECOPILOTE_{k.upper()}_F}}' for k in meta['fams']) + '};\n'
open(LIB+'ecopilote.js','w').write(js)
print(f"   {len(js)//1024} KB | dims {meta['dims']}")
for k,m in meta['fams'].items(): print(f"     {k:14} {m['n']:3} elem  {m['tri']:6} tri")

# ---------------------------------------------------------------- 2) MONTAJE
print("\n== crujia_montaje.ifc -> slide 07, 5 fases (wireframe malla completa) ==")
els = leer('modelos_3d/crujia_montaje.ifc')
todos = np.vstack([e[3] for e in els]); c = (todos.min(0)+todos.max(0))/2
c[2] = todos[:,2].min()          # apoyar en Z=0 (el pilote mas bajo)
dims = todos.max(0)-todos.min(0)

def fase(nm, tipo, fm, zi, za):
    if tipo in ('IfcPile','IfcColumn') or fm=='pilote': return 0          # F1 fundacion
    if fm=='viga' and za < 0.05: return 1                                  # F2 vigas bajo piso
    if fm=='subestructura' and za < 0.05: return 1
    if fm in ('tubular','losa') and za < 0.05: return 2                    # F3 suelo ventilado
    if fm=='otro' and za < 0.05: return 2
    if fm in ('muro','ventana','cubierta'): return 3                       # F4 modulo volumetrico
    if fm=='otro' and zi >= 0.0 and za <= 3.1: return 3
    return 4                                                               # F5 piel + pliegue

FASES = ['fundacion','vigas','suelo','modulo','piel']
grupos = defaultdict(lambda: {'V':[], 'F':[], 'n':0, 'off':0})
for nm, tipo, fm, v, fa, zi, za in els:
    k = FASES[fase(nm, tipo, fm, zi, za)]          # alturas en el sistema original: piso = 0.0
    g = grupos[k]
    g['V'].append(v - c); g['F'].append(fa + g['off']); g['off'] += len(v); g['n'] += 1

meta = {'dims':[round(float(d),3) for d in dims], 'fases':{}}
js = "/* crujia_montaje.ifc horneado por fase. Wireframe: TODAS las aristas de la malla.\n   mm int16, indices uint32, IFC Z-up, apoyado en Z=0. */\n"
tot_e = 0
for k in FASES:
    if k not in grupos: continue
    g = grupos[k]
    V = np.vstack(g['V']); F = np.vstack(g['F'])
    V, F = soldar(V, F)
    E = aristas(F); tot_e += len(E)
    vi = np.clip(np.round(V*1000), -32767, 32767).astype(np.int16)
    idx = E.ravel().astype(np.uint32)
    meta['fases'][k] = {'n':g['n'], 'nv':int(len(V)), 'aristas':int(len(E))}
    js += f'const MONT_{k.upper()}_V="{b64(vi)}";\n'
    js += f'const MONT_{k.upper()}_E="{b64(idx)}";\n'
js += 'const MONTAJE_META=' + json.dumps(meta) + ';\n'
js += 'const MONTAJE_DATA={' + ','.join(
    f'{k}:{{v:MONT_{k.upper()}_V,e:MONT_{k.upper()}_E}}' for k in meta['fases']) + '};\n'
open(LIB+'crujia_montaje.js','w').write(js)
print(f"   {len(js)//1024} KB | dims {meta['dims']} | aristas totales {tot_e}")
for k in FASES:
    if k in meta['fases']:
        m = meta['fases'][k]
        print(f"     {k:12} {m['n']:4} elem  {m['nv']:7} vert  {m['aristas']:8} aristas")
