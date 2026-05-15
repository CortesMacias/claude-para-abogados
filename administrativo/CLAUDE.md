<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /administrativo:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /administrativo:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/administrativo/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Administrativo
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/administrativo:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho administrativo se quedan aquí.*

[Empresa] es una [tipo de entidad]. Interactuamos principalmente con [PLACEHOLDER — AGE / CCAA / EELL].
El equipo de derecho administrativo cuenta con [N] personas. Áreas principales de actuación:
[PLACEHOLDER — contratación pública / urbanismo / regulatorio / subvenciones / responsabilidad patrimonial / etc.].
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Administraciones con las que interactuamos habitualmente:** [PLACEHOLDER] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos administrativos abiertos:** [PLACEHOLDER — procedimientos en curso, recursos, licitaciones]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Plataforma de contratación del sector público | [PLACEHOLDER ✓/✗] | Consulta manual |
| Sede electrónica de administraciones | [PLACEHOLDER ✓/✗] | Gestión presencial o por representante |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/administrativo:entrevista-inicial --check-integraciones`*

---

## Administraciones con las que interactuamos

| Nivel | Administración | Materias habituales | Contacto |
|---|---|---|---|
| AGE (Administración General del Estado) | [PLACEHOLDER — ministerios concretos] | [PLACEHOLDER] | [PLACEHOLDER] |
| CCAA (Comunidades Autónomas) | [PLACEHOLDER — consejerías concretas] | [PLACEHOLDER] | [PLACEHOLDER] |
| EELL (Entidades Locales) | [PLACEHOLDER — ayuntamientos, diputaciones] | [PLACEHOLDER] | [PLACEHOLDER] |
| Organismos autónomos / Entidades de derecho público | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Procedimiento administrativo común (LPAC 39/2015)

### Fases del procedimiento

| Fase | Plazo legal | Consideraciones clave |
|---|---|---|
| Iniciación (de oficio o a instancia de parte) | — | Derecho a no aportar documentos ya en poder de la Administración (art. 28.2) |
| Instrucción | — | Trámite de audiencia (art. 82), vista del expediente (art. 53.1.a) |
| Resolución | Plazo específico según procedimiento; máximo 6 meses si no se fija otro (art. 21.3) | Obligación de resolver y notificar |
| Silencio administrativo | Agotado el plazo sin resolución expresa | Positivo (regla general solicitudes, art. 24.1) / Negativo (excepciones tasadas, art. 24.1 párr. 2) |

### Plazos clave

| Concepto | Plazo | Base legal |
|---|---|---|
| Resolución expresa (genérico) | 3 meses si no se fija otro (art. 21.3) | LPAC |
| Notificación por comparecencia | 10 días hábiles desde publicación en BOE/tablón | Art. 44 LPAC |
| Subsanación de solicitudes | 10 días hábiles | Art. 68.1 LPAC |
| Período de información pública | 20 días hábiles mínimo | Art. 83 LPAC |

---

## Recursos administrativos

| Recurso | Contra qué actos | Plazo | Órgano | Base legal |
|---|---|---|---|---|
| Alzada | Actos que no agotan vía administrativa | 1 mes (acto expreso) / 3 meses (presunto) | Superior jerárquico | Arts. 121-122 LPAC |
| Reposición (potestativo) | Actos que agotan vía administrativa | 1 mes (acto expreso) / 3 meses (presunto) | Mismo órgano | Arts. 123-124 LPAC |
| Extraordinario de revisión | Actos firmes (causas tasadas) | 4 años (error de hecho) / 3 meses (resto) | Mismo órgano | Art. 125 LPAC |

**Política interna sobre recursos:** [PLACEHOLDER — cuándo recurrimos, criterio de coste-beneficio]

---

## Contratación pública (LCSP 9/2017)

### Tipos de contrato habituales

| Tipo | Frecuencia | Valor medio | Notas |
|---|---|---|---|
| Obras | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Servicios | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Suministros | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Concesiones de servicios | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Contratos menores | [PLACEHOLDER] | [PLACEHOLDER] | Límites: 40.000€ obras / 15.000€ resto |

### Procedimientos de adjudicación

| Procedimiento | Cuándo se usa | Plazos clave |
|---|---|---|
| Abierto | Regla general | 35 días (oferta) / 15 días simplificado |
| Restringido | Cuando se requiere selección previa | 30 días (solicitud) + 25 días (oferta) |
| Negociado con publicidad | Supuestos tasados (art. 167) | Según pliegos |
| Negociado sin publicidad | Supuestos excepcionales (art. 168) | Según pliegos |
| Diálogo competitivo | Contratos particularmente complejos | Variable |
| Asociación para la innovación | I+D+i | Variable |

### PCAP y PPT — Estilo house

**Revisión estándar de pliegos incluye:** [PLACEHOLDER — checklist de revisión de PCAP/PPT]
**Cláusulas críticas:** [PLACEHOLDER — penalidades, modificación, resolución, revisión de precios]

### Recurso especial en contratación

| Campo | Detalle |
|---|---|
| Órgano | TACRC (estatal) / órganos autonómicos equivalentes |
| Plazo | 15 días hábiles desde notificación del acto |
| Actos recurribles | Anuncios de licitación, pliegos, actos de trámite cualificados, adjudicación |
| Efecto | Suspensión automática de la adjudicación (art. 53 LCSP) |
| Contratos recurribles | Sujetos a regulación armonizada + concesiones > umbrales |

---

## Responsabilidad patrimonial

| Campo | Detalle | Base legal |
|---|---|---|
| Plazo de reclamación | 1 año desde producción del hecho o manifestación del efecto lesivo | Art. 67.1 LPAC |
| Requisitos | Daño efectivo, evaluable, individualizable y antijurídico | Art. 32 LRJSP |
| Procedimiento | Regulado en LPAC + LRJSP | Arts. 65, 67, 81 LPAC; arts. 32-37 LRJSP |
| Dictamen del Consejo de Estado | Preceptivo si cuantía > 50.000€ o cuestiones de principio | Art. 81.2 LPAC |

**Asuntos de responsabilidad patrimonial abiertos:** [PLACEHOLDER]

---

## Subvenciones (LGS 38/2003)

| Campo | Detalle |
|---|---|
| Subvenciones habituales | [PLACEHOLDER — programas a los que se solicita habitualmente] |
| Obligaciones como beneficiario | Justificación del gasto, cumplimiento de fines, contabilidad separada, publicidad |
| Plazo de justificación | Según bases reguladoras (usualmente 3 meses desde fin del plazo de ejecución) |
| Procedimiento de reintegro | Arts. 36-37 LGS — 4 años de prescripción |

---

## Contencioso-administrativo (LJCA 29/1998)

| Campo | Detalle |
|---|---|
| Plazo para interponer recurso | 2 meses desde notificación (acto expreso) / 6 meses (silencio o vía de hecho) |
| Legitimación | Art. 19 LJCA — titulares de derechos o intereses legítimos |
| Medidas cautelares | Art. 129-136 LJCA — periculum in mora + ponderación de intereses |
| Órganos | Juzgados de lo Contencioso (unipersonales) / TSJ / AN / TS |
| Recurso de casación | Interés casacional objetivo (art. 88-93 LJCA) |
| Procedimiento abreviado | Cuantía < 30.000€ (art. 78 LJCA) |

**Criterio de litigación:** [PLACEHOLDER — cuándo se recomienda acudir al contencioso, análisis coste-beneficio]

---

## Expropiación forzosa

| Campo | Detalle | Base legal |
|---|---|---|
| Procedimiento general | Declaración de necesidad → justiprecio → pago/consignación → ocupación | LEF de 16 de diciembre de 1954 |
| Jurado Provincial de Expropiación | Fijación del justiprecio en caso de desacuerdo | Arts. 30-35 LEF |
| Recurso | Contencioso-administrativo contra acuerdo del Jurado | LJCA |
| Urgencia | Declaración de urgente ocupación — ocupación previa al justiprecio | Art. 52 LEF |
| Reversión | Derecho del expropiado si no se ejecuta la obra o sobra terreno | Art. 54 LEF |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Solicitud / instancia administrativa rutinaria | Equipo administrativo | — | — |
| Recurso de alzada o reposición | Equipo administrativo | Socio/Director | Si cuantía > [PLACEHOLDER] |
| Recurso especial en contratación (TACRC) | — | Socio/Director + Dirección | Siempre |
| Contencioso-administrativo | — | Socio/Director + Dirección | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Dirección General | Siempre |
| Expropiación | — | Dirección jurídica + Dirección | Siempre |

---

## Referencias legislativas principales

- **LPAC** — Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas
- **LRJSP** — Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público
- **LJCA** — Ley 29/1998, de 13 de julio, de la Jurisdicción Contencioso-Administrativa
- **LCSP** — Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público
- **LGS** — Ley 38/2003, de 17 de noviembre, General de Subvenciones
- **LEF** — Ley de Expropiación Forzosa de 16 de diciembre de 1954
- **LRBRL** — Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Modelo de recurso administrativo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Checklist de revisión de pliegos | [PLACEHOLDER] | [PLACEHOLDER] | |
| Demanda contencioso-administrativa de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan recursos, demandas, análisis de pliegos y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/administrativo:entrevista-inicial --redo`*
