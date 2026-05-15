<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /societario:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /societario:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/societario/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis, vuestra postura de riesgo, personas clave) se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Societario

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/societario:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad / despacho]. El equipo de derecho societario lo forman [N] personas. [Nombre del socio/a responsable] es el punto final de escalado. Gestionamos aproximadamente [N] operaciones/consultas societarias al mes. Usamos [herramienta de gestión de entidades] para el seguimiento de obligaciones registrales.

*(Nombre de empresa, tipo de entidad, sector y tamaño proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública/clínica jurídica]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a colegiado/a | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Áreas de práctica activas

| Área | Estado | Responsable |
|---|---|---|
| M&A (fusiones y adquisiciones) | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Secretaría del Consejo / Junta | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Cumplimiento registral | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Gestión de entidades (grupo) | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Reestructuraciones societarias | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Capital riesgo / financiación | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |

---

## Due diligence — Checklist por categoría

*Checklist estándar para operaciones de M&A. Adaptar según tipo y tamaño de la operación.*

### Societario

- [ ] Escritura de constitución y estatutos vigentes
- [ ] Certificaciones registrales actualizadas (Registro Mercantil)
- [ ] Libro registro de socios / accionistas
- [ ] Actas de juntas generales (últimos [N] años)
- [ ] Actas del consejo de administración (últimos [N] años)
- [ ] Poderes vigentes y revocados
- [ ] Pactos parasociales / pactos de socios
- [ ] Estructura del grupo (organigrama societario)
- [ ] Participaciones en otras sociedades
- [ ] [PLACEHOLDER — ítems adicionales específicos del despacho/empresa]

### Contratos

- [ ] Contratos materiales vigentes (>€[PLACEHOLDER] de valor)
- [ ] Cláusulas de cambio de control
- [ ] Contratos con partes vinculadas (art. 231 LSC)
- [ ] Contratos de financiación y garantías
- [ ] [PLACEHOLDER]

### Laboral

- [ ] Convenio colectivo aplicable
- [ ] Plantilla y categorías profesionales
- [ ] Contratos de alta dirección
- [ ] Litigios laborales pendientes
- [ ] Plan de igualdad (obligatorio >50 trabajadores)
- [ ] [PLACEHOLDER]

### Fiscal

- [ ] Declaraciones de los últimos [N] ejercicios (IS, IVA, IRPF)
- [ ] Actas de inspección y comprobaciones
- [ ] Bases imponibles negativas pendientes de compensar
- [ ] Operaciones vinculadas (documentación de precios de transferencia)
- [ ] [PLACEHOLDER]

### Regulatorio

- [ ] Licencias y autorizaciones administrativas
- [ ] Cumplimiento sectorial específico
- [ ] [PLACEHOLDER]

### Litigios

- [ ] Procedimientos judiciales activos
- [ ] Procedimientos arbitrales
- [ ] Reclamaciones administrativas
- [ ] Contingencias no provisionadas
- [ ] [PLACEHOLDER]

### Propiedad intelectual e industrial

- [ ] Marcas registradas y solicitudes pendientes
- [ ] Patentes y modelos de utilidad
- [ ] Nombres de dominio
- [ ] Contratos de licencia de PI
- [ ] [PLACEHOLDER]

### Inmobiliario

- [ ] Inmuebles en propiedad (notas simples actualizadas)
- [ ] Contratos de arrendamiento
- [ ] Licencias urbanísticas y de actividad
- [ ] [PLACEHOLDER]

---

## Gobierno corporativo

### Tipos de acuerdos

**Junta General:**
- [PLACEHOLDER — ej., "Ordinaria anual (aprobación CCAA, aplicación resultado, gestión social), Extraordinaria (modificación estatutos, ampliación/reducción capital, transformación, fusión, escisión)"]

**Consejo de Administración / Órgano de administración:**
- [PLACEHOLDER — ej., "Administrador único / Administradores mancomunados / Consejo de administración — frecuencia de reuniones, quórum, sistema de voto"]

### Libro de actas

**Formato:** [PLACEHOLDER — ej., "Libro encuadernado legalizado en el Registro Mercantil / formato electrónico con firma digital"]
**Responsable de custodia:** [PLACEHOLDER]
**Legalización:** [PLACEHOLDER — ej., "Presentación telemática al Registro Mercantil dentro de los 4 meses siguientes al cierre del ejercicio"]

### Certificaciones

**Modelo house de certificación del secretario:** [PLACEHOLDER — ej., "Certificación del acta con transcripción literal del acuerdo, datos de asistencia, quórum"]
**Certificaciones registrales habituales:** [PLACEHOLDER — ej., "Certificación de cargos vigentes, certificación de titularidad"]

---

## Cumplimiento registral — Plazos y obligaciones

| Obligación | Plazo legal | Alerta interna | Referencia |
|---|---|---|---|
| Cuentas anuales — formulación | 3 meses desde cierre (art. 253 LSC) | [PLACEHOLDER] | Art. 253 LSC |
| Cuentas anuales — aprobación en Junta | 6 meses desde cierre (art. 164 LSC) | [PLACEHOLDER] | Art. 164 LSC |
| Cuentas anuales — depósito en RM | 1 mes desde aprobación (art. 279 LSC) | [PLACEHOLDER] | Art. 279 LSC |
| Legalización de libros | 4 meses desde cierre del ejercicio | [PLACEHOLDER] | Art. 18 CdC |
| Inscripción de nombramientos/ceses | 10 días desde otorgamiento escritura | [PLACEHOLDER] | Art. 94 RRM |
| Declaración de titulares reales | Según normativa antiblanqueo vigente | [PLACEHOLDER] | Ley 10/2010 |
| [PLACEHOLDER — otras obligaciones periódicas] | | | |

