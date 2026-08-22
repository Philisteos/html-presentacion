# CLAUDE.md — PAC 7.0 · PRESENTACIÓN (equipo PAC7.0-WSEF)
> Última actualización: 2026-07-18. Carpeta dedicada 100% a producir y pulir la presentación del concurso.

## 0. Regla de oro: dónde está el contexto
El **contexto maestro del proyecto** (concurso, hitos, sistema constructivo, norma térmica, equipo, actas) vive en:

`C:\Users\Ricardo SZ\Desktop\CLAUDE - WORKS\PAC 7.0 - CLAUDE`

**Al iniciar cada sesión en esta carpeta, leer primero** `CLAUDE.md` y `00_INDICE_ACUERDOS.md` de esa carpeta. Es la fuente de verdad y se actualiza continuamente: **nunca duplicar su contenido aquí, solo referenciarlo.** Ante contradicción, prima la carpeta maestra.

## 1. Objetivo de esta carpeta
Producir la **1ª entrega digital del 23-ago-2026** (filtro de finalistas): imágenes insertas en un PowerPoint + video explicativo. Y servir de base para la 2ª entrega (16-oct: láminas A1 + memoria + video).

## 2. Decisiones de diseño (registro)
| ID | Fecha | Decisión |
|---|---|---|
| PRES-001 | 2026-07-18 | **El HTML es el formato central**: funciona como nuestro "PPT" para el pitch interno/ensayos **y** es la base exportable de la que salen el PowerPoint oficial (capturas/exportes de cada slide) y el material del video. |
| PRES-002 | 2026-07-18 | Estructura narrativa basada en los **6 criterios del jurado**: habitabilidad, diseño pasivo, aporte al entorno, estrategia MMC, escalabilidad, innovación técnica. |
| PRES-003 | 2026-07-18 | **Deck scroll-driven tipo Madar** (madarplatform.com/en): objeto 3D wireframe como hilo conductor total. Concepto **híbrido viaje + edificio** (módulo Promet viaja y se monta → posta se explora por capas). Ver `PLAN_ESTRATEGICO_DECK.md`. |
| PRES-004 | 2026-07-18 | **Autorizado entregar el HTML como si fuera el PPT.** Plan B si revierten: video = scroll grabado + PPT de capturas. Animaciones van sí o sí. |
| PRES-005 | 2026-07-18 | Estilo **FUSIÓN técnica + PAC**: wireframe como "dibujo técnico vivo"; paleta/tipografía/láminas siguen TOP 3 6.0. |
| PRES-006 | 2026-07-18 | Geometría 3D: **placeholders primero**, geometría real (Revit→glTF o Blender) cuando el diseño esté cerrado. |
| PRES-007 | 2026-07-18 | Salida: **archivo HTML autocontenido** (offline, doble clic) como objetivo; link hosteado de respaldo. Presupuesto: <25 MB, 60 fps en GPU integrada. |
| PRES-008 | 2026-07-18 | Flujo de equipo: Ricardo+Claude construyen, **Javier itera** vía carpeta espejo `C:\Users\Ricardo SZ\Dropbox\PAC\03_PRESENTACION_CLAUDE\`. Cuando Ricardo indique "guardado importante", Claude sincroniza la versión vigente ahí. |

| PRES-009 | 2026-07-18 | **Pivot de formato tras ver Prototipo 1**: NO scroll vertical continuo → **slides horizontales deslizables** (flechas/teclado/swipe/rueda, como un PPT). Estética: **Madar tal cual** (fondo oscuro high-tech, wireframe claro, acento ámbar), reemplaza la "fusión clara" del prototipo 1. El design system propio se diseña después sobre esta base. |

| PRES-010 | 2026-07-18 | **Tono gráfico elegido: "Ingeniería sobria y precisa"** (Tono 1 de la prueba de 4): sans condensada mayúscula + mono para datos, composición con 3D contenido (no a pantalla completa), retícula de 12 columnas. |
| PRES-011 | 2026-07-18 | **Paleta cruzada (v1 fijada)**: sistema de dos grounds — **MODO COBALTO `#1466E0`** (hero/portada/divisores de acto/cierre) + blanco puro, y **MODO TÉCNICO `#0A0F14`** (slides densas de datos/wireframe/planimetría). Hilo constante: tinta blanca + acento **ámbar `#FF8A2B`**. Cobalto confirmado en su saturación actual. Tinta hielo wireframe `#E9F1FA`, panel `#0E151C`, texto sec. dark `#7D8D99` / cobalto `#D6E6FB`. |

