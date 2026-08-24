# -*- coding: utf-8 -*-
"""
Hornea crujia_montaje.ifc en 5 fases con MALLA SOLIDA (para sombreado tipo slide 06).
El Danpalon se separa en un subgrupo 'dp' para poder pintarlo translucido.
Uso: python bake_montaje_fases.py
"""
import json, base64
import numpy as np
import ifcopenshell, ifcopenshell.geom, re

S = ifcopenshell.geom.settings(); S.set(S.USE_WORLD_COORDS, True)
LIB = "../02_SLIDES_HTML/lib/"
SRC = "modelos_3d/crujia_montaje.ifc"

def familia(nm):
    n = (nm or '').lower()
    if 'danpal' in n: return 'danpal'
    if 'acero negro' in n: return 'subestructura'
    if 'ecopilote' in n: return 'pilote'
    if 'aligerada' in n: return 'viga'
    if 'tron' in n: return 'tubular'
    if any(k in n for k in ['plate', 'connection', 'bolts', 'conexi']): return 'nudo'
    if 'muro' in n or 'wall' in n: return 'muro'
    if 'vidrio' in n or 'termopanel' in n: return 'ventana'
    if 'cubierta' in n or 'roof' in n or 'covering' in n: return 'cubierta'
    if 'piso' in n or 'slab' in n: return 'losa'
    return 'otro'

def soldar(v, fa, mm=2000):
    q = np.round(v * mm).astype(np.int64)
    uq, inv = np.unique(q, axis=0, return_inverse=True)
    f2 = inv[fa]
    ok = (f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 0] != f2[:, 2])
    return uq / float(mm), f2[ok]

def b64(a): return base64.b64encode(a.tobytes()).decode()

print("== crujia_montaje.ifc -> 5 fases, malla solida ==")
f = ifcopenshell.open(SRC)
els = []
for p in f.by_type('IfcProduct'):
    if p.is_a() in ('IfcSite', 'IfcBuilding', 'IfcBuildingStorey', 'IfcOpeningElement'): continue
    try: sh = ifcopenshell.geom.create_shape(S, p)
    except Exception: continue
    v = np.array(sh.geometry.verts, dtype=np.float64).reshape(-1, 3)
    fa = np.array(sh.geometry.faces, dtype=np.int64).reshape(-1, 3)
    if len(v) == 0: continue
    nm = (p.Name or '').replace('Direct Shape:', ''); nm = re.sub(r':\d+$', '', nm); nm = re.sub(r' id\d+$', '', nm)
    els.append((nm, p.is_a(), familia(nm), v, fa, v[:, 2].min(), v[:, 2].max()))
print("   elementos con geometria:", len(els))

todos = np.vstack([e[3] for e in els])
c = (todos.min(0) + todos.max(0)) / 2
c[2] = todos[:, 2].min()                      # apoyar en Z=0 (pilote mas bajo)
dims = todos.max(0) - todos.min(0)

def fase(tipo, fm, zi, za, zc):
    # los elementos atraviesan varias alturas: se clasifica por su centro vertical
    if tipo == 'IfcPile' or fm == 'pilote': return 0                       # F1 fundacion
    if za < 0.10:                                                          # todo lo que vive bajo el piso
        return 2 if (fm in ('tubular', 'losa') or zc > -0.55) else 1       # F3 emparrillado / F2 vigas
    if fm in ('danpal', 'subestructura'): return 4                         # F5 piel y su subestructura
    if fm in ('muro', 'ventana', 'cubierta', 'losa'): return 3             # F4 modulo volumetrico
    if zc > 2.6: return 4                                                  # lo alto es pliegue de piel
    return 3

FASES = ['fundacion', 'vigas', 'suelo', 'modulo', 'piel']
grupos = {}
for nm, tipo, fm, v, fa, zi, za in els:
    k = FASES[fase(tipo, fm, zi, za, (zi + za) / 2)]
    sub = 'dp' if fm == 'danpal' else 'op'     # Danpalon aparte -> translucido
    g = grupos.setdefault((k, sub), {'V': [], 'F': [], 'n': 0, 'off': 0})
    g['V'].append(v - c); g['F'].append(fa + g['off']); g['off'] += len(v); g['n'] += 1

meta = {'dims': [round(float(d), 3) for d in dims], 'fases': {}}
lineas = ["/* crujia_montaje.ifc horneado por fase, MALLA SOLIDA (mm int16 + indices).",
          "   Subgrupo dp = Danpalon translucido. IFC Z-up, apoyado en Z=0. */"]
refs = {}
tot_tri = 0
for (k, sub), g in sorted(grupos.items()):
    V = np.vstack(g['V']); F = np.vstack(g['F'])
    V, F = soldar(V, F)
    vi = np.clip(np.round(V * 1000), -32767, 32767).astype(np.int16)
    i32 = len(V) >= 65535
    idx = F.ravel().astype(np.uint32 if i32 else np.uint16)
    tag = k.upper() + "_" + sub.upper()
    meta['fases'].setdefault(k, {})[sub] = {'n': g['n'], 'nv': int(len(V)), 'tri': int(len(F)), 'i32': int(i32)}
    lineas.append('const MONT_' + tag + '_V="' + b64(vi) + '";')
    lineas.append('const MONT_' + tag + '_F="' + b64(idx) + '";')
    refs.setdefault(k, {})[sub] = tag
    tot_tri += len(F)

lineas.append('const MONTAJE_META=' + json.dumps(meta) + ';')
partes = []
for k, subs in refs.items():
    campos = ','.join(s + ':{v:MONT_' + t + '_V,f:MONT_' + t + '_F}' for s, t in subs.items())
    partes.append(k + ':{' + campos + '}')
lineas.append('const MONTAJE_DATA={' + ','.join(partes) + '};')

js = "\n".join(lineas) + "\n"
open(LIB + 'crujia_montaje.js', 'w').write(js)
print("   " + str(len(js) // 1024) + " KB | dims " + str(meta['dims']) + " | triangulos " + str(tot_tri))
for k in FASES:
    if k in meta['fases']:
        for sub, m in meta['fases'][k].items():
            print("     %-11s %s  %4d elem  %7d vert  %8d tri" % (k, sub, m['n'], m['nv'], m['tri']))
