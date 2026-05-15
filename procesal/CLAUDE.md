<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /procesal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /procesal:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/procesal/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Procesal

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/procesal:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad / despacho]. El equipo de litigación/procesal lo forman [N] personas. [Nombre del socio/a responsable] es el punto final de escalado. Llevamos aproximadamente [N] asuntos activos en [N] jurisdicciones.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Procurador]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a colegiado/a | Procurador/a | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Jurisdicciones activas

| Jurisdicción | Volumen | Tipos habituales | Despacho externo (si aplica) |
|---|---|---|---|
| Civil | [PLACEHOLDER — alto/medio/bajo/inactivo] | [PLACEHOLDER] | [PLACEHOLDER] |
| Mercantil | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Penal | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Contencioso-administrativo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Social (laboral) | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Partidos judiciales habituales:** [PLACEHOLDER — ej., "Madrid, Barcelona, Valencia, Bilbao"]

**Plataformas telemáticas:**
- LexNET: [PLACEHOLDER ✓/✗ — obligatorio para comunicaciones con la Administración de Justicia]
- Plataforma autonómica: [PLACEHOLDER — ej., "e-Justicia (País Vasco), Justicia Digital (Cataluña)"]

---

## Tipos de procedimiento habituales

### Jurisdicción civil

| Procedimiento | Cuantía/Criterio | Referencia LEC | Uso habitual |
|---|---|---|---|
| Juicio ordinario | >6.000€ o sin cuantía determinada | Arts. 399-436 LEC | [PLACEHOLDER] |
| Juicio verbal | ≤6.000€ o materias especiales (art. 250 LEC) | Arts. 437-447 LEC | [PLACEHOLDER] |
| Monitorio | Reclamación de deuda dineraria líquida | Arts. 812-818 LEC | [PLACEHOLDER] |
| Cambiario | Letra, cheque, pagaré | Arts. 819-827 LEC | [PLACEHOLDER] |
| Ejecución de títulos judiciales | Sentencia firme | Arts. 517-570 LEC | [PLACEHOLDER] |
| Ejecución de títulos no judiciales | Escritura pública, póliza intervenida | Arts. 517-570 LEC | [PLACEHOLDER] |
| Medidas cautelares | Periculum in mora + fumus boni iuris | Arts. 721-747 LEC | [PLACEHOLDER] |
| Procedimiento de jura de cuentas | Honorarios de abogados/procuradores | Arts. 34-35 LEC | [PLACEHOLDER] |

### Jurisdicción mercantil

| Procedimiento | Referencia | Uso habitual |
|---|---|---|
| Impugnación de acuerdos sociales | Art. 204 LSC + LEC | [PLACEHOLDER] |
| Acciones de responsabilidad de administradores | Arts. 236-241 LSC | [PLACEHOLDER] |
| Competencia desleal | Ley 3/1991 + LEC | [PLACEHOLDER] |
| Propiedad industrial / intelectual | Leyes sectoriales + LEC | [PLACEHOLDER] |
| [PLACEHOLDER — otros procedimientos habituales] | | |

### Jurisdicción contencioso-administrativa

| Procedimiento | Referencia LJCA | Uso habitual |
|---|---|---|
| Procedimiento ordinario | Arts. 45-77 LJCA | [PLACEHOLDER] |
| Procedimiento abreviado | Art. 78 LJCA | [PLACEHOLDER] |
| Recurso de casación | Arts. 86-93 LJCA | [PLACEHOLDER] |
| Medidas cautelares | Arts. 129-136 LJCA | [PLACEHOLDER] |

### Jurisdicción social

| Procedimiento | Referencia LRJS | Uso habitual |
|---|---|---|
| Proceso ordinario | Arts. 76-101 LRJS | [PLACEHOLDER] |
| Despido | Arts. 103-113 LRJS | [PLACEHOLDER] |
| Conflicto colectivo | Arts. 153-162 LRJS | [PLACEHOLDER] |
| Recurso de suplicación | Arts. 190-204 LRJS | [PLACEHOLDER] |

