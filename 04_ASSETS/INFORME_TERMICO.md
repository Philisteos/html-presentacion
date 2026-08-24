# Desempeño térmico · PAC7.0-WSEF

**Posta rural · Frutillar · Zona térmica G · Uso salud (Tabla 10, D.S. 15/2024 — RT vigente 28-nov-2025)**
Cálculo NCh 853 verificado por 3 motores independientes con coincidencia a 3 decimales. Todas las series de este documento están listas para graficar.

---

## 1. Veredicto de cumplimiento (gráfico: barras U vs límite, semáforo)

| Elemento | U calc. (W/m²K) | U máx zona G | Margen | Semáforo | Cumple |
|---|---:|---:|---:|:-:|:-:|
| Muro módulo 15 cm | 0,376 | 0,40 | +6% | 🟡 justo | ✅ |
| Losa ventilada | 0,359 | 0,39 | +8% | 🟡 justo | ✅ |
| Cubierta módulo | 0,234 | 0,28 | +16% | 🟢 óptimo | ✅ |
| Piel translúcida (como ventana, fachada) | 1,50 | 3,00 | +50% | 🟢 | ✅ |
| Piel translúcida (faldón ≤60°, techumbre) | 1,50 | 3,60 | +58% | 🟢 | ✅ |
| Puertas opacas (exigencia) | — | 1,70 | por especificar | ⚪ | pend. |

Umbrales del semáforo: 🔴 no cumple · 🟡 margen <10% · 🟢 10–50% · 🔵 >50% (sobredimensionado).
El cumplimiento se logra **sin bonificación por la galería**: el muro que da a ella se evalúa como exterior (la OGUC no bonifica espacios no acondicionados).

## 2. Escantillones capa a capa (gráfico: cortes constructivos acotados)

### Muro módulo — U 0,376 · Rt 2,66 (Rsi+Rse 0,17)
| # | Capa | e (mm) | λ (W/mK) | R (m²K/W) |
|---|---|---:|---:|---:|
| 1 | Acabado Sto | 2,5 | 0,70 | 0,004 |
| 2 | EIFS EPS | 60 | 0,038 | 1,579 |
| 3 | Placa soporte | 12,5 | 0,25 | 0,050 |
| 4 | Metalcon + lana mineral (λ eq. c/perfil) | 60 | 0,075 | 0,800 |
| 5 | Yeso cartón | 15 | 0,25 | 0,060 |

### Losa ventilada — U 0,359 · Rt 2,78 (Rsi+Rse 0,22)
| # | Capa | e (mm) | λ | R |
|---|---|---:|---:|---:|
| 1 | Piso terminación | 15 | 0,18 | 0,083 |
| 2 | OSB | 18 | 0,13 | 0,138 |
| 3 | Lana mineral | 117 | 0,05 | 2,340 |

### Cubierta módulo — U 0,234 · Rt 4,26 (Rsi+Rse 0,14)
| # | Capa | e (mm) | λ | R |
|---|---|---:|---:|---:|
| 1 | Membrana impermeable | 5 | 0,23 | 0,022 |
| 2 | EIFS EPS | 50 | 0,038 | 1,316 |
| 3 | Lana mineral | 150 | 0,055 | 2,727 |
| 4 | Yeso cartón | 15 | 0,25 | 0,060 |

### Piel translúcida — policarbonato multipared 6 paredes, ancho útil 600 mm
Ug panel **1,50** · Up sistema (junta + fijaciones) **1,60** · factor solar Sw **0,46** (cristal, EN 16153) · TL 0,62.

## 3. Geometría de la envolvente (gráfico: despiece por orientación / anillo)

| Superficie | m² | Orientación / inclinación |
|---|---:|---|
| Piel — faldón | 414,5 | 26° desde horizontal |
| Piel — oriente | 238,0 | ~57° |
| Piel — poniente | 184,7 | ~58° |
| Piel — norte | 111,9 | ~50–55° |
| Piel — sur | 29,1 | vertical |
| **Piel total** | **978,2** | — |
| — de ella, paños abatibles | 94,8 | N 24,5 · O 43,3 · P 27,0 |
| Muro módulo → galería (36 muros) | 565,2 | protegido |
| Muro módulo mixto (→ evaluado exterior) | 106,1 | conservador |
| Muro módulo exterior directo | 125,7 | expuesto |
| Cubierta módulo bajo piel (pleno) | 157,9 | protegida |
| Huella galería / volumen | 408,9 / ≈1.480 m³ | — |

