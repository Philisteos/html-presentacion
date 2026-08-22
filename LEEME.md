# Deck PAC 7.0 — equipo PAC7.0-WSEF

> Sincronizado el **22-ago-2026** · versión **v29** (13 slides).
> Esta carpeta es el espejo de trabajo. La fuente viva está en el equipo de Ricardo.

## Qué abrir

| Quiero… | Archivo |
|---|---|
| **Solo verlo / presentarlo** | `PAC7.0-WSEF_deck_v29.html` — doble clic, funciona offline y sin carpetas adyacentes |
| **Editarlo** | `02_SLIDES_HTML/index.html` — necesita la carpeta `lib/` al lado (ya está) |

## Cómo se navega
- **← →**, rueda o swipe para cambiar de slide · **Home / End** para saltar al inicio o al final.
- **E** en la portada abre el panel de edición del visor ASCII (o el ⚙ discreto abajo a la derecha).
- Botones dentro de las slides:
  - **05** ▲ EXPLOTAR MÓDULO — separa las 7 capas y la cámara se aleja sola
  - **06** ▶ INICIAR MONTAJE — secuencia 4D de 5 fases (tipo SynchroPro)
  - **07** ⇄ INDUSTRIALIZACIÓN DEL MÓDULO — barrido entre planta tipo MINSAL y planta del módulo
  - **08** ▼ DESPLEGAR CORTE A–A' — el corte se abre dentro de la misma slide

## Las 13 slides
`01` Portada · `02` El problema · `03` Nace el módulo · `04` **Sistemas MMC** · `05` El módulo ·
`06` El montaje · `07` Vida interior · `08` Plano general · `09` La piel · `10` Detalles constructivos ·
`11` Imagen 01 · `12` Imagen 02 · `13` Cierre

## Qué falta (placeholders a la espera de archivos)
- **DXF**: planta del módulo (07-B), planta general + corte A–A' (08), escantillón (10).
- **IFC por elemento** para la secuencia de montaje (hoy es geometría procedural).
- **Imágenes**: render exterior héroe y render interior (slides 11 y 12).
- ⚠️ **Confirmar con Nicolás** si Sto Chile provee **StoPanel** (panel prefabricado) o si la vía local es StoTherm panelizado. El deck ya lo nombra como StoPanel.

## Si tienes un plano CAD que integrar
1. En AutoCAD: **Guardar como → DXF 2018** (no hace falta configurar ploteo).
2. Reglas para que los grosores lleguen bien: todo **ByLayer**, una capa = un concepto = un grosor, tipos de línea estándar, `PURGE` antes de exportar.
3. Se hornea con `_DOCS/bake_planta.py` (DXF → SVG blanco con jerarquía de grosores). La tabla vigente de grosores está en `_DOCS/TABLA_GROSORES.md`.

## Documentación
`_DOCS/CLAUDE.md` — registro de decisiones (PRES-001…022) · `_DOCS/00_REGISTRO_SLIDES.md` — ficha por slide ·
`_DOCS/DESIGN_SYSTEM.md` — criterio gráfico · `_DOCS/PLAN_PRESENTACION.md` — narrativa y cronograma.

**Anonimato**: en todo entregable solo aparece el código **PAC7.0-WSEF**. Sin nombres ni instituciones.
