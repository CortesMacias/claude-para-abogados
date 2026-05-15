<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /fiscal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /fiscal:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/fiscal/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Fiscal y Tributario
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/fiscal:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de fiscalidad se quedan aquí.*

[Empresa] es una [tipo de entidad]. Forma jurídica: [PLACEHOLDER — SA, SL, SLP, cooperativa, autónomo, etc.].
Régimen fiscal: [PLACEHOLDER — régimen general IS / régimen especial / consolidación fiscal / etc.].
Ejercicio fiscal: [PLACEHOLDER — año natural / ejercicio partido]. NIF: [PLACEHOLDER].
Delegación de Hacienda: [PLACEHOLDER]. El equipo fiscal cuenta con [N] personas.
[Responsable fiscal: nombre o ninguno]. Asesor fiscal externo: [PLACEHOLDER]. La escalación va a [nombre].

**Huella fiscal:** [PLACEHOLDER — tributos principales a los que está sujeta la entidad] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos fiscales abiertos:** [PLACEHOLDER — inspecciones en curso, reclamaciones, consultas vinculantes pendientes]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica/fiscal interna | Asesoría fiscal independiente] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a fiscalista | Asesor fiscal | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Software contable (A3, Sage, SAP, etc.) | [PLACEHOLDER ✓/✗] | Datos fiscales introducidos manualmente |
| Sede electrónica AEAT | [PLACEHOLDER ✓/✗] | Consulta manual de plazos y modelos |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de calendario fiscal solo bajo demanda |

*Re-comprobar: `/fiscal:entrevista-inicial --check-integraciones`*

---

## Forma jurídica y régimen fiscal

| Campo | Valor |
|---|---|
| Forma jurídica | [PLACEHOLDER — SA / SL / SLP / CB / autónomo / etc.] |
| Régimen del Impuesto sobre Sociedades | [PLACEHOLDER — general / ERD / consolidación / SOCIMI / etc.] |
| Régimen de IVA | [PLACEHOLDER — general / simplificado / recargo de equivalencia / RECC / exento / prorrata] |
| Grupo de consolidación fiscal | [PLACEHOLDER — sí/no, número de grupo] |
| Grupo de IVA | [PLACEHOLDER — sí/no] |
| Obligación TicketBAI / SII | [PLACEHOLDER — sí/no] |
| Operador intracomunitario (ROI) | [PLACEHOLDER — sí/no, NIF-IVA] |

---

## Obligaciones tributarias principales

| Impuesto | Modelo | Periodicidad | Plazo | Notas |
|---|---|---|---|---|
| IS — Impuesto sobre Sociedades | 200 | Anual (25 días tras 6 meses fin ejercicio) | [PLACEHOLDER] | [PLACEHOLDER] |
| IS — Pagos fraccionados | 202 | Trimestral (abril, octubre, diciembre) | [PLACEHOLDER] | [PLACEHOLDER — modalidad art. 40.2 o 40.3 LIS] |
| IVA — Autoliquidación | 303 | Trimestral / mensual (SII) | [PLACEHOLDER] | [PLACEHOLDER] |
| IVA — Resumen anual | 390 | Anual (enero) | [PLACEHOLDER] | [PLACEHOLDER] |
| IRPF — Retenciones trabajo | 111 | Trimestral / mensual | [PLACEHOLDER] | [PLACEHOLDER] |
| IRPF — Retenciones capital | 123 | Trimestral / mensual | [PLACEHOLDER] | [PLACEHOLDER] |
| IRPF — Resumen anual | 190 | Anual (enero) | [PLACEHOLDER] | [PLACEHOLDER] |
| IAE | 840/848 | Anual | [PLACEHOLDER] | [PLACEHOLDER — exento si cifra negocios < 1M€] |
| Operaciones intracomunitarias | 349 | Mensual / trimestral | [PLACEHOLDER] | [PLACEHOLDER] |
| Operaciones con terceros | 347 | Anual (febrero) | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro modelo] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Calendario fiscal AEAT — Plazos clave

| Trimestre | Modelos principales | Plazo presentación |
|---|---|---|
| 1T (enero-marzo) | 303, 111, 115, 123, 202 | 1-20 abril |
| 2T (abril-junio) | 303, 111, 115, 123, 200, 202 | 1-20 julio (200 hasta 25 julio) |
| 3T (julio-septiembre) | 303, 111, 115, 123 | 1-20 octubre |
| 4T (octubre-diciembre) | 303, 111, 115, 123, 202, 390, 190, 180 | 1-20/30 enero |

**Plazos especiales:** [PLACEHOLDER — grandes empresas, SII, grupos de consolidación]

---

## Impuestos autonómicos y locales

