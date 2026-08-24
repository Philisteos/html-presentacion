# SLIDE 02 · "Salud lejos de todo"
> El Problema · criterio **Aporte del Proyecto al Entorno** · id `#s1` · ground cobalto

## 1. Idea (del usuario)
Mostrar el **territorio actual** y el problema logístico como un **trayecto A → B**:
- **A = planta industrializadora** — un **low-poly de galpón** que comunica "esto se fabrica en serie / industrializado".
- **B = el terreno** de Frutillar (Centinela de la Guacha) — ya lo tenemos (topografía de Gabriel).
- **Iconos de ubicación** (pines) en A y en B.
- El **traslado A→B considera tiempo y condiciones viales** — la idea de que *no se puede llegar a todos lados* fácil: el acceso difícil es el argumento.

## 2. Criterio de composición
- Retícula 12 col. **Panel de texto a la izquierda** (col 1–4): kicker "02 — EL PROBLEMA", título "Salud lejos de todo", bajada corta.
- **Zona 3D centro-derecha** (col 5–12): el **mapa/territorio wireframe** con el eje A→B en diagonal, pines A y B, y la línea de ruta segmentada.
- Densidad de datos: **3-4** anclados a la ruta (no racimo): distancia, tiempo estimado, tipo de vía, y una nota de accesibilidad.
- El 3D no tapa el panel; la ruta "entra" desde la izquierda para conectar con el texto.

## 3. Elementos 3D
| Elemento | Descripción | Fuente |
|---|---|---|
| Terreno B | Plano/relieve wireframe de la zona, con el pin B | Topografía Gabriel (QGIS/Google Earth) → placeholder por ahora |
| Galpón A (low-poly) | Nave industrial simple (cubierta a dos aguas + pórticos) que lea "fábrica" | Modelar (Three.js primitives o Blender→glTF) |
| Pines A y B | Iconos de ubicación (marcador) sobre cada punto | Icono 3D o sprite |
| Ruta A→B | Línea segmentada por **tramos** (asfalto / ripio / camino difícil), con nudos | Diseño |
| Anotaciones de tramo | Micro-etiquetas de condición vial por segmento | Diseño |

## 4. Datos flotantes (calculados)
A = **centroide de Puerto Montt** (ciudad más grande cercana, teórica) → B = **Centinela de la Guacha**.
Cálculo por haversine + factor de sinuosidad 1,45 y velocidades por condición vial:
- **Distancia total**: ~**71 km**.
- **Tiempo estimado**: ~**1 h 08 min**.
- **Tramos**: asfalto (Ruta 5) 57 km · 36 min → ripio 8 km · 11 min → camino difícil 6 km · 21 min (18 km/h, estacional).
- **Accesibilidad**: "no se llega en cualquier vehículo · últimos 6 km rurales estacionales".
> Valores estimados (A teórico). Ajustar si se define planta real o se mide la ruta.

## 5. Plan de trabajo
| Tarea | Responsable | Fuente | Estado |
|---|---|---|---|
| Low-poly galpón A | Claude (Three.js) | — | ⬜ |
| Terreno B wireframe | Claude placeholder → Gabriel real | topografía Frutillar | ⬜ |
| Pines A/B + iconos ubicación | Claude | — | ⬜ |
| Ruta segmentada por condición vial | Claude | — | ⬜ |
| Datos reales (km, tiempo, vías) | Riki/Gabriel | mapa real ruta a Centinela de la Guacha | ⬜ dato pendiente |
| Integrar a #s1 con composición col 12 | Claude | DESIGN_SYSTEM | ⬜ |

## 6. Datos que faltan (bloquean el contenido real, no el build)
- Coordenadas/ubicación de la **planta industrializadora** de referencia (¿Promet? ¿ciudad?) para A.
- **Km y tiempo reales** del trayecto a Centinela de la Guacha.
- **Condición vial** por tramo (asfalto/ripio/rural).

## 7. Spec de construcción → CONSTRUIDO (v1)
Implementado en `02_SLIDES_HTML/index.html`, slide index 1 (`#s1`):
- Grupo `prob` con: **galpón low-poly** (caja + cubierta a dos aguas + 3 pórticos), **terreno B** (3 curvas de nivel + domo de relieve, placeholder `// TODO topografía real Gabriel`), **2 pines** (cono ámbar + anillo pulsante), **ruta de 3 tramos** (asfalto continuo → ripio guionado → camino difícil punteado).
- Estado `st.abDraw` (fade-in), gate `prob.visible = current===1`. Escena corrida a la derecha (`prob.position.x=8`) + cámara `{x:-8,y:22,z:42,tx:8}` → mitad izquierda libre para texto (panel `#s1` a `max-width:44%/470px`).
- **4 callouts**: A·Planta MMC (Puerto Montt teórico), B·Centinela de la Guacha, ≈71 km · 1 h 08 min (asfalto→ripio→camino rural), últimos 6 km rural estacional.
- Verificado en navegador: A abajo-izq del cluster, B arriba-der, ruta segmentada, pines, texto sin tapar. Estado: ✅ base construida (datos reales de km/tiempo estimados por haversine; ajustar si se define planta/ruta reales).

