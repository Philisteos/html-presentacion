# Plan Estratégico — Deck HTML tipo Madar · PAC 7.0
> Equipo **PAC7.0-WSEF** · Creado 2026-07-18 tras entrevista de definición · Complementa `PLAN_PRESENTACION.md`
> Referencia tecnológica: https://madarplatform.com/en (Three.js + wireframe "webgl-lines" + scroll-driven)

---

## A. Resumen de la entrevista (lo acordado)

1. **Objetivo**: deck HTML scroll-driven tipo Madar que ES la entrega oficial (autorizado entregar HTML en vez de PPT). Plan B: video = grabación del scroll. Las animaciones van sí o sí.
2. **Destinatario**: jurado PAC 7.0 (Diego Mellado, Carolina Briones, Pabla Ortúzar) + equipo (pitch/ensayos).
3. **Concepto narrativo**: **HÍBRIDO viaje + edificio** —
   - *Acto 1*: un módulo Promet nace en fábrica (off-site), viaja en camión a Frutillar y se monta.
   - *Acto 2*: la posta armada se explora por capas (habitabilidad, térmica, entorno, escalabilidad, innovación).
4. **Ingredientes Madar rescatados (los 4)**:
   - Objeto 3D **wireframe que se dibuja** ante el ojo (efecto "dibujo técnico vivo").
   - **Datos flotantes anclados** al objeto (U≤0,40 · 200 m² · ~2h/módulo · Zona G…).
   - **Cámara scroll-driven**: el scroll mueve cámara y escena, sin cortes.
   - **Ritmo editorial**: numeración de capítulos, textos sincronizados, scroll suave.
