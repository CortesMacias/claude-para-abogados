<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /propiedad-intelectual:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /propiedad-intelectual:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/propiedad-intelectual/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Propiedad Intelectual e Industrial

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/propiedad-intelectual:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de PI lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos un portfolio de [N] registros activos.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Agente de la propiedad industrial]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a colegiado/a | Agente de la propiedad industrial | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Portfolio de registros

### Marcas

| Marca | Territorio | N.º registro | Clase(s) Niza | Vencimiento | Estado |
|---|---|---|---|---|---|
| [PLACEHOLDER] | [OEPM/EUIPO/OMPI] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

**Alerta de renovación:** [PLACEHOLDER — ej., "6 meses antes del vencimiento"]

### Patentes y modelos de utilidad

| Título | Territorio | N.º solicitud/concesión | Vencimiento | Estado |
|---|---|---|---|---|
| [PLACEHOLDER] | [OEPM/OEP] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

**Pago de anualidades:** [PLACEHOLDER — ej., "Recordatorio 3 meses antes; gestor externo: [nombre]"]

### Diseños industriales

| Diseño | Territorio | N.º registro | Vencimiento | Estado |
|---|---|---|---|---|
| [PLACEHOLDER] | [OEPM/EUIPO] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

### Nombres de dominio

| Dominio | Registrador | Vencimiento | Renovación automática |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [sí/no] |

---

## Postura de enforcement

**Estrategia general:** [PLACEHOLDER — ej., "Defensa activa de marcas core; vigilancia de nuevas solicitudes en OEPM y EUIPO; acción contra infracciones evidentes"]

**Prioridades de enforcement:**
1. [PLACEHOLDER — ej., "Marcas denominativas principales"]
2. [PLACEHOLDER — ej., "Nombres de dominio confusamente similares"]
3. [PLACEHOLDER — ej., "Uso no autorizado en marketplaces"]

**Presupuesto anual de enforcement:** [PLACEHOLDER]

**Servicio de vigilancia:** [PLACEHOLDER — ej., "CompuMark / Corsearch / vigilancia interna mensual"]

---

## Marcas — Procedimientos por oficina

### OEPM (Oficina Española de Patentes y Marcas)

**Búsqueda previa:** [PLACEHOLDER — ej., "Siempre búsqueda fonética y gráfica en Localizador de marcas OEPM antes de solicitar"]
**Tasa de solicitud vigente:** [PLACEHOLDER — verificar en oepm.es]
**Plazo de oposición:** 2 meses desde publicación en BOPI
**Duración del registro:** 10 años renovables
**Posición ante oposiciones recibidas:** [PLACEHOLDER — ej., "Contestar siempre; escalar a responsable si oposición de marca notoria"]

### EUIPO (Oficina de Propiedad Intelectual de la UE)

**Uso habitual:** [PLACEHOLDER — ej., "Para marcas con presencia en varios Estados miembros; siempre que la marca principal se registre en OEPM"]
**Plazo de oposición:** 3 meses desde publicación
**Posición ante oposiciones:** [PLACEHOLDER]

### OMPI (Organización Mundial de la Propiedad Intelectual)

**Sistema de Madrid — uso:** [PLACEHOLDER — ej., "Para extensión a países fuera de la UE; marca base en OEPM"]
**Territorios designados habitualmente:** [PLACEHOLDER — ej., "EE.UU., Reino Unido, China, Japón"]

---

## Patentes — Procedimientos

### OEPM

**Tipos de protección:** Patente de invención (20 años) / Modelo de utilidad (10 años)
**Informe sobre el estado de la técnica:** [PLACEHOLDER — ej., "Solicitar siempre con la solicitud; plazo aproximado 12 meses"]
**Política de mantenimiento:** [PLACEHOLDER — ej., "Evaluar anualmente la utilidad comercial; abandonar patentes sin explotación tras 5 años"]

### OEP (Oficina Europea de Patentes)

**Uso habitual:** [PLACEHOLDER — ej., "Para invenciones con mercado europeo amplio; validación siempre en ES, DE, FR como mínimo"]
**Agente europeo de patentes:** [PLACEHOLDER]

---

## Derechos de autor (LPI)

**Obras protegidas principales:** [PLACEHOLDER — ej., "Software, bases de datos, contenido web, materiales de formación, diseños gráficos"]

**Software:**
- Protección: Derechos de autor (arts. 95-104 LPI), no patente en España
- Titularidad: [PLACEHOLDER — ej., "La empresa como persona jurídica si creado por empleados en el ejercicio de sus funciones (art. 97.4 LPI)"]
- Registro: [PLACEHOLDER — ej., "Registro de la Propiedad Intelectual para acreditación de autoría y fecha"]

**Bases de datos:**
- Protección sui generis (arts. 133-137 LPI)
- Derecho del fabricante: [PLACEHOLDER — ej., "15 años desde finalización; renovable si inversión sustancial adicional"]

**Cesión de derechos por empleados:**
- Art. 51 LPI: presunción de cesión al empresario de los derechos de explotación sobre obras creadas en virtud de relación laboral
- [PLACEHOLDER — cláusula house adicional en contratos de trabajo]

---

## Secretos empresariales (Ley 1/2019)

**Información clasificada como secreto empresarial:** [PLACEHOLDER — ej., "Algoritmos, bases de clientes, estrategias comerciales, know-how técnico"]