## 8. Modelo 3D del galpón (v3 — modelo limpio CC0)
- Galpón = **modelo low-poly real** en wireframe. Tras probar "Warehouse" de Lavender Harmony (CC-BY, muy denso ~8600 aristas → saturado), se cambió a **"Barn" de CreativeTrio** (Poly Pizza), licencia **CC0 (dominio público, sin atribución)**.
- **Limpieza de fachada**: horneado con `EdgesGeometry` + **filtro que elimina las tablas cortas del techo** (aristas en el 50% superior con largo < 50% del span) → fachada limpia con **portón central visible**. Resultado ~1690 vértices.
- **Integración offline**: solo la geometría de aristas normalizada, base64 en `lib/galpon_wire.js` (**27 KB**). El deck la decodifica a `LineSegments`. Sin GLTFLoader ni red. .glb fuente en `04_ASSETS/modelos_3d/`.
- Escala S=7, base a nivel de suelo. **Giro lento** solo en slide 02 (mapa); escena en `x=10`, panel `#s1` 40% → barrido verificado sin tocar texto.
- **Íconos de ubicación**: marcador "map pin" (gota) billboard a cámara + anillo pulsante en suelo.

## 9. Slide 03 "Nace en fábrica" — zoom a la planta
- Transición 02→03: la cámara **hace zoom al galpón A** (`SLIDES[2].cam` cerca de la nave). El grupo `prob` queda visible en slides 1 y 2; el giro del galpón se detiene en slide 03 para leer la fachada.
- **Módulo Metalcon que "nace"**: caja wireframe (`bornMod`, estado `st.moduleBorn` 0→1) que se dibuja y **emerge del galpón** (avanza en Z). Encuadre con el cluster a la izquierda y panel de texto a la derecha (`#s2` 42%).
- ⚠️ **Continuidad pendiente 03→04**: la slide 04 (viaje) todavía usa el camión/ruta del esquema antiguo en `x≈-60`, separado del galpón A. Próximo paso: **re-basar el 1er acto** (viaje desde el galpón A → montaje en el terreno B) para que todo fluya desde esta planta.

## 9-bis. Slide 02 v3 — secuencia spur.us (globo → descenso → recuadros → galpón)
Al entrar a la slide 2 corre una secuencia automática (~5 s, GSAP timeline `introTl`, re-entrable):
1. **Globo 3D** (graticule crema + nube de 520 puntos + marcador ámbar pulsante en Centinela de la Guacha, lat −41,1 lon −73,0) con etiqueta `#globeTag` (REGIÓN DE LOS LAGOS · coords).
2. **Descenso**: la cámara baja hacia el marcador; el globo escala 2,5× y se desvanece mientras aparece el mapa A→B (el descenso presenta el terreno).
3. **Recuadros de ubicación** estilo satelital (`rectFrame`: marco + ticks de esquina) en A y B, con cajas `.locbox` estilo spur (panel oscuro, bullet cuadrado ámbar, título mono + coordenadas): "A · PLANTA MMC / 41°28'S 72°56'W" y "B · TERRENO / 41°06'S 72°57'W". Reemplazan los callouts ptA/ptB.
4. **Elemento 3D**: recién entonces se dibuja el galpón (giro lento). El camión NO aparece aquí (slide 3).
Estados nuevos: `st.globe/frameDraw/galponIn`; `goTo(1)` dispara `playIntro()` (o `introSkip()` si instant); salir mata la timeline. Slide 3 lista `galponIn:1` para acceso directo. Colores propios (cobalto/crema/ámbar), sin el verde spur. Verificado: fases, re-entrada 2→3→2, slide 3 sin globo/recuadros.

## 10. Slide 03 v2 — camión hi-res + paleta ref + sin terreno
- **Galpón limpio (barn CC0)** cambiado por modelo denso; techo filtrado → fachada limpia con portón central. En slide 03 el galpón deja de girar (protagonista, arriba con pin A).
- **Camión a escala real**: tractor "Basic Semi-truck" de WilliWam (Poly Pizza, **CC0**) horneado a wireframe (`lib/truck_wire.js`, 45 KB) + **plataforma modelada a mano** (deck 13 m, gooseneck, 3 ejes de ruedas) cargando el **módulo 3,5×8×3,2 m**. Rig completo en `truckRig`, escala 0.44, en primer plano-izquierda.
- **Slide 03 sin terreno B** (se oculta terr/pinB/ringB/ruta en slide 2) y **zoom más cerca**. Cluster a la izquierda, panel de texto a la derecha (`#s2` 42%).
- **Paleta adoptada de oci.madebybuzzworthy.com**: fondo **azul profundo `#1925AA`** + tinta **crema `#E8E6E0`** (wireframe), acento ámbar propio. Afecta todo el deck.
- ⏳ **Pendiente de la adopción gráfica**: falta la **tipografía** (Geist Sans medium sentence-case + Geist Mono, embebidas offline) — reemplaza la condensada mayúscula actual. Es el próximo paso.
