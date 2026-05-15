<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /concursal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /concursal:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/concursal/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Concursal
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/concursal:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho concursal se quedan aquí.*

[Empresa] es una [tipo de entidad — despacho / asesoría interna / administrador concursal].
Rol habitual: [PLACEHOLDER — representación del deudor / representación de acreedores / administración concursal / asesor de operaciones distressed].
Juzgados de lo Mercantil habituales: [PLACEHOLDER — provincia/s]. El equipo concursal cuenta con [N] personas.
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Experiencia concursal:** [PLACEHOLDER — número aproximado de concursos gestionados, perfil de los mismos] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos concursales abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración concursal profesional] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Administrador concursal | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Registro Público Concursal | [PLACEHOLDER ✓/✗] | Consulta manual en publicidadconcursal.es |
| LexNET / Justicia Digital | [PLACEHOLDER ✓/✗] | Presentación por procurador |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/concursal:entrevista-inicial --check-integraciones`*

---

## Rol en el procedimiento concursal

| Rol | Descripción | Frecuencia |
|---|---|---|
| Deudor | Representación del concursado en concurso voluntario o necesario | [PLACEHOLDER] |
| Acreedor | Defensa de créditos en la masa pasiva, impugnación de la lista | [PLACEHOLDER] |
| Administración concursal | Designación como administrador concursal (persona física o jurídica) | [PLACEHOLDER] |
| Adquirente de unidad productiva | Asesoramiento en adquisición de activos/unidades productivas | [PLACEHOLDER] |
| Asesor de reestructuración pre-concursal | Planes de reestructuración y comunicación art. 583 TRLC | [PLACEHOLDER] |

---

## Presupuestos del concurso

| Presupuesto | Descripción | Base legal |
|---|---|---|
| Subjetivo | Persona natural o jurídica (también herencia yacente) | Art. 1 TRLC |
| Objetivo | Insolvencia: no puede cumplir regularmente sus obligaciones exigibles | Art. 2 TRLC |
| Insolvencia actual | El deudor ya no puede cumplir | Art. 2.3 TRLC |
| Insolvencia inminente | El deudor prevé que no podrá cumplir | Art. 2.3 TRLC |
| Probabilidad de insolvencia | Para planes de reestructuración | Art. 584.2 TRLC |

---

## Comunicación del art. 583 TRLC (pre-concurso)

| Campo | Detalle |
|---|---|
| Finalidad | Comunicar al juzgado el inicio de negociaciones con acreedores para plan de reestructuración |
| Plazo de protección | 3 meses (prorrogable otros 3) desde comunicación |
| Efectos | Suspensión de ejecuciones singulares sobre bienes necesarios; no obligación de solicitar concurso |
| Experto en reestructuración | Posibilidad de solicitar nombramiento (art. 672 TRLC) |
| Desistimiento | Comunicación al juzgado si no se alcanza acuerdo |

**Comunicaciones art. 583 activas:** [PLACEHOLDER]

---

## Declaración de concurso

| Tipo | Quién solicita | Plazo | Efectos principales |
|---|---|---|---|
| Voluntario | El propio deudor | 2 meses desde conocimiento de insolvencia (art. 5 TRLC) | Deudor conserva facultades de administración (art. 106 TRLC) |
| Necesario | Acreedor u otros legitimados | — | Suspensión de facultades del deudor (art. 106 TRLC) |

**Juzgado competente:** Juzgado de lo Mercantil del domicilio del deudor (art. 10 TRLC)

---

## Masa activa y masa pasiva

### Masa activa

| Concepto | Descripción | Consideraciones |
|---|---|---|
| Bienes y derechos del deudor | Todo el patrimonio a fecha de declaración | Art. 192 TRLC |
| Bienes de terceros | Separatio ex iure dominii | Art. 227 TRLC |
| Acciones de reintegración | Rescisión de actos perjudiciales (2 años anteriores) | Arts. 226-237 TRLC |

### Masa pasiva — Clasificación de créditos

| Categoría | Descripción | Ejemplos | Base legal |
|---|---|---|---|
| Créditos contra la masa | Generados tras declaración de concurso | Salarios corrientes, créditos de la administración concursal | Art. 242 TRLC |
| Privilegio especial | Garantía real sobre bien concreto | Hipotecarios, pignoraticios, arrendamientos financieros | Art. 270 TRLC |
| Privilegio general | Preferencia sin afección a bien concreto | Salarios (hasta límites), retenciones tributarias y SS, créditos de persona especialmente relacionada con acreedor público | Art. 280 TRLC |
| Ordinarios | Sin privilegio ni subordinación | Proveedores, préstamos sin garantía | Art. 269 TRLC |
| Subordinados | Postergados por ley | Intereses, multas, personas especialmente relacionadas, tardíamente comunicados | Art. 281 TRLC |

**Tratamiento habitual de créditos:** [PLACEHOLDER — política de comunicación, impugnación del inventario y la lista]

---

## Plan de reestructuración (Libro II TRLC)

| Aspecto | Detalle | Base legal |
|---|---|---|
| Contenido mínimo | Descripción de la situación, medidas propuestas, plan de viabilidad | Art. 633 TRLC |
| Clases de créditos afectados | Al menos una clase por cada categoría de créditos | Art. 623 TRLC |
| Mayorías | 2/3 del pasivo de cada clase afectada (regla general) | Art. 629 TRLC |
| Homologación judicial | Cross-class cram-down posible | Art. 639 TRLC |
| Impugnación | 15 días desde publicación | Art. 654 TRLC |

---

## Convenio concursal

| Aspecto | Detalle | Base legal |
|---|---|---|
| Contenido | Quitas (sin límite) y/o esperas (sin límite) | Art. 316 TRLC |
| Mayorías | Según porcentaje de quita/espera (art. 376 TRLC) | Variable |
| Aprobación judicial | Control de legalidad | Art. 382 TRLC |
| Incumplimiento | Apertura de liquidación | Art. 404 TRLC |

---

## Liquidación

| Aspecto | Detalle | Base legal |
|---|---|---|
| Apertura | De oficio, a solicitud del deudor o del administrador concursal | Arts. 406-413 TRLC |
| Plan de liquidación | Presentado por administración concursal en 15 días | Art. 415 TRLC |
| Venta de unidad productiva | Preferencia legal de enajenación como unidad | Art. 421 TRLC |
| Sucesión de empresa | Riesgo de sucesión laboral y tributaria | Arts. 221-222 TRLC |
| Pago de créditos | Orden de prelación según clasificación | Arts. 429-435 TRLC |

---

## Calificación del concurso

| Calificación | Consecuencias | Base legal |
|---|---|---|
| Fortuito | Sin consecuencias personales ni patrimoniales adicionales | Art. 441 TRLC |
| Culpable | Inhabilitación (2-15 años), pérdida de derechos, condena a cobertura del déficit concursal | Arts. 442-456 TRLC |

**Presunción de culpabilidad (iuris et de iure):** Art. 443 TRLC — incumplimiento de obligación de solicitar concurso, irregularidades contables graves, alzamiento de bienes
**Presunción de culpabilidad (iuris tantum):** Art. 444 TRLC — incumplimiento de depósito de cuentas, contabilidad irregular

---

## Exoneración del pasivo insatisfecho — Segunda oportunidad

| Aspecto | Detalle | Base legal |
|---|---|---|
| Beneficiario | Persona natural (también autónomos) | Art. 486 TRLC |
| Requisito de buena fe | No haber sido declarado culpable, no haber rechazado oferta de empleo adecuada, no haber incumplido deberes de colaboración | Art. 487 TRLC |
| Exoneración provisional | Con plan de pagos (3-5 años) | Art. 495 TRLC |
| Exoneración definitiva | Cumplido el plan de pagos o transcurrido el plazo | Art. 500 TRLC |
| Créditos no exonerables | Créditos públicos (parcialmente), alimentos, créditos por responsabilidad extracontractual | Art. 489 TRLC |

---

## Concurso de persona natural

| Aspecto | Consideraciones especiales |
|---|---|
| Vivienda habitual | Protección especial en liquidación; posibilidad de mantenerla en plan de pagos |
| Masa activa | Bienes inembargables excluidos (art. 607 LEC) |
| Acuerdo extrajudicial de pagos | Mediador concursal (arts. 631 y ss. TRLC — derogado parcialmente, verificar vigencia) |
| Deudas empresariales del autónomo | Se incluyen en el concurso personal |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Comunicación de créditos | Equipo concursal | — | — |
| Impugnación de lista de acreedores / inventario | Equipo concursal | Socio/Director | Si crédito > [PLACEHOLDER] |
| Solicitud de concurso (voluntario) | — | Socio/Director + Dirección | Siempre |
| Solicitud de concurso (necesario) | — | Socio/Director | Siempre |
| Sección de calificación | — | Socio/Director + Dirección General | Siempre |
| Adquisición de unidad productiva | — | Socio/Director + Dirección + Laboral + Fiscal | Siempre |
| Plan de reestructuración | — | Socio/Director + Dirección | Siempre |

---

## Referencias legislativas principales

- **TRLC** — Real Decreto Legislativo 1/2020, de 5 de mayo, por el que se aprueba el Texto Refundido de la Ley Concursal
- **Directiva (UE) 2019/1023** — sobre marcos de reestructuración preventiva (transpuesta al TRLC por Ley 16/2022)
- **Ley 16/2022** — de reforma del TRLC para transposición de la Directiva de reestructuración
- **LEC** — Ley 1/2000, de Enjuiciamiento Civil (supletoria)
- **CC** — Código Civil (régimen general de obligaciones y contratos)
- **ET** — Estatuto de los Trabajadores (ERE concursal, sucesión de empresa)

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Solicitud de concurso de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Comunicación de créditos tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Plan de reestructuración de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan solicitudes, comunicaciones de créditos, informes y planes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/concursal:entrevista-inicial --redo`*
