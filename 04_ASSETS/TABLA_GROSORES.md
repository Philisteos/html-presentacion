# Tabla de grosores — planimetrías CAD → deck PAC 7.0
> Fuente de verdad ejecutable: [`bake_planta.py`](bake_planta.py) (CTB + OVERRIDES).
> Este doc es su espejo legible. Para cambiar algo: pedirlo en el chat en una línea
> ("capa X → 0,45" / "todo lo HIDDEN → 0,20" / "color amarillo → 0,50") y se re-hornea.

## Reglas del flujo (lado CAD)
1. Todo **ByLayer** (color, tipo de línea, grosor) — cero overrides por objeto.
2. **Una capa = un concepto = un grosor**; si un concepto necesita dos pesos, se divide la capa.
3. Tipos de línea **estándar** (Continuous, HIDDEN, DASHED, CENTER).
4. Bloques con interior ByBlock/ByLayer.
5. `PURGE` y exportar **DXF 2018** (guardar-como, sin ploteo). Wipeouts se eliminan solos.

## Tabla base por color (CTB) — vigente
| Color ACI | Uso típico | Grosor (mm) |
|---|---|---|
| 2 amarillo | muros | 0,50 |
| 3 verde | instalaciones | 0,20 |
| 1 rojo | ventanas | 0,18 |
| 4 cian | mobiliario | 0,15 |
| 5 azul | equipos móviles | 0,15 |
| 7 blanco | textos, cotas | 0,13 |
| 6 magenta | superficies | 0,13 |
| 8 plomo | segmentados aux. | 0,10 |
| 250+ grises | tramas, referencias | 0,09 |
| (otro color) | — | 0,13 por defecto |

## Overrides vigentes (ganan sobre la tabla)
| # | Objetivo | Match | Grosor |
|---|---|---|---|
| 1 | Línea punteada exterior (perímetro del box) | capa `GD SUPERFICIES` | 0,40 |

## Parámetros del render
- Unidades: **1 unidad DXF = 1 cm** (validado: box 480 u = 4,80 m; camilla 200 u = 2,00 m).
- Amplificación en pantalla: ×2,2 (`LW_SCALE`).
- Escala: **escala gráfica real** en la slide (barra de 2 m derivada de `PLANTA_W_M`); escala nominal exacta se calcula al exportar a PPT/A1.

## Historial
- 2026-08-17 · `planta box.dxf` (ficha equipamiento box consulta 4,81×2,74 m) → `lib/planta_box.js` · primera tabla + override marco exterior.