| PRES-012 | 2026-07-18 | **Design system formalizado** en `02_SLIDES_HTML/theme.css`: tokens de la paleta v1 (dos grounds + ámbar), tipografía Tono 1 (display condensada MAYÚS + mono datos), escala tipográfica, retícula 12 col y primitivos (`.kicker/.title/.body/.chip`). El deck se re-skinea con estos tokens al cerrar la entrevista de criterio gráfico. (theme-factory se activó pero requiere sesión nueva para cargar; el tema se autoró a mano.) |

| PRES-013 | 2026-08-17 | **Globo 2D día**: mapa NASA Blue Marble (PD) con contraste continente/océano, resolución fija máxima (300), rotación que se **alinea a Chile** y zoom anclado al marcador antes del descenso. Slider de resolución eliminado. |
| PRES-014 | 2026-08-17 | **Planta industrializadora procedural** reemplaza al barn CC0: nave a dos aguas + anexo + monitor de cumbrera + estanque + explanada + cierre perimetral con acceso (wire + ocultadores de la misma geometría → alineación perfecta). libs galpon_* fuera del deck (−150 KB). |
| PRES-015 | 2026-08-17 | **Slide 04 en proyección paralela** (axo técnica sin fuga): cámara lejana + fov 4,5° por-slide (`SLIDES[].fov`), niebla anulada en esa slide, primer plano armado ↔ vista amplia explotada. |
| PRES-016 | 2026-08-17 | **Rótulos técnicos → COTA TÉCNICA (alternativa C elegida)**, estética OCI: micro-etiqueta MAYÚS sobre línea de cota con ticks 45° + valor mono blanco + secundario atenuado. Sin cajas/blur/ámbar. Aplicado a los 24 callouts + etiqueta del globo; capas del explode en 2 columnas limpias (offset `px` en pantalla). Propuesta comparativa en artifact "Anotaciones OCI". |

| PRES-017 | 2026-08-17 | **Slide 05 EL MONTAJE → secuencia constructiva 4D estilo SynchroPro**: 5 fases de abajo hacia arriba (tornillos de fundación → vigas aligeradas perforadas → suelo ventilado RF → módulo volumétrico → fachada inclinada proyectada en cubierta). Cada fase entra en ámbar "en obra" y asienta a crema; HUD de fase estilo cota + barra segmentada; axo paralela (fov 4,5°); botón ↻ repetir. Geometría procedural placeholder → se reemplazará por los IFC por elemento que enviará Ricardo. |

| PRES-018 | 2026-08-17 | **Pipeline planta CAD → deck (probado con "planta box.dxf")**: DXF (guardar-como desde AutoCAD, sin ploteo) → ezdxf drawing add-on con **tabla CTB color→grosor** inyectada en capas + WIPEOUTs eliminados + hatch ignore → SVG monocromo blanco (`lib/planta_box.js`, ~145 KB) → lámina en slide 06 con barrido de revelado tipo plóter + caption cota. Tabla CTB editable en el script de horneado (04_ASSETS/planta_box.svg es el intermedio). DWG/DWF no sirven (binarios propietarios); siempre pedir DXF. |

| PRES-019 | 2026-08-17 | **Deck pasa a 11 slides.** Slide 06 = planta tipo MINSAL con transición **"Industrialización del módulo"** (botón ⇄: barrido A→B entre dos DXF; B placeholder hasta recibir el DXF del módulo). **Nueva slide 07 "PLANO GENERAL"**: planta general con línea de sección A–A' y **corte desplegable dentro de la misma slide** (botón ▼; planta y corte placeholders → DXF pendientes). LA PIEL→08, TERRITORIO→09, ENTREGABLES→10, CIERRE→11. Todos los placeholders se reemplazan con `bake_planta.py` al llegar los archivos. |

