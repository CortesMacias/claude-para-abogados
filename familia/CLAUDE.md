<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /familia:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /familia:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/familia/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho de Familia
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/familia:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho de familia se quedan aquí.*

[Empresa] es un [tipo de entidad — despacho / servicio de mediación / turno de oficio].
Partido judicial principal: [PLACEHOLDER]. CCAA: [PLACEHOLDER — relevante para régimen económico foral y parejas de hecho].
El equipo de familia cuenta con [N] personas. Mediadores familiares: [PLACEHOLDER — sí/no, acreditación].
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Perfil de asuntos:** [PLACEHOLDER — divorcios de mutuo acuerdo / contenciosos / modificación de medidas / ejecución / internacional] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos de familia abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Turno de oficio | Servicio de mediación] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Mediador/a familiar | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| LexNET / Justicia Digital | [PLACEHOLDER ✓/✗] | Presentación por procurador |
| Calculadora de pensiones alimenticias (tablas orientadoras CGPJ) | [PLACEHOLDER ✓/✗] | Cálculo manual |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/familia:entrevista-inicial --check-integraciones`*

---

## Tipos de procedimiento

| Procedimiento | Frecuencia | Parte habitual | Juzgado competente |
|---|---|---|---|
| Divorcio / separación de mutuo acuerdo | [PLACEHOLDER] | [PLACEHOLDER — ambas partes / una parte] | Juzgado de Familia (o 1.ª Instancia) del último domicilio común |
| Divorcio / separación contencioso | [PLACEHOLDER] | [PLACEHOLDER — demandante / demandado] | Juzgado de Familia del domicilio del demandado |
| Medidas paternofiliales (parejas no casadas) | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado del domicilio del menor |
| Modificación de medidas | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado que dictó la sentencia originaria |
| Ejecución de sentencia de familia | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado que dictó la sentencia |
| Liquidación de régimen económico matrimonial | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado de Familia |
| Sustracción internacional de menores | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado de 1.ª Instancia (Convenio de La Haya) |

---

## Convenio regulador

### Contenido obligatorio (art. 90 CC)

| Materia | Posición habitual del despacho | Consideraciones |
|---|---|---|
| Guarda y custodia | [PLACEHOLDER — custodia compartida / exclusiva como preferencia] | Interés superior del menor (art. 2 LOPJM); criterio del TS y audiencias provinciales |
| Régimen de visitas y comunicaciones | [PLACEHOLDER — modelo estándar: fines de semana alternos + mitad vacaciones] | [PLACEHOLDER] |
| Uso de vivienda familiar | [PLACEHOLDER — criterio: atribución al progenitor custodio / interés del menor] | Art. 96 CC; doctrina TS sobre temporalidad |
| Pensión de alimentos | [PLACEHOLDER — referencia a tablas CGPJ / criterio de proporcionalidad] | Arts. 142-153 CC; gastos ordinarios vs extraordinarios |
| Pensión compensatoria | [PLACEHOLDER — criterio: desequilibrio económico, duración, cuantía] | Art. 97 CC; criterios del TS |
| Liquidación del régimen económico | [PLACEHOLDER — se incluye en convenio o procedimiento aparte] | Según régimen económico aplicable |

### Gastos extraordinarios

| Tipo | Consensuados / judicialmente autorizados | Reparto habitual |
|---|---|---|
| Sanitarios no cubiertos por SS | [PLACEHOLDER] | [PLACEHOLDER — 50/50 o proporcional] |
| Actividades extraescolares | [PLACEHOLDER] | [PLACEHOLDER] |
| Educación especial / refuerzo | [PLACEHOLDER] | [PLACEHOLDER] |
| Otros (permiso de conducir, viajes, etc.) | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Regímenes económicos matrimoniales

### Derecho común (CC)

| Régimen | Descripción | Liquidación | Base legal |
|---|---|---|---|
| Sociedad de gananciales | Régimen legal supletorio; bienes comunes los adquiridos durante el matrimonio a título oneroso | Inventario → avalúo → liquidación → adjudicación | Arts. 1344-1410 CC |
| Separación de bienes | Cada cónyuge conserva la propiedad de sus bienes | No hay masa común que liquidar (salvo bienes pro indiviso) | Arts. 1435-1444 CC |
| Participación | Cada cónyuge adquiere derecho a participar en las ganancias del otro | Cálculo de ganancias y derecho de crédito | Arts. 1411-1434 CC |

### Derechos forales

| Derecho foral | Régimen supletorio | CCAA | Normativa |
|---|---|---|---|
| Cataluña | Separación de bienes | Cataluña | Ley 25/2010 del Libro II del CC de Cataluña |
| Aragón | Consorcio conyugal (similar a gananciales) | Aragón | DL 1/2011 del Código del Derecho Foral de Aragón |
| País Vasco | Comunicación foral (Bizkaia) / gananciales (resto) | País Vasco | Ley 5/2015 de Derecho Civil Vasco |
| Navarra | Sociedad conyugal de conquistas | Navarra | Ley 1/1973, Compilación del Derecho Civil Foral de Navarra |
| Baleares | Separación de bienes | Baleares | Compilación del Derecho Civil de Baleares (DL 79/1990) |
| Galicia | Gananciales (CC) con particularidades | Galicia | Ley 2/2006 de Derecho Civil de Galicia |
| Valencia | Separación de bienes (régimen autonómico anulado por STC; aplica CC) | Comunidad Valenciana | CC (tras STC 82/2016) |

**Derecho foral aplicable habitualmente:** [PLACEHOLDER — según vecindad civil de los clientes]

---

## Parejas de hecho

| CCAA | Regulación | Registro | Efectos patrimoniales |
|---|---|---|---|
| [PLACEHOLDER — CCAA principal de actuación] | [PLACEHOLDER — ley autonómica] | [PLACEHOLDER — registro autonómico] | [PLACEHOLDER — pacto de convivencia / régimen supletorio] |

**Nota:** La regulación de parejas de hecho es exclusivamente autonómica. No existe legislación estatal unificada.

---

## Mediación familiar

| Campo | Detalle | Base legal |
|---|---|---|
| Marco legal estatal | Ley 5/2012, de 6 de julio, de Mediación en Asuntos Civiles y Mercantiles | Ley 5/2012 |
| Legislación autonómica | [PLACEHOLDER — ley autonómica de mediación familiar aplicable] | [PLACEHOLDER] |
| Mediadores acreditados en el equipo | [PLACEHOLDER — sí/no, nombres, número de registro] | |
| Derivación judicial a mediación | [PLACEHOLDER — frecuencia, juzgados que derivan habitualmente] | Art. 414.1 LEC |
| Sesión informativa obligatoria | [PLACEHOLDER — según normativa autonómica] | Variable por CCAA |

---

## Medidas provisionales y provisionalísimas

| Tipo | Cuándo | Plazo | Base legal |
|---|---|---|---|
| Medidas provisionalísimas (previas a la demanda) | Urgencia: riesgo para el menor o violencia | 30 días para presentar demanda | Art. 771 LEC |
| Medidas provisionales (coetáneas a la demanda) | Con la admisión de la demanda | Vigentes hasta sentencia firme | Art. 773 LEC |
| Medidas definitivas | En sentencia | Hasta modificación judicial | Art. 774 LEC |

---

## Ejecución de sentencias de familia

| Incumplimiento | Mecanismo | Plazo | Base legal |
|---|---|---|---|
| Impago de pensión alimenticia | Ejecución dineraria; posible delito de abandono de familia (art. 227 CP) | Sin plazo de caducidad para alimentos devengados | Arts. 776 LEC, 608 LEC |
| Incumplimiento de régimen de visitas | Ejecución no dineraria; multas coercitivas; cambio de custodia en casos graves | — | Art. 776.3 LEC |
| Incumplimiento de uso de vivienda | Lanzamiento | — | Art. 776 LEC |

---

## Sustracción internacional de menores

| Campo | Detalle | Base legal |
|---|---|---|
| Marco legal | Convenio de La Haya de 25 de octubre de 1980 sobre los Aspectos Civiles de la Sustracción Internacional de Menores | Convenio de La Haya 1980 |
| Autoridad Central española | Ministerio de Justicia — Subdirección General de Cooperación Jurídica Internacional | |
| Reglamento UE | Reglamento (UE) 2019/1111 (Bruselas II ter) — competencia, reconocimiento y ejecución en materia matrimonial y de responsabilidad parental | Reglamento 2019/1111 |
| Plazo de resolución | 6 semanas (objetivo del Convenio) | Art. 11 Convenio de La Haya |
| Excepciones a la restitución | Art. 13 Convenio: grave riesgo, oposición del menor con madurez suficiente, integración en nuevo medio | Art. 13 Convenio |

---

## Violencia de género — Aspectos civiles

| Campo | Detalle | Base legal |
|---|---|---|
| Juzgado competente | Juzgado de Violencia sobre la Mujer (competencia civil y penal acumulada) | Art. 87 ter LOPJ; LO 1/2004 |
| Orden de protección | Medidas civiles y penales cautelares (72 horas para resolver) | Art. 544 ter LECrim |
| Medidas civiles en orden de protección | Atribución vivienda, custodia, régimen de visitas, pensión alimentos | Art. 544 ter.7 LECrim |
| Vigencia de medidas civiles | 30 días; se extinguen si no se ratifican en proceso de familia | Art. 544 ter.7 LECrim |
| Suspensión de régimen de visitas | Posible si el menor es víctima directa o indirecta | Art. 94 CC (reforma Ley 8/2021) |

**Nota sensible:** Los asuntos de violencia de género requieren especial cuidado en la confidencialidad y protección de datos de la víctima.

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Divorcio de mutuo acuerdo | Equipo de familia | — | — |
| Divorcio contencioso | Equipo de familia | Socio/Director | Si patrimonio > [PLACEHOLDER] o custodia disputada |
| Sustracción internacional | — | Socio/Director + Internacional | Siempre |
| Violencia de género | — | Socio/Director + Penal | Siempre |
| Liquidación de régimen económico complejo | — | Socio/Director + Patrimonial | Si patrimonio > [PLACEHOLDER] |
| Ejecución con indicios de insolvencia | Equipo de familia | Socio/Director | Si impago > 6 meses |

---

## Referencias legislativas principales

- **CC** — Código Civil: Libro I, Título IV (matrimonio, arts. 42-107); Título VII (patria potestad, arts. 154-171); Libro IV, Título III, Cap. IV-V (régimen económico matrimonial, arts. 1315-1444)
- **LEC** — Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil: Libro IV, Título I, Cap. IV (procesos de familia, arts. 748-781)
- **Ley 5/2012** — Ley de Mediación en Asuntos Civiles y Mercantiles
- **LO 1/2004** — Ley Orgánica de Medidas de Protección Integral contra la Violencia de Género
- **Ley 8/2021** — Ley de protección integral a la infancia y adolescencia frente a la violencia (reforma del art. 94 CC)
- **LOPJM** — LO 1/1996, de Protección Jurídica del Menor
- **Convenio de La Haya 1980** — sobre Aspectos Civiles de la Sustracción Internacional de Menores
- **Reglamento (UE) 2019/1111** — Bruselas II ter (competencia y reconocimiento en materia de familia)
- **Legislación foral** — según derecho civil aplicable por vecindad civil

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Convenio regulador tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Demanda de divorcio contencioso de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Modelo de solicitud de medidas provisionales | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan convenios, demandas, informes y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/familia:entrevista-inicial --redo`*