**Medidas razonables de protección adoptadas (art. 1.1.c Ley 1/2019):**
- [PLACEHOLDER — ej., "NDAs con empleados y terceros"]
- [PLACEHOLDER — ej., "Control de acceso por niveles"]
- [PLACEHOLDER — ej., "Marcado de documentos como confidenciales"]
- [PLACEHOLDER — ej., "Políticas de seguridad de la información"]

**Protocolo ante obtención/revelación ilícita:**
1. [PLACEHOLDER — ej., "Identificar la fuente de la filtración"]
2. [PLACEHOLDER — ej., "Medidas cautelares urgentes (art. 13 Ley 1/2019)"]
3. [PLACEHOLDER — ej., "Burofax de requerimiento al infractor"]
4. [PLACEHOLDER — ej., "Acción judicial por competencia desleal"]

---

## Open source — Política de uso

**Posición general:** [PLACEHOLDER — ej., "Uso permitido con aprobación previa; restricción de licencias copyleft en componentes distribuidos"]

**Licencias aceptables sin aprobación:** [PLACEHOLDER — ej., "MIT, BSD-2, BSD-3, Apache 2.0, ISC"]

**Licencias que requieren aprobación:** [PLACEHOLDER — ej., "LGPL, MPL 2.0, CDDL"]

**Licencias prohibidas:** [PLACEHOLDER — ej., "GPL v2/v3, AGPL, SSPL en cualquier componente que se distribuya o se ofrezca como servicio"]

**Proceso de aprobación:** [PLACEHOLDER — ej., "Solicitud a equipo legal con nombre del componente, licencia, uso previsto; respuesta en 48h"]

**Herramienta de escaneo:** [PLACEHOLDER — ej., "FOSSA / Snyk / escaneo manual"]

---

## Cláusulas de PI en contratos

### Cesión vs. licencia

**Posición house (como cedente/licenciante):** [PLACEHOLDER — ej., "Preferir licencia limitada; cesión solo si se paga precio separado por la PI"]

**Posición house (como cesionario/licenciatario):** [PLACEHOLDER — ej., "Exigir cesión plena para desarrollos a medida; licencia amplia para productos estándar"]

### Obra por encargo

**Posición house:** [PLACEHOLDER — ej., "Contrato escrito obligatorio (art. 43 LPI); especificar modalidades de explotación, ámbito territorial y temporal, remuneración proporcional si aplica"]

### Empleados (art. 51 LPI / art. 15 Ley de Patentes)

**Cláusula house en contratos de trabajo:** [PLACEHOLDER — ej., "Referencia expresa a art. 51 LPI para derechos de autor y art. 15 LP para invenciones laborales; compensación adicional para invenciones mixtas art. 17 LP"]

---

## Requerimientos extrajudiciales

**Formato:** [PLACEHOLDER — ej., "Burofax con acuse de recibo y certificación de contenido vía notario.es o Correos"]

**Estructura house del requerimiento:**
1. Identificación del requirente y sus derechos
2. Descripción de la infracción con pruebas
3. Fundamento jurídico (norma infringida)
4. Petición concreta (cesar, retirar, indemnizar)
5. Plazo para cumplimiento (habitualmente [PLACEHOLDER — ej., "15 días hábiles"])
6. Advertencia de acciones judiciales

**Aprobación necesaria:** [PLACEHOLDER — ej., "Todo burofax requiere aprobación del responsable de PI"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Junior/paralegal] | [PLACEHOLDER — ej., "Renovaciones rutinarias, vigilancia de marcas"] | [Abogado/a de PI] | [método] |
| [Abogado/a de PI] | [PLACEHOLDER — ej., "Oposiciones, registros nuevos, consultas de licencias"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Litigios de PI, enforcement contra terceros, acuerdos de licencia >€X"] | [Comité / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda demanda recibida, toda medida cautelar, negociación de patentes esenciales, licencias FRAND"]

---

## Estilo house

**Formato de informes de PI:** [PLACEHOLDER]
**Citas normativas:** [PLACEHOLDER — ej., "art. 34 Ley 17/2001, art. 1 LPI (RDLeg 1/1996), art. 52 Ley 24/2015"]
**Idioma:** [PLACEHOLDER — ej., "Español para registros OEPM; inglés para EUIPO y OMPI"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Ley de Marcas** (Ley 17/2001, de 7 de diciembre)
- **Ley de Patentes** (Ley 24/2015, de 24 de julio)
- **LPI** — Ley de Propiedad Intelectual (Real Decreto Legislativo 1/1996, de 12 de abril)
- **Ley de Secretos Empresariales** (Ley 1/2019, de 20 de febrero)
- **Ley de Diseño Industrial** (Ley 20/2003, de 7 de julio)
- **Reglamento de Marca de la UE** (Reglamento UE 2017/1001)
- **Reglamento de Diseño Comunitario** (Reglamento CE 6/2002)
- **Convenio de la Patente Europea** (CPE, Múnich 1973, revisado 2000)
- **Arreglo y Protocolo de Madrid** (marcas internacionales)
- **LCD** — Ley de Competencia Desleal (Ley 3/1991) — en lo relativo a actos de imitación y aprovechamiento de reputación ajena

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/propiedad-intelectual:entrevista-inicial --repetir`*
