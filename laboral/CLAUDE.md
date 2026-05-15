<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /laboral:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /laboral:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/laboral/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Laboral

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/laboral:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de derecho laboral lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos aproximadamente [N] consultas/expedientes laborales al mes.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna / RRHH | Graduado social]

**Tamaño de plantilla (si asesoría interna):** [PLACEHOLDER — ej., "<50 / 50-250 / >250 trabajadores"]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a laboralista colegiado/a | Graduado/a social | RRHH con acceso a letrado | RRHH sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Convenio colectivo aplicable

**Convenio:** [PLACEHOLDER — ej., "Convenio colectivo estatal de consultoría y estudios de mercado (Resolución de XX/XX/XXXX, BOE)"]
**Código convenio:** [PLACEHOLDER]
**Vigencia:** [PLACEHOLDER — ej., "2023-2025, prorrogado tácitamente"]
**Ultraactividad:** [PLACEHOLDER — ej., "Convenio de ámbito superior aplicable tras la ultraactividad: sectorial estatal"]

**Convenios adicionales si hay centros en varias CCAA:**
- [PLACEHOLDER]

**Posición ante vacío de convenio:** [PLACEHOLDER — ej., "Aplicar condiciones más favorables del convenio vencido; escalar a letrado si hay duda"]

---

## Tipos de contrato — Referencia y posición

| Tipo de contrato | Referencia legal | Uso habitual | Posición house |
|---|---|---|---|
| Indefinido ordinario | Art. 15.1 ET | [PLACEHOLDER] | [PLACEHOLDER — ej., "Tipo por defecto desde reforma 2022"] |
| Indefinido fijo-discontinuo | Art. 16 ET | [PLACEHOLDER] | [PLACEHOLDER — ej., "Para trabajos de naturaleza estacional o vinculados a contratas"] |
| Temporal por circunstancias de la producción | Art. 15.2 ET | [PLACEHOLDER — ej., "Máx. 6 meses ampliable a 12 por convenio; o 90 días no continuados en año natural"] | [PLACEHOLDER] |
| Formación en alternancia | Art. 11.2 ET | [PLACEHOLDER] | [PLACEHOLDER] |
| Formación para obtención de práctica profesional | Art. 11.3 ET | [PLACEHOLDER] | [PLACEHOLDER] |

**Modelos house de contrato:** [PLACEHOLDER — ej., "Repositorio en Drive/carpeta X; usar siempre modelo house, no modelo SEPE genérico"]

**Cláusulas adicionales habituales en contratos:**
- [PLACEHOLDER — ej., "Período de prueba, dedicación exclusiva, teletrabajo, protección de datos del empleado"]

---

## Despido — Tipos y requisitos

### Despido objetivo (art. 52 ET)

**Causas:** Ineptitud sobrevenida, falta de adaptación, causas ETOP (económicas, técnicas, organizativas, productivas — individuales o colectivas <umbrales art. 51)

**Requisitos formales:**
- Carta de despido con causa concreta y fecha de efectos
- Preaviso de 15 días (o abono en su lugar)
- Puesta a disposición simultánea de la indemnización: 20 días por año trabajado, máximo 12 mensualidades
- [PLACEHOLDER — requisitos adicionales del convenio aplicable]

**Posición house:** [PLACEHOLDER — ej., "Siempre revisar carta con letrado antes de entregar; documentar la causa con evidencia objetiva"]

### Despido disciplinario (art. 54 ET)

**Causas:** Faltas repetidas de asistencia, indisciplina, ofensas verbales/físicas, transgresión de buena fe, disminución continuada del rendimiento, embriaguez/toxicomanía, acoso

**Requisitos formales:**
- Carta de despido con hechos concretos, fechas y causa legal
- Sin preaviso ni indemnización
- Expediente contradictorio si hay representantes de los trabajadores o delegados sindicales
- [PLACEHOLDER — requisitos del convenio: sanciones previas, graduación de faltas]

**Posición house:** [PLACEHOLDER — ej., "Documentar siempre con advertencias previas escritas cuando sea posible; consultar letrado antes de despido disciplinario"]

### Despido colectivo (art. 51 ET)

**Umbrales:**
- 10 trabajadores en empresas de <100
- 10% de la plantilla en empresas de 100-300
- 30 trabajadores en empresas de >300

**Procedimiento:**
- Período de consultas con representantes (30 días, 15 si <50 trabajadores)
- Comunicación a la autoridad laboral
- Informe técnico de causas
- Plan de recolocación si >50 trabajadores

**Posición house:** [PLACEHOLDER — ej., "Siempre con acompañamiento de despacho externo especializado"]

---

## Período de prueba

**Duración máxima legal (art. 14 ET):**
- Técnicos titulados: 6 meses
- Resto de trabajadores: 2 meses (3 meses si empresa <25 trabajadores)
- Contratos temporales ≤6 meses: 1 mes máximo

**Duración según convenio aplicable:** [PLACEHOLDER — ej., "Grupo 1-3: 2 meses; Grupo 4-6: 3 meses; Grupo 7-8: 6 meses"]

**Posición house:** [PLACEHOLDER — ej., "Aplicar siempre el máximo que permita convenio; documentar causa de no superación"]

---

## Cláusulas especiales

### No competencia post-contractual (art. 21.2 ET)

**Posición house:** [PLACEHOLDER — ej., "Incluir en contratos de personal clave; duración máx. 2 años técnicos / 6 meses resto; compensación económica adecuada obligatoria"]

