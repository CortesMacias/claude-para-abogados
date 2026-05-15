# Claude para Abogados (España)

Agentes, skills y conectores de referencia para los flujos de trabajo jurídicos más habituales en España — mercantil, societario, laboral, propiedad intelectual, procesal, privacidad, consumo, regulatorio, gobernanza de IA, fiscal, administrativo, inmobiliario, concursal, familia, protección de datos, startups, clínica jurídica y estudiantes de Derecho.

> **¿Primera vez aquí?** Empieza por [QUICKSTART.md](QUICKSTART.md) — instalación en 60 segundos. Este README es la referencia completa.

> [!NOTE]
> **Atribución — Este proyecto es una adaptación al derecho español de [claude-for-legal](https://github.com/anthropics/claude-for-legal)**, el repositorio original creado por [Anthropic](https://www.anthropic.com). Toda la arquitectura de plugins, los patrones de diseño, la estructura de cold-start interviews y el concepto de perfiles de práctica son mérito del equipo de Anthropic. Este repositorio toma ese trabajo como base y lo adapta a la legislación española y de la Unión Europea, traduciendo al castellano y añadiendo áreas jurídicas propias del ordenamiento español. **El crédito del diseño original corresponde íntegramente a Anthropic.**

> [!CAUTION]
> **Descargo de responsabilidad**
>
> **Este proyecto NO ha sido testado con casos reales.** Los skills, agentes y perfiles de práctica han sido diseñados conforme a la legislación española vigente, pero no han sido validados en producción con documentos jurídicos reales. Pueden contener errores, omisiones o interpretaciones incorrectas.
>
> **Esto es una herramienta, no un sustituto del criterio profesional.** La inteligencia artificial asiste, pero no piensa por ti. Todo resultado generado por estos agentes requiere:
> - **Revisión humana** por un profesional cualificado antes de cualquier uso
> - **Pensamiento crítico** — no aceptes ningún resultado sin verificarlo
> - **Criterio profesional** — el abogado que usa la herramienta es quien decide, no la herramienta
>
> Este proyecto se proporciona "tal cual" (*as is*), sin garantías de ningún tipo, expresas o implícitas. **No constituye asesoramiento jurídico, ni sustituye el criterio de un abogado colegiado.**
>
> Los autores y colaboradores de este proyecto **no se hacen responsables** de ningún daño, perjuicio, pérdida económica o consecuencia de cualquier naturaleza derivados del uso, mal uso o imposibilidad de uso de estas herramientas. Esto incluye, sin limitación:
> - Errores en el contenido legal o referencias normativas incorrectas
> - Interpretaciones incorrectas de la legislación
> - Cambios normativos no reflejados en el proyecto
> - Decisiones tomadas basándose en los resultados generados
> - Plazos, cálculos o importes incorrectos
>
> **Todo resultado generado es un borrador para revisión profesional** — no es un dictamen, no es una conclusión jurídica, no sustituye a un abogado. Un letrado colegiado debe revisar, verificar y asumir la responsabilidad profesional de cualquier documento antes de su uso.
>
> El uso de este proyecto implica la aceptación de estas condiciones.

> [!IMPORTANT]
> **Estos plugins no representan posiciones jurídicas de Anthropic, ni de los autores de esta adaptación, ni de ninguna otra entidad.** Son herramientas que ayudan a los profesionales del Derecho a analizar cuestiones jurídicas. Cuando un skill incluye un checklist, un marco de análisis, una señal de riesgo o una caracterización de jurisprudencia o normativa, se trata de una ayuda al análisis del abogado, no de una opinión jurídica vinculante. La legislación en muchas de estas áreas está en evolución y sujeta a interpretación. El abogado que utiliza el plugin — no el plugin, y no los autores — es responsable de las posiciones jurídicas adoptadas en su trabajo.

---

## Agentes

Cada agente lleva el nombre del flujo de trabajo que ejecuta. Son el punto de entrada más habitual — empieza por los que encajan con tu práctica y ajusta el skill, el perfil de práctica y los conectores a cómo trabaja tu equipo.

### Mercantil

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de contratos mercantiles** | Revisa un contrato contra tu playbook y genera un memo de observaciones | `mercantil` | `/mercantil:revision` |
| **Triaje de NDAs** | VERDE/AMARILLO/ROJO — solo los complicados llegan al abogado | `mercantil` | `/mercantil:revision` |
| **Trazador de adendas** | Traza cómo ha cambiado un contrato a lo largo de sus modificaciones | `mercantil` | `/mercantil:historial-adendas` |
| **Vigilante de renovaciones** | Escanea el registro de contratos buscando vencimientos y renovaciones | `mercantil` | agente programado |
| **Debrief semanal** | Revisión semanal de contratos firmados con desviaciones del playbook | `mercantil` | agente programado |
| **Router de escalado** | Deriva cuestiones contractuales al aprobador correcto | `mercantil` | `/mercantil:escalado` |

### Societario

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de due diligence** | Revisión tabular de data room con una fila por documento y cada celda citada | `societario` | `/societario:revision-tabular` |
| **Extractor de incidencias** | Lee documentos del VDR y extrae incidencias por categoría y materialidad | `societario` | `/societario:extraccion-incidencias` |
| **Redactor de acuerdos sociales** | Redacta acuerdos del órgano de administración en formato house | `societario` | `/societario:acuerdo-social` |
| **Tracker de cumplimiento societario** | Plazos de presentación en el Registro Mercantil, cuentas anuales, libros | `societario` | `/societario:cumplimiento` |
| **Checklist de cierre** | Seguimiento de condiciones, consentimientos y documentos pendientes de cierre | `societario` | `/societario:checklist-cierre` |
| **Vigilante de data room** | Monitoriza el VDR para nuevas subidas y actualiza el estado del cierre | `societario` | agente programado |

### Laboral

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de despidos** | Analiza un despido propuesto contra los requisitos legales y el convenio | `laboral` | `/laboral:revision-despido` |
| **Revisor de contratación** | Revisa contratos de trabajo, cláusulas de no competencia, período de prueba | `laboral` | `/laboral:revision-contratacion` |
| **Clasificador de relación laboral** | Test de laboralidad vs. autónomo/falso autónomo | `laboral` | `/laboral:clasificacion` |
| **Redactor de políticas** | Redacta políticas laborales adaptadas al convenio colectivo | `laboral` | `/laboral:politica` |
| **Calculadora de indemnizaciones** | Cálculo de indemnización por tipo de despido y antigüedad | `laboral` | `/laboral:indemnizacion` |
| **Q&A laboral** | Respuesta rápida a consultas laborales con referencia a ET y convenio | `laboral` | `/laboral:consulta` |

### Propiedad Intelectual

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Screening de marca** | Primera búsqueda de disponibilidad con heurísticas de confusión (OEPM/EUIPO) | `propiedad-intelectual` | `/pi:busqueda-marca` |
| **Redactor de burofax** | Redacta o triaja un requerimiento extrajudicial de cese | `propiedad-intelectual` | `/pi:burofax` |
| **Revisor de licencias OSS** | Clasifica licencias open source según tu modelo de distribución | `propiedad-intelectual` | `/pi:oss` |
| **Triaje de infracción** | Triaje de marca/copyright/patente/secreto empresarial — factores, no dictamen | `propiedad-intelectual` | `/pi:triaje-infraccion` |
| **Revisor de cláusulas de PI** | Revisa cesión, titularidad, licencia, garantías e indemnizaciones | `propiedad-intelectual` | `/pi:clausulas` |
| **Tracker de portfolio** | Registros, renovaciones, tasas de mantenimiento | `propiedad-intelectual` | `/pi:portfolio` |

### Procesal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Cronología** | Construye o actualiza una cronología de hechos desde fuentes declaradas | `procesal` | `/procesal:cronologia` |
| **Redactor de demanda** | Borrador de sección de demanda en estilo house | `procesal` | `/procesal:demanda` |
| **Triaje de requerimiento recibido** | Analiza un requerimiento/demanda entrante — opciones, plazos, derivación | `procesal` | `/procesal:requerimiento-recibido` |
| **Calculadora de plazos** | Plazos procesales según LEC/LECrim/LJCA con días hábiles | `procesal` | `/procesal:plazos` |
| **Intake de asunto** | Alta de nuevo asunto — ficha, cronología inicial, log | `procesal` | `/procesal:intake` |
| **Briefing de asunto** | Briefing en profundidad de un asunto para reunión con socio o cliente | `procesal` | `/procesal:briefing` |
| **Estado del portfolio** | Distribución de riesgo, próximos plazos, asuntos sin actividad | `procesal` | `/procesal:portfolio` |

### Privacidad

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Respondedor de derechos ARCO-POL** | Redacta acuse y respuesta sustantiva dentro del plazo legal | `privacidad` | `/privacidad:derechos` |
| **Revisor de encargos de tratamiento** | Revisa un contrato de encargado del tratamiento contra tu playbook | `privacidad` | `/privacidad:encargo` |
| **Generador de EIPD** | Genera Evaluación de Impacto en Protección de Datos en formato house | `privacidad` | `/privacidad:eipd` |
| **Triaje de tratamiento** | Decide si un tratamiento necesita EIPD, consulta previa o puede proceder | `privacidad` | `/privacidad:triaje` |
| **Gap regulatorio de privacidad** | Compara un cambio normativo contra tu política de privacidad actual | `privacidad` | `/privacidad:gap` |

### Consumo

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de lanzamiento** | Revisa un lanzamiento de producto contra tu calibración de riesgo | `consumo` | `/consumo:lanzamiento` |
| **Checker de claims de marketing** | Señala claims que necesitan sustanciación o retirada (LGDCU, LCD) | `consumo` | `/consumo:claims` |
| **Revisor de condiciones generales** | Analiza condiciones generales de contratación con consumidores | `consumo` | `/consumo:condiciones-generales` |
| **¿Esto es un problema?** | Respuesta rápida al "¿podemos hacer esto?" con tu calibración | `consumo` | `/consumo:consulta` |

### Regulatorio

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Vigilante de normativa** | Monitoriza BOE, DOUE y boletines autonómicos y genera resumen | `regulatorio` | agente programado |
| **Diff de política** | Compara un cambio normativo contra tu biblioteca de políticas internas | `regulatorio` | `/regulatorio:diff` |
| **Tracker de gaps** | Gaps abiertos — qué se ha señalado y aún no se ha cerrado | `regulatorio` | `/regulatorio:gaps` |
| **Redactor de política** | Propuesta de redacción de política para cerrar un gap | `regulatorio` | `/regulatorio:redaccion` |

### Gobernanza de IA

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Triaje de caso de uso IA** | Clasifica usos de IA propuestos contra el EU AI Act y tu registro interno | `gobernanza-ia` | `/gobernanza-ia:triaje` |
| **Evaluador de impacto IA** | Evaluación de impacto de IA según los regímenes aplicables | `gobernanza-ia` | `/gobernanza-ia:evaluacion` |
| **Revisor de IA de proveedor** | Revisa cláusulas de IA de proveedores (entrenamiento, responsabilidad, cambios de modelo) | `gobernanza-ia` | `/gobernanza-ia:proveedor` |
| **Gap regulatorio de IA** | Compara nueva regulación de IA contra tu postura de gobernanza actual | `gobernanza-ia` | `/gobernanza-ia:gap` |

### Fiscal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Calendario fiscal** | Plazos de AEAT por tipo de obligación y forma jurídica | `fiscal` | `/fiscal:calendario` |
| **Revisor de declaraciones** | Revisión de coherencia de declaraciones de IRPF, IS, IVA | `fiscal` | `/fiscal:revision` |
| **Consulta tributaria** | Respuesta rápida a consultas fiscales con referencia a normativa y consultas DGT | `fiscal` | `/fiscal:consulta` |
| **Triaje de procedimiento** | Inspección, sancionador, reclamación TEA — plazos y opciones | `fiscal` | `/fiscal:procedimiento` |

### Administrativo

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Procedimiento administrativo** | Plazos, silencio administrativo, recursos (alzada, reposición, extraordinario) | `administrativo` | `/administrativo:procedimiento` |
| **Contratación pública** | Revisión de pliegos, criterios de adjudicación, recursos especiales (LCSP) | `administrativo` | `/administrativo:contratacion` |
| **Contencioso-administrativo** | Plazos, legitimación y estrategia para recurso contencioso (LJCA) | `administrativo` | `/administrativo:contencioso` |

### Inmobiliario

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de arrendamiento** | Revisa contrato de alquiler contra LAU y cláusulas habituales | `inmobiliario` | `/inmobiliario:arrendamiento` |
| **Compraventa** | Revisión de contrato de compraventa, arras, condiciones suspensivas | `inmobiliario` | `/inmobiliario:compraventa` |
| **Propiedad horizontal** | Revisión de estatutos, actas de junta, derramas | `inmobiliario` | `/inmobiliario:comunidad` |

### Concursal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Diagnóstico de insolvencia** | Análisis de la situación del deudor según TRLC | `concursal` | `/concursal:diagnostico` |
| **Plan de reestructuración** | Estructura básica de plan de reestructuración | `concursal` | `/concursal:plan` |
| **Calificación de créditos** | Clasificación de créditos (privilegiados, ordinarios, subordinados) | `concursal` | `/concursal:creditos` |

### Familia

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Convenio regulador** | Borrador de convenio regulador con los pactos habituales | `familia` | `/familia:convenio` |
| **Régimen económico** | Análisis del régimen económico matrimonial aplicable | `familia` | `/familia:regimen-economico` |
| **Pensiones** | Cálculo orientativo de pensión de alimentos y compensatoria | `familia` | `/familia:pensiones` |

### Protección de datos

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Registro de actividades** | Genera o actualiza el registro de actividades de tratamiento (RAT) | `proteccion-datos` | `/proteccion-datos:rat` |
| **Evaluación de impacto** | EIPD completa según guías AEPD | `proteccion-datos` | `/proteccion-datos:eipd` |
| **Gestión de brechas** | Protocolo de notificación de brecha (72h AEPD + comunicación a interesados) | `proteccion-datos` | `/proteccion-datos:brecha` |
| **Relación con AEPD** | Reclamaciones, inspecciones, procedimiento sancionador | `proteccion-datos` | `/proteccion-datos:aepd` |

### Startups

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Constitución de SL** | Checklist y borradores de estatutos y pacto de socios | `startups` | `/startups:constitucion` |
| **Stock options** | Estructura de stock options/phantom shares con régimen fiscal | `startups` | `/startups:stock-options` |
| **Ronda de inversión** | Revisión de term sheet y SHA con señales de riesgo | `startups` | `/startups:ronda` |
| **Incentivos fiscales** | Mapa de incentivos disponibles bajo la Ley de Startups | `startups` | `/startups:incentivos` |
| **Primeras contrataciones** | Guía para contratar los primeros empleados (tipo de contrato, convenio, coste) | `startups` | `/startups:contratacion` |

### Clínica jurídica

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Intake de cliente** | Recepción estructurada con detección de áreas y conflictos | `clinica-juridica` | `/clinica:intake` |
| **Memo de caso** | Memo con estructura IRAC adaptada con gaps de investigación señalados | `clinica-juridica` | `/clinica:memo` |
| **Hoja de ruta de investigación** | Legislación a consultar, jurisprudencia relevante, términos de búsqueda | `clinica-juridica` | `/clinica:investigacion` |
| **Tracker de plazos** | Plazos del caso con alertas de preclusión | `clinica-juridica` | `/clinica:plazos` |
| **Carta al cliente** | Correspondencia rutinaria — citaciones, solicitud de documentos, actualizaciones | `clinica-juridica` | `/clinica:carta` |

### Estudiante de Derecho

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Método socrático** | Pregunta, tú respondes, te desafía — no te da la respuesta | `estudiante-derecho` | `/estudiante:socratico` |
| **Evaluador IRAC** | Evalúa tu caso práctico en estructura, identificación del problema, normas, análisis | `estudiante-derecho` | `/estudiante:irac` |
| **Esquematizador** | Construye o amplía un esquema desde tus apuntes y manual | `estudiante-derecho` | `/estudiante:esquema` |
| **Preparación de oposiciones** | Temas, test y casos prácticos por especialidad | `estudiante-derecho` | `/estudiante:oposiciones` |
| **Preparación acceso a la abogacía** | Práctica de examen de acceso con retroalimentación | `estudiante-derecho` | `/estudiante:acceso` |
| **Fichas de estudio** | Genera o repasa fichas estilo Leitner | `estudiante-derecho` | `/estudiante:fichas` |
| **Planificador de estudio** | Plan a largo plazo con sesiones programadas | `estudiante-derecho` | `/estudiante:plan` |

---

## Estructura del repositorio

```
mercantil/                # contratos mercantiles, NDAs, SaaS, renovaciones
societario/               # due diligence, gobierno corporativo, cumplimiento registral
laboral/                  # contratación, despido, convenios, clasificación laboral
propiedad-intelectual/    # marcas, patentes, copyright, OSS, cláusulas de PI
procesal/                 # portfolio de asuntos, demandas, plazos, cronologías
privacidad/               # encargos de tratamiento, derechos ARCO-POL, EIPD
consumo/                  # lanzamientos, claims de marketing, condiciones generales
regulatorio/              # vigilancia BOE/DOUE, diff de políticas, gaps
gobernanza-ia/            # triaje AI Act, evaluaciones de impacto IA, proveedores
fiscal/                   # calendario AEAT, declaraciones, procedimientos tributarios
administrativo/           # procedimiento administrativo, contratación pública, contencioso
inmobiliario/             # arrendamientos, compraventa, propiedad horizontal
concursal/                # insolvencia, reestructuración, calificación de créditos
familia/                  # convenio regulador, régimen económico, pensiones
proteccion-datos/         # RAT, EIPD operativa, brechas, relación con AEPD
startups/                 # constitución, stock options, rondas, incentivos fiscales
clinica-juridica/         # intake, memos, plazos, correspondencia
estudiante-derecho/       # socrático, IRAC, oposiciones, acceso, fichas
hub-constructor/          # descubrimiento e instalación de skills comunitarios
recetas-agentes/          # cookbooks de agentes programados
references/               # materiales de referencia
scripts/                  # scripts de despliegue y validación
```

Cada directorio de plugin tiene la misma estructura:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # perfil de práctica — se rellena con /<plugin>:entrevista-inicial
  README.md
  skills/                 # skills — cada uno es un comando /<plugin>:<skill>
  agents/                 # agentes programados (si los hay)
  hooks/                  # hooks pre y post herramienta (si los hay)
```

---

## Conectores MCP

Los plugins alcanzan su máximo potencial cuando están conectados a fuentes de datos autorizadas. Consulta [CONNECTORS.md](CONNECTORS.md) para la lista completa de conectores actuales y deseados.

### MCPs por desarrollar

Estos conectores MCP no existen aún pero multiplicarían el valor de los plugins. Son candidatos naturales para desarrollo:

| MCP | Fuente | Plugins beneficiados | Prioridad |
|---|---|---|---|
| **CENDOJ** | Buscador de jurisprudencia del CGPJ | procesal, clinica-juridica, estudiante-derecho, laboral, familia | Alta |
| **BOE** | Boletín Oficial del Estado (legislación y disposiciones) | regulatorio, fiscal, administrativo, laboral, todos | Alta |
| **EUR-Lex** | Legislación y jurisprudencia de la UE | privacidad, gobernanza-ia, regulatorio, consumo | Alta |
| **AEPD Resoluciones** | Resoluciones y guías de la Agencia Española de Protección de Datos | privacidad, proteccion-datos | Alta |
| **Registro Mercantil** | Información registral de sociedades | societario, mercantil, concursal | Media |
| **OEPM** | Oficina Española de Patentes y Marcas | propiedad-intelectual | Media |
| **EUIPO** | Oficina de Propiedad Intelectual de la UE | propiedad-intelectual | Media |
| **DGT Consultas** | Consultas vinculantes de la Dirección General de Tributos | fiscal, startups | Media |
| **PLACE** | Plataforma de Contratación del Sector Público | administrativo | Media |
| **LexNET** | Notificaciones judiciales electrónicas | procesal, clinica-juridica | Media |
| **Registro Público Concursal** | Procedimientos concursales en curso | concursal | Baja |
| **Catastro** | Información catastral de inmuebles | inmobiliario | Baja |
| **Registro de la Propiedad** | Notas simples e información registral | inmobiliario | Baja |
| **CGPJ Tablas** | Tablas orientadoras de pensiones alimenticias | familia | Baja |
| **AESIA** | Agencia Española de Supervisión de IA (sandbox regulatorio) | gobernanza-ia | Baja |

Si desarrollas alguno de estos MCPs o conoces uno existente, abre un issue o un PR.

---

## Estado del proyecto

Este proyecto está en fase inicial. Los skills han sido diseñados pero **no han sido testados con casos reales**. Las referencias legislativas deben verificarse. Se agradecen contribuciones, especialmente:

- Correcciones de referencias normativas
- Tests con documentos jurídicos reales
- Desarrollo de conectores MCP
- Nuevos skills para áreas no cubiertas

---

## Créditos

Este proyecto es una **adaptación al derecho español** de [claude-for-legal](https://github.com/anthropics/claude-for-legal), creado por [Anthropic](https://www.anthropic.com) y publicado bajo la licencia Apache 2.0.

Todo el mérito del diseño original — la arquitectura de plugins, el sistema de cold-start interviews, los perfiles de práctica, los patrones de agentes programados y el concepto de skills jurídicos — corresponde al equipo de Anthropic. Este repositorio adapta ese trabajo al ordenamiento jurídico español, traduce al castellano y añade áreas de práctica propias del derecho español (fiscal, administrativo, inmobiliario, concursal, familia, protección de datos y startups).

## Licencia

[Apache 2.0](LICENSE) — la misma licencia que el proyecto original.