**Consecuencias del incumplimiento:**
- Cierre de la hoja registral por falta de depósito de CCAA (art. 282 LSC)
- Sanciones por falta de depósito (art. 283 LSC): multa de 1.200€ a 60.000€ (hasta 300.000€ si facturación >6M€)
- Responsabilidad de administradores por incumplimiento de deberes (arts. 236-241 LSC)

---

## Tipos societarios — Referencia rápida

| Tipo | Capital mínimo | Norma principal | Notas |
|---|---|---|---|
| SL (Sociedad Limitada) | 1€ (desde reforma 2022) | Arts. 1-40 LSC | Tipo más común; restricciones a transmisión de participaciones |
| SA (Sociedad Anónima) | 60.000€ | Arts. 1-40 LSC | Necesaria para cotización; acciones libremente transmisibles |
| SLP (Sociedad Limitada Profesional) | 1€ | Ley 2/2007 | Para ejercicio colectivo de profesiones colegiadas |
| SC (Sociedad Civil) | Sin mínimo | Arts. 1665-1708 CC | Personalidad jurídica si pactos públicos |
| Cooperativa | Según ley autonómica | Ley 27/1999 (estatal) | Legislación autonómica prevalente |
| SAU/SLU (Unipersonal) | Según tipo base | Art. 12-17 LSC | Obligación de inscribir unipersonalidad |

**Tipo societario del cliente / entidades del grupo:**
- [PLACEHOLDER — listar cada entidad con su tipo, CIF, Registro Mercantil de inscripción]

---

## Operaciones M&A — Posiciones estándar

**Tipo de operaciones habituales:** [PLACEHOLDER — ej., "Compraventas de participaciones, fusiones por absorción, escisiones"]

**Posición en representaciones y garantías (R&W):**
- [PLACEHOLDER — ej., "Exigir catálogo completo; limitar temporalmente a 2 años (3 para fiscal y laboral); cap al precio de compra"]

**Cláusula de ajuste de precio:** [PLACEHOLDER — ej., "Locked box vs. completion accounts — preferencia"]

**Cláusula de no competencia:** [PLACEHOLDER — ej., "Duración máxima 2 años; ámbito geográfico acotado a España/UE"]

**Indemnización:** [PLACEHOLDER — ej., "Basket/de minimis, cap global, supervivencia de reclamaciones"]

**Condiciones suspensivas habituales:** [PLACEHOLDER — ej., "Due diligence satisfactoria, autorizaciones regulatorias, renuncia a derechos de adquisición preferente"]

---

## Pactos de socios — Cláusulas clave

- **Derecho de acompañamiento (tag-along):** [PLACEHOLDER]
- **Derecho de arrastre (drag-along):** [PLACEHOLDER]
- **Derecho de adquisición preferente:** [PLACEHOLDER]
- **Cláusulas antidilución:** [PLACEHOLDER]
- **Governance / composición del órgano de administración:** [PLACEHOLDER]
- **Materias reservadas:** [PLACEHOLDER — ej., "Operaciones >€X, endeudamiento >€Y, contratación de directivos clave"]
- **Deadlock y mecanismos de resolución:** [PLACEHOLDER — ej., "Mediación → arbitraje; put/call de última oferta"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Junior/paralegal] | [PLACEHOLDER — ej., "Certificaciones rutinarias, legalizaciones"] | [Abogado/a senior] | [método] |
| [Abogado/a senior] | [PLACEHOLDER — ej., "Operaciones <€500K, juntas ordinarias"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Operaciones <€5M"] | [Comité de dirección / cliente] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Cualquier operación de M&A, modificaciones estructurales, operaciones con partes vinculadas art. 231 LSC"]

---

## Estilo house

**Formato de escrituras y actas:** [PLACEHOLDER — ej., "Seguir modelo del despacho; siempre incluir datos de inscripción registral"]
**Formato de informes de due diligence:** [PLACEHOLDER — ej., "Resumen ejecutivo + hallazgos por categoría con semáforo + anexos documentales"]
**Citas normativas:** [PLACEHOLDER — ej., "art. 160 LSC, art. 234 RRM, DA 3ª LME"]
**Idioma:** [PLACEHOLDER — ej., "Español; documentos bilingües para operaciones internacionales"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **LSC** — Ley de Sociedades de Capital (Real Decreto Legislativo 1/2010, de 2 de julio)
- **RRM** — Reglamento del Registro Mercantil (RD 1784/1996, de 19 de julio)
- **LME** — Ley de Modificaciones Estructurales de las Sociedades Mercantiles (Ley 3/2009, de 3 de abril; reformada por RDL 5/2023)
- **Código de Comercio** (Real Decreto de 22 de agosto de 1885)
- **Código Civil** — en lo relativo a obligaciones, contratos y personalidad jurídica
- **Ley 2/2007** de Sociedades Profesionales
- **Ley 27/1999** de Cooperativas (estatal)
- **Ley 10/2010** de prevención del blanqueo de capitales — titularidad real
- **Ley 5/2021** de modificación de la LSC para el fomento de la implicación de los accionistas (sociedades cotizadas)

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio jurídico subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea específica con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/societario:entrevista-inicial --repetir`*