**Compensación económica:** [PLACEHOLDER — ej., "Mínimo 40% del salario anual; pago mensual durante la vigencia del pacto"]

**Interés industrial/comercial:** [PLACEHOLDER — ej., "Documentar siempre el interés empresarial legítimo"]

### Pacto de permanencia (art. 21.4 ET)

**Posición house:** [PLACEHOLDER — ej., "Solo para formaciones con coste >€X; duración máx. 2 años; indemnización de daños y perjuicios proporcional"]

### Cláusula de confidencialidad

**Posición house:** [PLACEHOLDER — ej., "Incluir en todos los contratos; referenciar Ley 1/2019 de Secretos Empresariales"]

### Pacto de dedicación exclusiva / plena dedicación (art. 21.1 ET)

**Posición house:** [PLACEHOLDER — ej., "Solo para puestos de dirección o con acceso a información estratégica; compensación económica expresa"]

---

## Jornada y salario

**SMI vigente:** [PLACEHOLDER — ej., "1.134€/mes en 14 pagas (2024); verificar actualización anual"]

**Jornada máxima legal:** 40 horas semanales en cómputo anual (art. 34 ET)
**Jornada según convenio:** [PLACEHOLDER — ej., "1.764 horas anuales"]

**Registro de jornada:** [PLACEHOLDER — ej., "Sistema electrónico obligatorio (art. 34.9 ET); conservación 4 años"]

**Horas extraordinarias:**
- Máximo 80 al año (art. 35.2 ET)
- Compensación: [PLACEHOLDER — ej., "Preferencia por compensación con descanso dentro de los 4 meses siguientes; abono al 175% si se pagan"]

**Complementos salariales habituales:** [PLACEHOLDER — ej., "Plus convenio, plus transporte, variable por objetivos, retribución flexible"]

**Teletrabajo (Ley 10/2021):**
- Acuerdo individual escrito obligatorio si >30% de la jornada en 3 meses
- Compensación de gastos obligatoria
- [PLACEHOLDER — política house de teletrabajo]

---

## Excedencias y permisos

| Tipo | Duración | Referencia | Posición house |
|---|---|---|---|
| Excedencia voluntaria | 4 meses - 5 años (art. 46.2 ET) | Art. 46.2 ET | [PLACEHOLDER] |
| Excedencia por cuidado de hijos | Hasta 3 años (art. 46.3 ET) | Art. 46.3 ET | [PLACEHOLDER — reserva de puesto 1 año / mismo grupo profesional 2-3 años] |
| Excedencia por cuidado de familiar | Hasta 2 años (art. 46.3 ET) | Art. 46.3 ET | [PLACEHOLDER] |
| Permiso por nacimiento | 16 semanas (art. 48.4 ET) | Art. 48.4 ET | [PLACEHOLDER] |
| Permiso por fallecimiento/hospitalización familiar | 2-4 días según desplazamiento | Art. 37.3 ET | [PLACEHOLDER] |
| Permiso por mudanza | 1 día | Art. 37.3 ET | [PLACEHOLDER] |
| [PLACEHOLDER — permisos adicionales del convenio] | | | |

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [RRHH/paralegal] | [PLACEHOLDER — ej., "Consultas rutinarias, permisos, certificados"] | [Abogado/a laboralista] | [método] |
| [Abogado/a laboralista] | [PLACEHOLDER — ej., "Despidos individuales, sanciones, reclamaciones <€X"] | [Socio/a / responsable] | [método] |
| [Socio/a / responsable] | [PLACEHOLDER — ej., "EREs, ERTE, conflictos colectivos, inspecciones de trabajo"] | [Comité dirección / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Todo despido colectivo, toda demanda ante el Juzgado de lo Social, toda inspección de trabajo, acoso laboral"]

---

## Estilo house

**Formato de cartas de despido:** [PLACEHOLDER — ej., "Modelo house obligatorio; siempre revisar por letrado"]
**Formato de informes laborales:** [PLACEHOLDER — ej., "Encabezado, antecedentes, normativa aplicable, análisis, recomendación"]
**Citas normativas:** [PLACEHOLDER — ej., "art. 54.2.d) ET, art. 110 LRJS, STS de DD/MM/AAAA (ECLI:ES:TS:AAAA:XXXX)"]
**Idioma:** [PLACEHOLDER — ej., "Español; traducciones juradas para trabajadores extranjeros si es necesario"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **ET** — Estatuto de los Trabajadores (Real Decreto Legislativo 2/2015, de 23 de octubre)
- **LISOS** — Ley sobre Infracciones y Sanciones en el Orden Social (Real Decreto Legislativo 5/2000)
- **LRJS** — Ley Reguladora de la Jurisdicción Social (Ley 36/2011, de 10 de octubre)
- **Ley 10/2021** de trabajo a distancia
- **RD 1/1995** y normativa de desarrollo sobre relaciones laborales de carácter especial (alta dirección RD 1382/1985, empleados de hogar RD 1620/2011, etc.)
- **Ley 31/1995** de Prevención de Riesgos Laborales
- **Ley Orgánica 3/2007** para la igualdad efectiva de mujeres y hombres (planes de igualdad)
- **Convenio colectivo aplicable** (ver sección específica arriba)

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio jurídico subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea específica con `[revisión]` inline. La etiqueta `[revisión]` ES el mecanismo. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/laboral:entrevista-inicial --repetir`*