**El 71% del muro de módulo trabaja contra la galería, no contra el exterior.**

## 4. Clima y radiación (gráfico: líneas mensuales, 12 puntos ene→dic)

Temperatura media mensual (DMC El Tepual, Normal 1991-2020):
```
Te (°C):    14.3 | 14.1 | 12.6 | 10.4 | 8.9 | 7.1 | 6.4 | 7.1 | 8.1 | 9.6 | 11.3 | 13.1
```
Irradiación media diaria por plano (kWh/m²·día — Explorador Solar + derivación declarada):
```
GHI:        6.92 | 5.67 | 3.9 | 2.28 | 1.43 | 1.1 | 1.19 | 1.78 | 3.08 | 4.11 | 5.38 | 6.45
Faldón 26°: 6.46 | 5.65 | 4.28 | 2.82 | 2.01 | 1.69 | 1.71 | 2.29 | 3.5 | 4.15 | 5.06 | 5.92
Norte 50°:  5.75 | 5.37 | 4.45 | 3.18 | 2.45 | 2.14 | 2.1 | 2.65 | 3.74 | 4.04 | 4.57 | 5.17
Oriente:    5.56 | 4.58 | 3.18 | 1.81 | 1.1 | 0.89 | 0.88 | 1.38 | 2.46 | 3.29 | 4.36 | 5.2
Poniente:   5.95 | 4.82 | 3.27 | 1.82 | 1.09 | 0.89 | 0.88 | 1.39 | 2.46 | 3.39 | 4.58 | 5.57
```
T. diseño invierno (percentil 99): **−0,8 °C** · nubosidad diurna invierno ~68% — el sistema funciona con radiación mayormente **difusa**.

## 5. La galería mes a mes (gráfico principal: Te vs Tg con banda de horquilla)

Balance estacionario mensual: Tg = (H_iu·Ti + H_ue·Te + Q_sol)/(H_iu+H_ue) · H_iu 242 W/K · H_ue 2.090 W/K · Ti 21 °C.
Régimen **cerrado** may–ago (compuertas cerradas); resto **regulado** (abatibles modulan, Tg operativa ≤22 °C).

| Mes | Régimen | Te | Tg pesim. | Tg central | Tg optim. | Tg operativa |
|---|---|---:|---:|---:|---:|---:|
| ene | regulado | 14.3 | 42.0 | 51.9 | 74.6 | 14.3–22 (modulada) |
| feb | regulado | 14.1 | 37.9 | 46.3 | 65.6 | 14.1–22 (modulada) |
| mar | regulado | 12.6 | 30.3 | 36.5 | 50.7 | 12.6–22 (modulada) |
| abr | regulado | 10.4 | 22.0 | 26.0 | 35.0 | 10.4–22 (modulada) |
| may | cerrado | 8.9 | 17.2 | 20.1 | 26.3 | 20.1 |
| jun | cerrado | 7.1 | 14.4 | 16.9 | 22.1 | 16.9 |
| jul | cerrado | 6.4 | 13.7 | 16.3 | 21.5 | 16.3 |
| ago | cerrado | 7.1 | 16.8 | 20.1 | 27.4 | 20.1 |
| sep | regulado | 8.1 | 22.8 | 27.9 | 39.3 | 8.1–22 (modulada) |
| oct | regulado | 9.6 | 27.4 | 33.7 | 47.7 | 9.6–22 (modulada) |
| nov | regulado | 11.3 | 33.4 | 41.2 | 58.9 | 11.3–22 (modulada) |
| dic | regulado | 13.1 | 38.9 | 48.1 | 69.0 | 13.1–22 (modulada) |

Factor de reducción y U efectiva del muro protegido (solo meses cerrados; gráfico: barras U 0,376→U_ef):