---

## Plazos procesales — Reglas de cómputo

**Regla general (art. 130-136 LEC):**
- Días hábiles: lunes a viernes (excluidos sábados, domingos y festivos nacionales/autonómicos/locales)
- Agosto: inhábil para actuaciones judiciales (art. 183.1 LOPJ), SALVO las excepciones del art. 183.2-4 LOPJ (medidas cautelares urgentes, procedimientos preferentes y sumarios de DDFF, alimentos, internamientos, menores)
- Hora límite LexNET: 15:00h del último día del plazo; si se presenta entre 15:01h y 23:59h, se entiende presentado el primer día hábil siguiente

**Plazos críticos:**
| Acto procesal | Plazo | Norma | Notas |
|---|---|---|---|
| Contestación a la demanda (ordinario) | 20 días hábiles | Art. 404 LEC | Desde notificación |
| Contestación a la demanda (verbal) | 10 días hábiles | Art. 438 LEC | Desde notificación |
| Recurso de apelación — preparación | - | Art. 457 LEC | Integrado en interposición |
| Recurso de apelación — interposición | 20 días hábiles | Art. 458 LEC | Desde notificación de resolución |
| Recurso de casación | 20 días hábiles | Art. 479 LEC | Desde notificación |
| Recurso extraordinario por infracción procesal | 20 días hábiles | Art. 470 LEC | Desde notificación |
| Oposición a monitorio | 20 días hábiles | Art. 815 LEC | Desde requerimiento |
| Recurso contencioso-administrativo | 2 meses (acto expreso) / 6 meses (silencio) | Art. 46 LJCA | Desde notificación/publicación |
| Demanda por despido (social) | 20 días hábiles | Art. 103 LRJS | Desde despido efectivo |
| [PLACEHOLDER — plazos adicionales relevantes] | | | |

**Sistema de alertas de plazos:** [PLACEHOLDER — ej., "Calendario compartido con alertas 5 días antes del vencimiento; doble verificación por procurador y letrado"]

---

## Matriz de severidad de asuntos

| Severidad | Criterio | Ejemplo | Responsable mínimo |
|---|---|---|---|
| 🔴 Crítico | [PLACEHOLDER — ej., "Cuantía >€1M, riesgo reputacional, medidas cautelares contra nosotros, procedimiento penal contra directivos"] | [PLACEHOLDER] | [Socio/a director/a] |
| 🟠 Alto | [PLACEHOLDER — ej., "Cuantía €200K-€1M, asuntos con publicidad, recursos de casación"] | [PLACEHOLDER] | [Socio/a responsable] |
| 🟡 Medio | [PLACEHOLDER — ej., "Cuantía €50K-€200K, procedimientos ordinarios"] | [PLACEHOLDER] | [Abogado/a senior] |
| 🟢 Bajo | [PLACEHOLDER — ej., "Cuantía <€50K, monitorios, verbales rutinarios, ejecuciones sin oposición"] | [PLACEHOLDER] | [Abogado/a junior] |

---

## Estilo house de escritos

### Estructura de escritos procesales

**Encabezamiento:** [PLACEHOLDER — ej., "AL JUZGADO DE [jurisdicción] N.º [X] DE [ciudad] / Procedimiento [tipo] n.º [XXX/AAAA]"]

**Cuerpo:**
1. Hechos (numerados)
2. Fundamentos de derecho (numerados, con subdivisiones si es necesario)
3. Suplico / Petitum (en mayúsculas, con peticiones numeradas)

**Otrosí:** [PLACEHOLDER — ej., "Usar para cuestiones procesales accesorias; numerar si hay varios"]

### Citas de jurisprudencia

**Formato ECLI obligatorio:** [PLACEHOLDER — ej., "STS de 15 de marzo de 2024 (ECLI:ES:TS:2024:XXXX)"]

