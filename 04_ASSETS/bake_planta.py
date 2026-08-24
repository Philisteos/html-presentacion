# -*- coding: utf-8 -*-
"""
Horneador de planimetrías CAD -> deck PAC 7.0
DXF (guardar-como desde AutoCAD, sin ploteo) -> SVG monocromo blanco con jerarquía
de grosores + const JS para el deck (PLANTA_SVG + PLANTA_W_M para escala gráfica).

Uso:  python bake_planta.py "ruta/al/plano.dxf"
"""
import sys, re
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.svg import SVGBackend
from ezdxf.addons.drawing.config import (Configuration, ColorPolicy, BackgroundPolicy,
                                         LineweightPolicy, HatchPolicy)
from ezdxf.addons.drawing.layout import Page

# ---------------- CONFIG ----------------
# Uso ampliado (retrocompatible):
#   python bake_planta.py plano.dxf
#   python bake_planta.py piel.dxf --prefix PIEL_OESTE --out-js ../02_SLIDES_HTML/lib/piel_oeste.js --unit 0.001
_a = sys.argv[1:]
def _opt(nombre, defecto):
    return _a[_a.index(nombre) + 1] if nombre in _a else defecto
_pos = [x for i, x in enumerate(_a) if not x.startswith("--") and (i == 0 or not _a[i - 1].startswith("--"))]

INPUT   = _pos[0] if _pos else r"C:\Users\Ricardo SZ\Downloads\planta box.dxf"
PREFIX  = _opt("--prefix", "PLANTA")                     # nombre de las constantes JS
OUT_SVG = _opt("--out-svg", "planta_box.svg" if _opt("--prefix", "PLANTA") == "PLANTA" else _opt("--prefix", "PLANTA").lower() + ".svg")
OUT_JS  = _opt("--out-js", "../02_SLIDES_HTML/lib/planta_box.js")
UNIT_M  = float(_opt("--unit", 0.01))   # 1 unidad DXF -> m. 0.01 = cm (AutoCAD), 0.001 = mm (Revit)
LW_SCALE = float(_opt("--lwscale", 2.2))   # amplificacion de la jerarquia en pantalla

# Tabla CTB: color ACI -> grosor de ploteo (mm). EDITABLE.
CTB = {2:0.50, 1:0.18, 4:0.15, 3:0.20, 6:0.13, 7:0.13, 5:0.15, 8:0.10, 30:0.15,
       254:0.09, 255:0.09, 150:0.09, 130:0.13, 91:0.13, 131:0.13, 192:0.13, 113:0.35, 32:0.13,
       # --- exportacion DXF desde Revit: jerarquia de la piel ---
       52:0.09,   # A-GLAZ-CURT  panel Danpal
       51:0.18,   # A-GLAZ-CWMG  montantes
       12:0.35}   # S-BEAM       vigas y estructura

# Overrides quirúrgicos: el primero que calce manda. EDITABLE.
#   match por 'layer' (nombre exacto), 'ltype' (subcadena, p.ej. 'HIDDEN') o 'handle' (entidad única)
OVERRIDES = [
    {"handle": "249B2", "lw": 0.50},           # perimetro exterior de la ficha MINSAL gine: mismo peso que el modulo
    {"layer": "GD SUPERFICIES", "lw": 0.40},   # linea punteada exterior (perimetro del box) mas gruesa
    {"layer": "S-FSTN-____-OTLN", "lw": 0.22}, # uniones estructurales: detalle fino, no manchas
    # {"ltype": "HIDDEN", "lw": 0.20},         # ej.: todos los segmentados
    # {"handle": "24A03", "lw": 0.60},         # ej.: una entidad especifica
]
# ----------------------------------------

doc = ezdxf.readfile(INPUT)
msp = doc.modelspace()

# 1) fuera mascaras de ocultamiento (WIPEOUT) en modelspace y bloques
killed = 0
for layout in [msp] + [blk for blk in doc.blocks]:
    for e in list(layout):
        if e.dxftype() == "WIPEOUT":
            layout.delete_entity(e); killed += 1

# 2) grosores por capa segun CTB de colores
for ly in doc.layers:
    aci = ly.dxf.color if ly.dxf.color > 0 else 7
    ly.dxf.lineweight = int(CTB.get(aci, 0.13) * 100)

# 3) overrides por entidad (capa / tipo de linea / handle) — a nivel entidad ganan a la capa
def match(e, o):
    if "handle" in o and e.dxf.handle != o["handle"]: return False
    if "layer" in o and e.dxf.layer != o["layer"]: return False
    if "ltype" in o:
        lt = getattr(e.dxf, "linetype", "") or ""
        if lt.upper() in ("BYLAYER", ""):
            lt = doc.layers.get(e.dxf.layer).dxf.linetype
        if o["ltype"].upper() not in lt.upper(): return False
    return True

hits = 0
for layout in [msp] + [blk for blk in doc.blocks]:
    for e in layout:
        for o in OVERRIDES:
            if match(e, o):
                try: e.dxf.lineweight = int(o["lw"] * 100); hits += 1
                except Exception: pass
                break

# 4) render SVG monocromo blanco, fondo fuera, hatch fuera
cfg = Configuration(color_policy=ColorPolicy.CUSTOM, custom_fg_color="#ffffff",
    background_policy=BackgroundPolicy.OFF, lineweight_policy=LineweightPolicy.ABSOLUTE,
    lineweight_scaling=LW_SCALE, min_lineweight=0.05, hatch_policy=HatchPolicy.IGNORE)
backend = SVGBackend()
Frontend(RenderContext(doc), backend, config=cfg).draw_layout(msp, finalize=True)
svg = backend.get_string(Page(0, 0))
svg = re.sub(r'(<svg[^>]*?) width="[^"]*" height="[^"]*"', r"\1", svg, count=1)
open(OUT_SVG, "w", encoding="utf-8").write(svg)

# 5) asset JS del deck (con ancho real en metros para la escala grafica)
ext_min, ext_max = doc.header["$EXTMIN"], doc.header["$EXTMAX"]
w_m = (ext_max[0] - ext_min[0]) * UNIT_M
h_m = (ext_max[1] - ext_min[1]) * UNIT_M
bs = chr(92)
esc = svg.replace(bs, bs + bs).replace("`", bs + "`").replace("${", bs + "${")
js = ("/* Planimetria horneada desde DXF via bake_planta.py — lineas blancas, grosores CTB+overrides.\n"
      f"   Fuente: {INPUT.replace(chr(92), chr(47)).rsplit(chr(47), 1)[-1]} | {w_m:.2f} x {h_m:.2f} m */\n"
      f"const {PREFIX}_W_M={w_m:.4f};\n"
      f"const {PREFIX}_SVG=`" + esc + "`;\n")
open(OUT_JS, "w", encoding="utf-8").write(js)
print(f"wipeouts eliminados: {killed} | overrides aplicados: {hits} entidades")
print(f"plano real: {w_m:.2f} x {h_m:.2f} m | SVG KB: {len(svg)//1024} | JS -> {OUT_JS}")