5. **Estilo**: **FUSIÓN técnica + PAC** — wireframe como esqueleto narrativo; paleta, tipografía y láminas de contenido (plantas, renders) siguen el lenguaje de TOP 3 6.0. Defendible ante la regla de estilo de las bases.
6. **Geometría 3D**: **placeholder primero** (volúmenes genéricos) → se enchufa la geometría real (Revit export → glTF, o Blender ligero) cuando el diseño esté cerrado.
7. **Formato de salida**: idealmente **archivo autocontenido** (abre offline con doble clic); link hosteado como alternativa/respaldo.
8. **Calidad**: **pareja en todo el recorrido** — no hay un solo "money shot"; la experiencia completa es el argumento.
9. **Roles y flujo**: Ricardo + Claude construyen; **Javier itera**. Carpeta espejo en Dropbox:
   `C:\Users\Ricardo SZ\Dropbox\PAC\03_PRESENTACION_CLAUDE\`
   **Regla**: cuando Ricardo indique "guardado importante", Claude copia la versión vigente del deck ahí para revisión de Javier.

### Riesgos identificados
| Riesgo | Mitigación |
|---|---|
| La organización revierte el permiso de entregar HTML | Plan B listo: video = scroll grabado + PPT de capturas. Diseñar cada capítulo para que funcione también como frame estático. |
| Peso/rendimiento en laptop promedio del jurado | Presupuesto duro: geometría low-poly, texturas mínimas, objetivo <25 MB autocontenido, 60 fps en integrada. |
| Partido general atrasado bloquea la geometría real | El pipeline placeholder desacopla: la animación avanza sin el diseño final. |
| Wireframe dark rompe la regla de estilo PAC | Estrategia fusión + validar look con referencias TOP 3 6.0 antes de la semana 3. |
| Un solo archivo HTML gigante difícil de editar | Desarrollo modular (secciones/JS separados) + build de empaquetado a autocontenido solo para entregas. |

---

## B. Arquitectura narrativa del deck (v1)

**Capítulos scroll (numeración 01–08 visible, estilo Madar):**

| Cap | Acto | Escena 3D | Criterio jurado | Datos flotantes (ejemplos) |
|---|---|---|---|---|
| 00 Portada | — | Módulo wireframe se dibuja desde líneas + código PAC7.0-WSEF | — | — |
| 01 El problema | 1 | Mapa/terreno wireframe: Chile → Los Lagos → Centinela de la Guacha | Aporte al entorno | "difícil acceso" · Zona térmica G |
| 02 La respuesta | 1 | El módulo nace en planta (off-site) | Estrategia MMC | fabricación controlada · Metalcon |
| 03 El viaje | 1 | Módulo sobre camión recorriendo la ruta (homenaje directo a Madar) | Estrategia MMC | dimensiones transporte · km a Frutillar |
| 04 El montaje | 1→2 | Módulos aterrizan y se ensamblan; la posta toma forma | MMC / Innovación | ~2 h/módulo · hasta 40% menos plazo |
| 05 La vida interior | 2 | Cámara entra: programa clínico por capas (PMA) | Habitabilidad | 200 m² · fichas MINSAL · 3 recintos |
| 06 La piel | 2 | Radiografía de envolvente: Sto EIFS + SIP capa por capa | Diseño pasivo / Innovación | U≤0,40 · Rt≥2,50 · 5 ach@50Pa · junta sin puente térmico |
| 07 El territorio | 2 | Zoom out: la posta en el paisaje; réplicas aparecen en otras localidades | Entorno / Escalabilidad | catálogo de módulos · plantas Talca/Valdivia |
| 08 Cierre | — | La posta completa, líneas → render real (fusión wireframe→realidad) | síntesis | PAC7.0-WSEF |

> La transición final "wireframe → render fotorrealista" es la firma de la estrategia FUSIÓN: el dibujo técnico cobra vida.

---

## C. Stack técnico

- **Three.js** (escena 3D) + efecto líneas (`LineSegments`/edges geometry o `three-mesh-line`) para el wireframe que se dibuja (animación de `drawRange`/dash offset).
- **GSAP + ScrollTrigger** (timeline maestra ligada al scroll) + **Lenis** (scroll suave).
- **glTF (.glb) comprimido (Draco)** como formato de geometría; placeholders primitivos en fase 1.
- **Datos flotantes**: HTML/CSS posicionado por proyección 3D→2D (no texturas), para nitidez y edición fácil.
- **Build**: desarrollo modular (Vite) → `npm run build` + inline a **un solo HTML autocontenido** para entregas.
- Presupuesto de rendimiento: <25 MB total · 60 fps en GPU integrada · funciona offline file://.

---

## D. Cronograma estratégico (regresivo desde 23-ago)

| Semana | Fechas | Hito del deck | Gate de calidad |
|---|---|---|---|
| **S1** | 18–26 jul | **Prototipo de maquinaria**: escena Three.js con módulo placeholder que se dibuja en wireframe + scroll controlando cámara + 1 dato flotante anclado. | ¿Se siente "Madar"? Demo a Javier vía Dropbox. |
| **S2** | 27 jul–02 ago | **Esqueleto completo**: los 8 capítulos navegables con placeholders, textos v1, análisis TOP 3 6.0 → paleta/tipografía fusión aplicada. | Recorrido completo sin bugs; estilo validado contra TOP 3. |
| **S3** | 03–09 ago | **Geometría real**: export Revit/Blender → glTF del módulo y la posta (según avance del partido general); datos flotantes definitivos; primeros renders integrados. | La posta real reemplaza placeholders sin romper animación. |
| **S4** | 10–16 ago | **Contenido completo + pulido**: renders IA (con trazabilidad), transición wireframe→render del cierre, música/narración si aplica; **grabar video Plan B**. | Ensayo de pitch con equipo; deck funciona en 3 laptops distintas. |
| **S5** | 17–22 ago | **Empaquetado y control final**: build autocontenido, test offline, control de anonimato (cero nombres), respaldos (hosting + video). | Checklist de entrega 100%; Javier y Gabriel aprueban. |
| **D** | **23-ago** | **ENTREGA** | — |

**Regla de oro del cronograma**: la maquinaria (S1–S2) no depende del proyecto arquitectónico; solo S3 lo necesita. Si el partido general se atrasa, el deck sigue avanzando.

---

## E. Próximos 3 pasos inmediatos

1. **Prototipo S1**: montar en `02_SLIDES_HTML/` la escena base (Three.js + GSAP ScrollTrigger + módulo placeholder wireframe dibujándose).
2. **Análisis TOP 3 6.0**: extraer paleta/tipografía/composición de las referencias del Dropbox → `03_REFERENCIAS/` (define la mitad "PAC" de la fusión).
3. **Confirmar con la organización por escrito** el formato de recepción del HTML (¿archivo? ¿link? ¿peso máximo?) — aprovechar el canal con Nicolás.