**Bases de datos utilizadas:**
- [PLACEHOLDER — ej., "CENDOJ (buscador de jurisprudencia del CGPJ) — acceso gratuito"]
- [PLACEHOLDER — ej., "Westlaw / Aranzadi / La Ley Digital — suscripción del despacho"]
- [PLACEHOLDER — ej., "vLex — suscripción del despacho"]

**Criterios de selección de jurisprudencia:**
- [PLACEHOLDER — ej., "Priorizar STS sobre SAP; citar jurisprudencia reciente (<5 años salvo doctrina consolidada); incluir siempre ECLI"]

### Referencias normativas

**Formato:** [PLACEHOLDER — ej., "art. 394.1 LEC, art. 1101 CC, art. 24 CE"]

---

## Despachos externos — Gestión de relación

| Despacho | Especialidad | Jurisdicción | Contacto | Condiciones |
|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "Fee cap €X, reporting mensual"] |

**Reporting exigido:** [PLACEHOLDER — ej., "Informe mensual de estado con: actuaciones del período, próximos hitos, estimación de costes, valoración de riesgo"]

**Aprobación de costes:** [PLACEHOLDER — ej., "Provisiones >€X requieren aprobación previa; minutas revisadas trimestralmente"]

---

## Medidas cautelares

**Posición como solicitante:**
- [PLACEHOLDER — ej., "Solicitar siempre que haya riesgo real de insolvencia o de frustración del fallo; ofrecer caución proporcional"]

**Posición como demandado:**
- [PLACEHOLDER — ej., "Oponerse siempre; solicitar caución sustitutoria; recurrir si se adoptan"]

**Tipos habituales solicitados/recibidos:**
- [PLACEHOLDER — ej., "Embargo preventivo, anotación preventiva de demanda, cesación de actos de competencia desleal, medidas de aseguramiento de prueba"]

---

## Costas procesales

**Criterio legal:** Vencimiento objetivo (art. 394 LEC civil); temeridad o mala fe (art. 97.3 LRJS social)

**Posición house:** [PLACEHOLDER — ej., "Solicitar siempre costas al contrario; impugnar tasación si >20% sobre minutas de referencia del ICAM"]

**Baremos de referencia:** [PLACEHOLDER — ej., "Criterios orientadores del Colegio de Abogados de [ciudad]; Decreto autonómico de aranceles de procuradores"]

**Límite de responsabilidad por costas (art. 394.3 LEC):** [PLACEHOLDER — ej., "1/3 de la cuantía del proceso para la parte perdedora"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Abogado/a junior] | [PLACEHOLDER — ej., "Monitorios, verbales <€6K, ejecuciones sin oposición"] | [Abogado/a senior] | [método] |
| [Abogado/a senior] | [PLACEHOLDER — ej., "Ordinarios, apelaciones, contencioso-administrativo"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Todo lo que no sea casación o asunto 🔴"] | [Socio/a director/a / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Todo procedimiento penal, toda medida cautelar recibida, todo recurso ante TS/TC, todo asunto con publicidad en medios"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **LEC** — Ley de Enjuiciamiento Civil (Ley 1/2000, de 7 de enero)
- **LECrim** — Ley de Enjuiciamiento Criminal (Real Decreto de 14 de septiembre de 1882, reformas sucesivas)
- **LJCA** — Ley de la Jurisdicción Contencioso-Administrativa (Ley 29/1998, de 13 de julio)
- **LRJS** — Ley Reguladora de la Jurisdicción Social (Ley 36/2011, de 10 de octubre)
- **LOPJ** — Ley Orgánica del Poder Judicial (LO 6/1985, de 1 de julio)
- **Ley de Asistencia Jurídica Gratuita** (Ley 1/1996, de 10 de enero)
- **Ley de Mediación** (Ley 5/2012, de 6 de julio)
- **Ley de Arbitraje** (Ley 60/2003, de 23 de diciembre)

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/procesal:entrevista-inicial --repetir`*
