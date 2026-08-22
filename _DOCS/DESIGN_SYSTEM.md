# Design System — Deck PAC 7.0 · "Ingeniería sobria"
> Equipo **PAC7.0-WSEF** · Brief cerrado 2026-07-18 tras entrevista de criterio gráfico.
> Tokens implementados en [`02_SLIDES_HTML/theme.css`](02_SLIDES_HTML/theme.css). Este doc es la fuente de verdad del criterio; el CSS es su ejecución.

## 1. Objetivo
Un sistema gráfico que haga el deck **coherente, memorable y defendible** ante el jurado PAC 7.0, transmitiendo *ingeniería sobria y control industrial* sin sacrificar la habitabilidad del proyecto. Debe sostener 10 slides horizontales con 3D, texto y datos, respetando anonimato PAC7.0-WSEF y dialogando con el estándar gráfico de PAC (TOP 3 6.0).

## 2. Tono (decidido)
**Ingeniería sobria y precisa** (Tono 1 de la prueba de 4). Terminal técnico, controlado, cero adorno. La tipografía *es* la personalidad; el color y el 3D acompañan.

## 3. Color — sistema de dos grounds
Hilo constante en ambos: **tinta blanca + acento ámbar `#FF8A2B`**.

| Rol | Token | Hex | Uso |
|---|---|---|---|
| Ground hitos | `--cobalt` | `#1466E0` | Portada · divisores de acto · cierre |
| Cobalto profundo | `--cobalt-deep` | `#0E4FB5` | Sombra/hover sobre cobalto |
| Ground técnico | `--navy` | `#0A0F14` | Slides densas: datos, wireframe, planimetría |
| Panel | `--navy-2` | `#0E151C` | Cards sobre navy |
| Tinta | `--white` | `#FFFFFF` | Texto y ASCII sobre cobalto |
| Wireframe | `--wire` | `#E9F1FA` | Líneas (hielo) sobre navy |
| Acento | `--accent` | `#FF8A2B` | Kickers, dato flotante, leaders (ambos grounds) |
| Acento sombra | `--accent-deep` | `#E06A00` | Hover/estados del acento |
| Sec. navy | `--dim-navy` | `#7D8D99` | Texto secundario sobre navy |
| Sec. cobalto | `--dim-cobalt` | `#D6E6FB` | Texto secundario sobre cobalto |

**Regla narrativa (no solo estética):** el cobalto **abre y cierra cada acto**; el navy es donde se trabaja. La alternancia marca la estructura, no decora.

## 4. Tipografía
- **Display** (`--font-display`, Arial Narrow / condensada): títulos en **MAYÚSCULAS**, peso 700, `line-height` 1.02.
- **Body** (`--font-body`, sans humanista): párrafos, máx. ~46ch.
- **Mono** (`--font-mono`, Consolas): **todo lo técnico** — kickers, datos, HUD, contadores, etiquetas de criterio.
- Escala: hero `clamp(40–92px)` · h2 `clamp(26–44px)` · body 14.5px · datos 11.5px · kicker 11px.
- *Pendiente producción:* incrustar fuentes reales caracterizadas (una grotesca condensada + una mono con carácter) vía `@font-face` para la entrega; las de sistema son el placeholder.

## 5. Composición — retícula de 12 columnas
- La composición **varía por slide** (a veces 3D protagonista, a veces texto, a veces split) **pero todo se alinea a la grilla de 12 columnas**. Esto da ritmo sin verse improvisado.
- Márgenes laterales `--margin-x: 7vw`. Panel de texto máx. ~52% del ancho — **el 3D nunca ocupa toda la pantalla** (feedback clave del usuario).
- Anclas fijas heredadas del HUD: código PAC7.0-WSEF, contador `NN/10`, capítulo, criterio del jurado.

## 6. Las dos técnicas 3D (decidido)
- **ASCII de caracteres** → vive en el **ground cobalto** (portada, divisores, cierre). Es el gancho memorable, interactivo en la intro (rotable + "expresar en datos"). Contenido en su zona, no a pantalla completa.
- **Wireframe de líneas** → vive en el **ground navy** (montaje, planta, envolvente, planimetría), donde la **precisión geométrica** importa y los caracteres no leerían bien.
- Cada técnica refuerza su ground: nunca compiten en la misma slide.

## 7. Densidad de datos (decidido) — varía según el criterio
- **Slides técnicas** (Diseño pasivo/térmica, Estrategia MMC, Innovación): **racimo de 3-5 datos** anclados, estilo telemetría — transmiten rigor y respaldo.
- **Slides narrativas** (El problema, Aporte al entorno, Habitabilidad): **casi sin datos** (0-1), aire y foco en la imagen/idea.
- La densidad sigue el **peso técnico de cada criterio del jurado**. Regla: si el criterio se gana con números, carga datos; si se gana con relato, quita datos.

## 8. Primitivos (en theme.css)
`.ground-cobalt` / `.ground-navy` (setean bg + tokens de tinta) · `.kicker` · `.title` · `.body` · `.chip` (dato flotante) · `.tag` (criterio del jurado) · `.data-dot` (punto con glow del leader).

## 9. Reglas no negociables
- Anonimato: solo **PAC7.0-WSEF**. Cero nombres/instituciones.
- Diálogo con TOP 3 6.0 (revisar antes de producción final).
- Renders IA con trazabilidad (par maqueta/IA + prompt).
- Nunca 3D a pantalla completa tapando el contenido.

## 10. Riesgos / pendientes
- Validar el sistema contra `TOP 3 6.0` (aún no revisado) — puede exigir ajustar la carga tipográfica.
- Incrustar tipografías reales (hoy placeholder de sistema).
- El bug del visor ASCII fullscreen queda **obsoleto**: se reconstruye contenido en su zona bajo estas reglas.
- Confirmar formato de recepción del HTML con la organización.

## 11. Siguiente acción
Re-skinear el deck completo (`index.html`) con `theme.css`: aplicar grounds por slide según §3/§6, densidad de datos según §7, y rehacer la intro con el ASCII **contenido** (no fullscreen). Construcción de una sola pasada.