| PRES-020 | 2026-08-17 | **Deck pasa a 12 slides.** Se elimina EL TERRITORIO (09) → entra **DETALLES CONSTRUCTIVOS** (escantillón vertical, DXF pendiente). Se elimina ENTREGABLES (10) → posiciones 10 y 11 = **slides de IMAGEN** (marco placeholder para render exterior héroe / render interior; par maqueta+IA con trazabilidad). CIERRE → 12. El índice de entregables sigue documentado en `01_GUION/00_REGISTRO_SLIDES.md` y `PLAN_PRESENTACION.md`. |

| PRES-021 | 2026-08-18 | **Deck a 13 slides: nueva 04 SISTEMAS MMC.** Se separa el discurso: la 04 argumenta los **sistemas y criterios MMC** y la 05 mantiene el módulo explotado. Estructura elegida (entrevista): **condición del encargo → sistema que responde**, jerarquía estrategia (01 módulo transportable, 02 fachada prefabricada) vs complemento (03 SIP, 04 construcción en seco). **Sin descartes en pantalla** (Facoro/Crillón no aparecen): se argumenta hacia adelante. |
| PRES-022 | 2026-08-18 | **Marca de fachada: StoPanel** (decisión de Ricardo). Sto industrializado = panel prefabricado en fábrica, no EIFS aplicado en obra; argumento clave para Frutillar (sin faena húmeda, menos dependencia del clima) y Sto lo lista para proyectos de salud. Propagado a portada, capa 06 del explode, LA PIEL y junta entre módulos. ⚠️ **Verificar con Nicolás si Sto Chile provee StoPanel** o si la vía local es StoTherm panelizado. |

*(Agregar aquí cada nueva decisión: paleta, tipografías, orden de slides, herramienta de video, etc.)*

## 3. Restricciones no negociables (de las bases)
- **Anonimato estricto**: solo el código **PAC7.0-WSEF** en todo entregable. Sin nombres, correos ni instituciones.
- **Estilo gráfico** basado en entregas anteriores de PAC → referencias `TOP 3 6.0` en Dropbox `/PAC/00_ANTECEDENTES/01_RECURSOS/1 REU PAC 7.0/TOP 3 6.0/`.
- **Renders con IA permitidos** solo con trazabilidad: comparación maqueta digital vs output IA + el prompt utilizado → guardar todo en `04_ASSETS/RENDERS_IA_TRAZABILIDAD/`.
- Entregable oficial 23-ago: **PowerPoint + video** (el HTML es interno/base de exporte, no se entrega como tal).

## 4. Estructura de esta carpeta
- `PLAN_PRESENTACION.md` — narrativa, lista de imágenes, responsables y cronograma regresivo.
- `01_GUION/` — guion del pitch y del video, textos por slide.
- `02_SLIDES_HTML/` — el deck HTML (fuente central de la presentación).
- `03_REFERENCIAS/` — análisis de estilo de TOP 3 6.0 y otras referencias gráficas.
- `04_ASSETS/` — renders, diagramas, esquemas, axonometrías listos para insertar.
  - `RENDERS_IA_TRAZABILIDAD/` — pares maqueta/IA + prompts (exigencia de las bases).
- `05_VIDEO/` — guion técnico, clips, música, versiones del video explicativo.
- `06_EXPORTS/` — entregables: PPT oficial exportado desde el HTML, video final, PDFs.

## 5. Flujo de trabajo HTML → entregables
1. Se diseña y pule todo en `02_SLIDES_HTML/` (una slide = una sección/pantalla).
2. El pitch y los ensayos del equipo se hacen directo en el navegador.
3. Para la entrega oficial: cada slide se exporta a imagen (resolución 16:9, mín. 1920×1080) y se inserta en el PowerPoint en `06_EXPORTS/`.
4. El video explicativo reutiliza las mismas slides/animaciones como material base.
