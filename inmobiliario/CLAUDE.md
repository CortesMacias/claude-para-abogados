<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /inmobiliario:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /inmobiliario:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/inmobiliario/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Inmobiliario
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/inmobiliario:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho inmobiliario se quedan aquí.*

[Empresa] es una [tipo de entidad]. Operaciones inmobiliarias habituales: [PLACEHOLDER — compraventa, arrendamiento, promoción, inversión].
Zona geográfica principal: [PLACEHOLDER — CCAA / provincia / municipio]. El equipo inmobiliario cuenta con [N] personas.
[Responsable del área: nombre o ninguno]. Notaría habitual: [PLACEHOLDER]. Registro de la Propiedad habitual: [PLACEHOLDER].
La escalación va a [nombre].

**Tipología de activos:** [PLACEHOLDER — residencial / comercial / industrial / suelo / mixto] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos inmobiliarios abiertos:** [PLACEHOLDER — operaciones en curso, litigios, procedimientos registrales]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Promotora / SOCIMI / fondo] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Registro de la Propiedad online | [PLACEHOLDER ✓/✗] | Solicitud presencial de notas simples |
| Catastro (Sede electrónica) | [PLACEHOLDER ✓/✗] | Consulta manual |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/inmobiliario:entrevista-inicial --check-integraciones`*

---

## Tipos de operaciones habituales

| Operación | Frecuencia | Valor medio | Parte habitual | Notas |
|---|---|---|---|---|
| Compraventa | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — comprador/vendedor/ambos] | [PLACEHOLDER] |
| Arrendamiento urbano — vivienda | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — arrendador/arrendatario] | [PLACEHOLDER] |
| Arrendamiento urbano — uso distinto | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Promoción inmobiliaria | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Operaciones societarias con inmuebles | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otra operación] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Compraventa de inmuebles

### Arras y precontrato

| Tipo de arras | Efecto | Uso habitual | Base legal |
|---|---|---|---|
| Penitenciales | Desistimiento: comprador pierde arras / vendedor devuelve el doble | [PLACEHOLDER] | Art. 1454 CC |
| Confirmatorias | Señal a cuenta del precio; no permiten desistimiento | [PLACEHOLDER] | Doctrina jurisprudencial |
| Penales | Pena convencional + cumplimiento forzoso | [PLACEHOLDER] | Arts. 1152-1153 CC |

**Importe habitual de arras:** [PLACEHOLDER — % del precio]

### Proceso de compraventa — Checklist

| Paso | Responsable | Documentación | Notas |
|---|---|---|---|
| Due diligence registral (nota simple) | [PLACEHOLDER] | Nota simple informativa | Cargas, titularidad, superficie, descripción |
| Due diligence urbanística | [PLACEHOLDER] | Cédula urbanística / informe municipal | Situación urbanística, afecciones |
| Due diligence catastral | [PLACEHOLDER] | Referencia catastral, certificación | Concordancia registro-catastro |
| Condiciones suspensivas | [PLACEHOLDER] | Contrato de arras / promesa | [PLACEHOLDER — financiación, licencias, etc.] |
| Cargas registrales | [PLACEHOLDER] | Nota simple | Hipotecas, embargos, anotaciones |
| Escritura pública | Notario | Escritura de compraventa | [PLACEHOLDER] |
| Liquidación de impuestos | [PLACEHOLDER] | Modelo 600 (ITP) o factura (IVA) | [PLACEHOLDER] |
| Inscripción en el Registro | [PLACEHOLDER] | Copia autorizada | Principio de prioridad registral |

---

## Arrendamiento urbano (LAU 29/1994)

### Vivienda (Título II LAU)

| Aspecto | Régimen legal | Posición habitual |
|---|---|---|
| Duración mínima | 5 años (persona física) / 7 años (persona jurídica) — art. 9 LAU | [PLACEHOLDER] |
| Prórroga tácita | 3 años adicionales — art. 10 LAU | [PLACEHOLDER] |
| Renta | Libre fijación inicial; actualización según pacto o IPC — art. 18 LAU | [PLACEHOLDER] |
| Zona tensionada | Limitación de renta inicial si aplica (Ley 12/2023 de Vivienda) | [PLACEHOLDER — zona tensionada sí/no] |
| Fianza | 1 mensualidad obligatoria; garantía adicional máx. 2 mensualidades — art. 36 LAU | [PLACEHOLDER] |
| Obras del arrendatario | Consentimiento escrito del arrendador — art. 23 LAU | [PLACEHOLDER] |
| Resolución | Causas tasadas — arts. 27-28 LAU | [PLACEHOLDER] |

### Uso distinto de vivienda (Título III LAU)

| Aspecto | Régimen legal | Posición habitual |
|---|---|---|
| Duración | Libre pacto — art. 29 LAU | [PLACEHOLDER] |
| Renta y actualización | Libre pacto — arts. 29-30 LAU | [PLACEHOLDER] |
| Fianza | 2 mensualidades obligatorias — art. 36.1 LAU | [PLACEHOLDER] |
| Cesión y subarriendo | Posible salvo pacto en contrario — art. 32 LAU | [PLACEHOLDER] |
| Indemnización por clientela | 1 mes por año hasta máx. 18 meses (comercio) — art. 34 LAU | [PLACEHOLDER] |

---

## Propiedad horizontal (LPH 49/1960)

| Aspecto | Normativa | Consideraciones |
|---|---|---|
| Estatutos de la comunidad | Art. 5 LPH | [PLACEHOLDER — restricciones habituales, uso turístico] |
| Actas y acuerdos | Arts. 19-20 LPH | Mayorías: simple, 3/5, unanimidad según materia |
| Derramas y gastos extraordinarios | Art. 9.1.e LPH | [PLACEHOLDER — política habitual] |
| Impugnación de acuerdos | Art. 18 LPH | Plazo: 3 meses (1 año para contrarios a ley) |
| Morosos | Art. 21 LPH | Procedimiento monitorio con certificación de deuda |
| Alquiler turístico | Art. 17.12 LPH | Acuerdo de 3/5 para limitar o condicionar |

---

## Registro de la Propiedad

| Principio registral | Descripción | Base legal |
|---|---|---|
| Legitimación | Lo inscrito se presume exacto e íntegro | Art. 38 LH |
| Fe pública registral | Tercero de buena fe que adquiere confiando en el Registro queda protegido | Art. 34 LH |
| Prioridad | Primer título inscrito prevalece | Art. 17 LH |
| Tracto sucesivo | Para inscribir un derecho, debe estar inscrito el del transmitente | Art. 20 LH |
| Calificación | El registrador califica la legalidad de los documentos | Art. 18 LH |

**Operaciones registrales habituales:** [PLACEHOLDER — inscripciones, anotaciones preventivas, cancelaciones, notas marginales]

---

## Urbanismo

| Aspecto | Normativa | Consideraciones |
|---|---|---|
| Clasificación del suelo | TRLSRU (RDLeg 7/2015) + normativa autonómica | Urbano, urbanizable, no urbanizable/rústico |
| Licencias urbanísticas | Normativa autonómica + PGOU municipal | [PLACEHOLDER — licencia de obras, primera ocupación, actividad] |
| Declaración responsable | Normativa autonómica | [PLACEHOLDER — actividades sujetas] |
| Disciplina urbanística | Normativa autonómica | Plazos de prescripción variables por CCAA |
| PGOU / planeamiento | TRLSRU + normativa autonómica | [PLACEHOLDER — plan vigente, revisiones en curso] |

**CCAA principal de actuación:** [PLACEHOLDER — normativa urbanística autonómica aplicable]

---

## Fiscalidad inmobiliaria

| Operación | Impuesto | Tipo | Notas |
|---|---|---|---|
| Compraventa (segunda transmisión) | ITP | [PLACEHOLDER — tipo autonómico, 6-10%] | [PLACEHOLDER] |
| Compraventa (primera transmisión o promotor) | IVA + AJD | 10% IVA (21% comercial) + AJD autonómico | [PLACEHOLDER] |
| Hipoteca | AJD | [PLACEHOLDER — tipo autonómico, a cargo de entidad financiera] | [PLACEHOLDER] |
| Plusvalía municipal (IIVTNU) | IIVTNU | Según valor catastral y años de tenencia | [PLACEHOLDER — método real o estimación objetiva] |
| Ganancia patrimonial en IRPF/IS | IRPF o IS | Según régimen del transmitente | [PLACEHOLDER] |
| Arrendamiento | IRPF/IS + IVA (si uso distinto) | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Compraventa rutinaria | Equipo inmobiliario | — | — |
| Cargas registrales complejas | Equipo inmobiliario | Socio/Director | Si afectan a viabilidad de operación |
| Arrendamiento con cláusulas no estándar | Equipo inmobiliario | Socio/Director | Si renta > [PLACEHOLDER] o duración > [PLACEHOLDER] |
| Litigio arrendaticio (desahucio, resolución) | — | Procesal + Dirección | Siempre |
| Operación con componente urbanístico complejo | — | Socio/Director + urbanista | Siempre |
| Promoción inmobiliaria | — | Socio/Director + Dirección | Siempre |

---

## Referencias legislativas principales

- **CC** — Código Civil (derechos reales, arts. 348 y ss.; compraventa, arts. 1445 y ss.; arras, art. 1454)
- **LAU** — Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos
- **LPH** — Ley 49/1960, de 21 de julio, sobre Propiedad Horizontal
- **LH** — Ley Hipotecaria (Decreto de 8 de febrero de 1946, texto refundido)
- **TRLSRU** — Real Decreto Legislativo 7/2015, de 30 de octubre, de Suelo y Rehabilitación Urbana
- **Ley 12/2023** — Ley por el Derecho a la Vivienda (zonas tensionadas)
- **Normativa autonómica urbanística** — según CCAA de actuación

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Contrato de arras de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Contrato de arrendamiento tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Checklist de due diligence inmobiliaria | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan contratos, informes de due diligence y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/inmobiliario:entrevista-inicial --redo`*
