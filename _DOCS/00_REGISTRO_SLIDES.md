# Registro de Slides — Deck PAC 7.0
> Equipo **PAC7.0-WSEF** · Una ficha por slide (composición + contenido 3D + datos + plan de trabajo).
> Base del sistema: [DESIGN_SYSTEM.md](../DESIGN_SYSTEM.md). Ground actual: **cobalto en todo el deck** (wireframe/ASCII blancos).

## Cómo se registra cada slide
Cada slide tiene una **ficha** `SLIDE_NN_nombre.md` en esta carpeta con:
1. **Tema y criterio del jurado** que ataca.
2. **Criterio de composición** — retícula 12 col: dónde va el panel de texto, dónde la zona 3D, densidad de datos.
3. **Elementos 3D** — qué se modela/muestra en la escena.
4. **Datos flotantes** — qué métricas y cuántas.
5. **Plan de trabajo** — tareas, responsable, fuente, estado.
6. **Spec de construcción** — el prompt optimizado para construir la slide.

## Índice y composición asignada

| # | Slide (id) | Tema · criterio | Composición (panel / zona 3D) | Datos | Técnica 3D | Estado | Ficha |
|---|---|---|---|---|---|---|---|
| 01 | PORTADA (s0) | Identidad | Split: texto izq 46% / ASCII der 46% | 4 (toggle) | ASCII rotable | ✅ base | — |
| 02 | EL PROBLEMA (s1) | Salud lejos de todo · Aporte al entorno | Texto izq / **mapa A→B** centro-der | 4 (ruta) | Wireframe mapa + galpón low-poly | ✅ **base** | [SLIDE_02](SLIDE_02_salud-lejos-de-todo.md) |
| 03 | NACE EL MÓDULO (s2) | La respuesta · MMC | Texto der / módulo+fábrica izq | 2 | Wireframe | ⬜ pendiente | — |
| 04 | SISTEMAS MMC (sMMC) | Estrategia MMC · Innovación | Texto izq / tabla exigencia→sistema der | 4 filas | Lámina tipográfica | ✅ base |  |
| 05 | EL MÓDULO (s3) | Anatomía · MMC | Texto der / módulo explotable | 7 capas | Axo paralela | ✅ base (IFC pendiente) |  |
| 06 | EL MONTAJE (s4) | Ensamblaje · MMC/Escala | Texto der / secuencia 4D SynchroPro (5 fases) | HUD fase | Wireframe axo paralela | ✅ base (IFC pendientes) | — |
| 07 | VIDA INTERIOR (s5) | Normativa MINSAL → módulo | Texto izq / planta DXF + transición ⇄ "Industrialización del módulo" | caption cota + escala gráfica | Lámina SVG (2 DXF) | ✅ base (DXF módulo pendiente) | — |
| 08 | PLANO GENERAL (sPG) | Habitabilidad · Entorno | Texto izq / planta general + corte A–A' desplegable ▼ | caption cota | Lámina SVG (DXF pendientes) | 🔨 placeholders | — |
| 09 | LA PIEL (s6) | Térmica · Diseño pasivo | Texto der / envolvente explotada | 3-5 racimo | Wireframe | ⬜ pendiente | — |
| 10 | DETALLES CONSTRUCTIVOS (sDET) | Innovación técnica · Pasivo | Texto izq / **escantillón** vertical der | caption cota | Lámina SVG (DXF pendiente) | 🔨 placeholder | — |
| 11 | IMAGEN 01 (sIMG1) | Render exterior héroe | Marco centrado + caption cota | — | Imagen (pendiente, IA+trazab.) | 🔨 placeholder | — |
| 12 | IMAGEN 02 (sIMG2) | Render interior peatonal | Marco centrado + caption cota | — | Imagen (pendiente, IA+trazab.) | 🔨 placeholder | — |
| 13 | CIERRE (s9) | Síntesis | Centrado | — | — (cobalto) | ✅ base | — |

> Eliminadas 2026-08-17: EL TERRITORIO (contenido absorbible en 03/09) y ENTREGABLES (el índice de producción vive en este doc y en PLAN_PRESENTACION.md).

**Leyenda estado:** ✅ base lista · 🔨 en construcción · ⬜ pendiente.

## Orden de trabajo (por tema)
Vamos slide por slide, cerrando composición → contenido 3D → datos → build. Actual: **SLIDE 02**.