| Impuesto | CCAA / Municipio | Tipo | Notas |
|---|---|---|---|
| ITP y AJD | [PLACEHOLDER — CCAA] | [PLACEHOLDER — tipo aplicable] | [PLACEHOLDER] |
| Plusvalía municipal (IIVTNU) | [PLACEHOLDER — municipio] | [PLACEHOLDER] | [PLACEHOLDER — método de cálculo] |
| IBI | [PLACEHOLDER — municipio] | [PLACEHOLDER] | [PLACEHOLDER] |
| Impuesto sobre sucesiones y donaciones | [PLACEHOLDER — CCAA] | [PLACEHOLDER] | [PLACEHOLDER — bonificaciones autonómicas] |
| [Otro impuesto autonómico/local] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Consultas vinculantes DGT

| Referencia | Fecha | Materia | Criterio relevante | Aplicable |
|---|---|---|---|---|
| [PLACEHOLDER — p.ej. V0001-23] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER ✓/✗] |

**Política de consultas vinculantes:** [PLACEHOLDER — cuándo elevamos consulta a la DGT, proceso interno]

---

## Procedimientos tributarios

| Procedimiento | Normativa | Plazos clave | Estado actual |
|---|---|---|---|
| Gestión tributaria | Arts. 117-140 LGT | Verificación: 6 meses; comprobación limitada: 6 meses | [PLACEHOLDER] |
| Inspección tributaria | Arts. 141-159 LGT | 18 meses (ampliable a 27) | [PLACEHOLDER] |
| Sancionador tributario | Arts. 207-212 LGT | 6 meses | [PLACEHOLDER] |
| Reclamación económico-administrativa (TEA) | Arts. 226-248 LGT | 1 año (TEAC) / 6 meses (TEAR) | [PLACEHOLDER] |
| Recurso contencioso-administrativo | LJCA 29/1998 | 2 meses desde resolución | [PLACEHOLDER] |

---

## Planificación fiscal

| Elemento | Descripción | Estado |
|---|---|---|
| Operaciones vinculadas (art. 18 LIS) | [PLACEHOLDER — política de precios de transferencia, documentación] | [PLACEHOLDER] |
| Deducciones I+D+i (art. 35 LIS) | [PLACEHOLDER — proyectos, informes motivados MINECO] | [PLACEHOLDER] |
| Patent box (art. 23 LIS) | [PLACEHOLDER — cesión de intangibles, reducción aplicada] | [PLACEHOLDER] |
| Reserva de capitalización (art. 25 LIS) | [PLACEHOLDER] | [PLACEHOLDER] |
| Reserva de nivelación ERD (art. 105 LIS) | [PLACEHOLDER] | [PLACEHOLDER] |
| Compensación de BINs | [PLACEHOLDER — bases imponibles negativas pendientes] | [PLACEHOLDER] |
| [Otro elemento de planificación] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Convenios de doble imposición

| País | CDI vigente | Aspectos clave | Operaciones afectadas |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER — sí/no, referencia BOE] | [PLACEHOLDER — retenciones, EP, cánones] | [PLACEHOLDER] |

---

## Estilo house — Memos fiscales

**Estructura estándar de memo fiscal:**
1. [PLACEHOLDER — p.ej. Antecedentes de hecho]
2. [PLACEHOLDER — p.ej. Cuestión planteada]
3. [PLACEHOLDER — p.ej. Normativa aplicable]
4. [PLACEHOLDER — p.ej. Análisis]
5. [PLACEHOLDER — p.ej. Conclusión y recomendación]

**Tono:** [PLACEHOLDER — técnico / divulgativo / mixto]
**Extensión típica:** [PLACEHOLDER — páginas]
**Destinatario habitual:** [PLACEHOLDER — dirección financiera / cliente / archivo]

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Autoliquidación rutinaria | Equipo fiscal | — | — |
| Consulta vinculante DGT | Equipo fiscal | Socio/Director fiscal | Siempre |
| Requerimiento de información AEAT | Equipo fiscal | Dirección jurídica | Si implica posible inspección |
| Inicio de inspección | — | Dirección jurídica + Dirección General | Siempre |
| Acta de inspección (conformidad/disconformidad) | — | Socio fiscal + Dirección | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Dirección | Siempre |

---

## Referencias legislativas principales

- **LGT** — Ley 58/2003, de 17 de diciembre, General Tributaria
- **LIRPF** — Ley 35/2006, de 28 de noviembre, del Impuesto sobre la Renta de las Personas Físicas
- **LIS** — Ley 27/2014, de 27 de noviembre, del Impuesto sobre Sociedades
- **LIVA** — Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido
- **LITPAJD** — Real Decreto Legislativo 1/1993, del Impuesto sobre Transmisiones Patrimoniales y AJD
- **RIRPF, RIS, RIVA** — Reglamentos de desarrollo respectivos
- **LGP** — Ley 47/2003, General Presupuestaria
- **Normativa autonómica** — según CCAA relevantes para ITP, ISD y tributos propios

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Última declaración IS (Modelo 200) | [PLACEHOLDER] | [PLACEHOLDER] | |
| Calendario fiscal vigente | [PLACEHOLDER] | [PLACEHOLDER] | |
| Memo fiscal de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan memos fiscales, análisis y calendarios]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a fiscalista: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/fiscal:entrevista-inicial --redo`*