| Mes | b_ef pesim. | b_ef central | b_ef optim. | U_ef central (W/m²K) | Pérdida evitada |
|---|---:|---:|---:|---:|---:|
| may | 0.31 | 0.07 | 0.00 | 0.027 | −93% |
| jun | 0.47 | 0.30 | 0.00 | 0.108 | −71% |
| jul | 0.50 | 0.33 | 0.00 | 0.118 | −69% |
| ago | 0.30 | 0.06 | 0.00 | 0.022 | −94% |

**Diseño (noche sin sol, Te −0,8 °C):** galería a +2,3 K · b = 0,90 · U_ef 0,326. El beneficio es estacional-energético; la carga punta nocturna casi no mejora — número honesto para dimensionar calefacción.

## 6. Energía por el muro protegido (gráfico: barras mensuales pareadas)

Pérdida mensual del muro de 565,2 m²: expuesto directo vs con galería, escenario central. En meses **regulados** la galería ventilada se asume a Te (no se reclama beneficio: solo el ajuste Rsi 0,376→0,363); en meses **cerrados** rige el balance solar:

| Mes | Régimen | Sin galería (kWh) | Con galería (kWh) | Ahorro |
|---|---|---:|---:|---:|
| ene | regulado | 1059 | 1023 | −3% |
| feb | regulado | 994 | 960 | −3% |
| mar | regulado | 1328 | 1282 | −3% |
| abr | regulado | 1622 | 1566 | −3% |
| may | cerrado | 1913 | 137 | −93% |
| jun | cerrado | 2127 | 606 | −72% |
| jul | cerrado | 2308 | 717 | −69% |
| ago | cerrado | 2198 | 137 | −94% |
| sep | regulado | 1974 | 1906 | −3% |
| oct | regulado | 1802 | 1740 | −3% |
| nov | regulado | 1484 | 1433 | −3% |
| dic | regulado | 1249 | 1206 | −3% |
| **año** | — | **20058** | **12713** | **−37%** |

## 7. Verano: ventilación por tiro térmico (gráfico: curva ΔT vs m² abatibles)

Enero, día medio, abatibles abiertos (40% de área libre por paño, ΔH 2 m, BS 5925/ASHRAE):

| Paño abatible (m²) | ΔT diurno galería (K) |
|---:|---:|
| 40 | +16.9 |
| 60 | +13.4 |
| 94.8 | +10.2 ← **actual** |
| 150 | +7.7 |
| 200 | +6.4 |
| 300 | +4.9 ← objetivo ΔT≤5 |
| 400 | +4.1 |
| 600 | +3.2 |

Con los 94,8 m² actuales: 25 ren/h y aun así **+10 K** (~30 °C con Tmáx 20). El faldón de 26° capta el **46%** de la ganancia estival: una banda opal/serigrafiada ahí (o subir a ~300 m² abatibles) lleva el sobrecalentamiento a +5 K. Acabado Opal (Sw 0,30) lo baja a ~+7 K a costa de ⅓ de la ganancia invernal.

## 8. Síntesis para la lámina

1. **Cumple la RT 2025 sin ayuda de la galería** — muro 0,376/0,40 · losa 0,359/0,39 · cubierta 0,234/0,28.
2. **La galería es la máquina de invierno**: julio a 16,3 °C de media con 6,4 °C fuera; la pérdida del 71% del muro cae −69% (horquilla −52% a −100%).
3. **Funciona nublado**: el clima de Frutillar es 68% difuso y el balance ya lo descuenta.
4. **Honestidad de carga punta**: de noche b=0,90 — la galería ahorra energía de temporada, no potencia instalada.
5. **El verano está dimensionado, no ignorado**: +10 K hoy → estrategia cuantificada (control solar del faldón / +abatibles).

---
*Método: balance estacionario mensual (EN 12831 An. D + término solar) · NCh 853 · datos DMC / Explorador Solar / DTA CSTB con nivel de confianza declarado. Memoria completa: MEMORIA_GALERIA_TERMICA.md. Limitaciones: sin inercia ni estratificación; volumen ±15%; series 50° E/P derivadas; condensación RT 2025 pendiente.*