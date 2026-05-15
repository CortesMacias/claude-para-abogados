<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /startups:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu situación."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /startups:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/startups/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Startups

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/startups:cold-start-interview`.*

---

## Quiénes somos

*El nombre de la empresa, sector, tamaño y jurisdicciones vienen de `perfil-empresa.md` — edita allí
para cambiar en todos los plugins. Los campos específicos de startups van aquí.*

[Empresa] es una startup en fase [PLACEHOLDER — ideación / pre-seed / seed / serie A / growth].
Sector: [PLACEHOLDER]. Fundadores: [PLACEHOLDER — nombres]. Sede social: [PLACEHOLDER — provincia].

**Entorno de práctica:** [PLACEHOLDER — Fundador sin abogado | Fundador con abogado externo | Abogado de startup | Despacho especializado en startups]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Fundador/a con acceso a abogado | Fundador/a sin acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / despacho / N/A si es abogado]

---

## Fase de la startup

| Campo | Valor |
|---|---|
| Fase actual | [PLACEHOLDER — Ideación / Pre-seed / Seed / Serie A / Growth] |
| Fecha de constitución | [PLACEHOLDER — o "pendiente"] |
| Empleados | [PLACEHOLDER] |
| Facturación último ejercicio | [PLACEHOLDER — o "pre-revenue"] |
| Condición de empresa emergente (Ley de Startups) | [PLACEHOLDER — Sí/No/Pendiente de certificación] |

---

## Constitución

| Campo | Valor |
|---|---|
| Forma jurídica | [PLACEHOLDER — SL / SL de formación sucesiva / pendiente] |
| Capital social | [PLACEHOLDER — mínimo 1 EUR formación sucesiva, 3.000 EUR SL ordinaria] |
| Estatutos | [PLACEHOLDER — estándar CIRCE / personalizados / ruta al documento] |
| Objeto social | [PLACEHOLDER] |
| PAC digital (Portal de Acceso a la Creación) | [PLACEHOLDER — utilizado Sí/No] |
| Certificación negativa RMNC | [PLACEHOLDER — obtenida Sí/No, fecha] |
| Notaría | [PLACEHOLDER] |
| Inscripción en el Registro Mercantil | [PLACEHOLDER — completada Sí/No, tomo/folio/hoja] |

*Referencia: arts. 1-27 LSC (Real Decreto Legislativo 1/2010); Ley 18/2022 de creación y crecimiento de empresas.*

---

## Pacto de socios

| Cláusula | Incluida | Detalle |
|---|---|---|
| Vesting | [PLACEHOLDER] | [PLACEHOLDER — periodo, cliff, aceleración] |
| Good/bad leaver | [PLACEHOLDER] | [PLACEHOLDER — valoración en cada caso] |
| Arrastre (drag-along) | [PLACEHOLDER] | [PLACEHOLDER — umbrales] |
| Acompañamiento (tag-along) | [PLACEHOLDER] | |
| Anti-dilución | [PLACEHOLDER] | [PLACEHOLDER — full ratchet / weighted average] |
| Derecho de adquisición preferente | [PLACEHOLDER] | |
| Bloqueo (lock-up) | [PLACEHOLDER] | [PLACEHOLDER — periodo] |
| Deadlock | [PLACEHOLDER] | [PLACEHOLDER — mecanismo de resolución] |
| No competencia | [PLACEHOLDER] | [PLACEHOLDER — duración, ámbito] |

**Ubicación del pacto:** [PLACEHOLDER — ruta al documento]

---

## Equity e incentivos

| Mecanismo | Estado | Detalle |
|---|---|---|
| Stock options | [PLACEHOLDER] | [PLACEHOLDER — plan aprobado, beneficiarios, precio de ejercicio] |
| Phantom shares | [PLACEHOLDER] | |
| Carried interest | [PLACEHOLDER] | |

**Régimen fiscal stock options — Ley de Startups (art. 13 Ley 28/2022):**
- Exención hasta 50.000 EUR/año (empresas emergentes certificadas)
- Diferimiento: tributación en el momento de la venta de las acciones, no del ejercicio
- [PLACEHOLDER — aplicabilidad a nuestra empresa: Sí/No, certificación ENISA obtenida]

*Referencia: art. 13 Ley 28/2022 (Ley de Startups); art. 42.3.f) LIRPF.*

---

## Rondas de inversión

| Ronda | Estado | Importe | Valoración | Instrumento |
|---|---|---|---|---|
| [PLACEHOLDER] | | | | [PLACEHOLDER — equity, nota convertible, SAFE] |

**Documentos tipo:**

| Documento | Ubicación | Notas |
|---|---|---|
| Term sheet modelo | [PLACEHOLDER] | |
| SHA (Shareholders Agreement) | [PLACEHOLDER] | |
| Nota convertible | [PLACEHOLDER] | |
| SAFE adaptado | [PLACEHOLDER] | |

**Cap table:** [PLACEHOLDER — ruta a la cap table actualizada o herramienta utilizada]

---

## Incentivos fiscales

| Incentivo | Aplicable | Detalle |
|---|---|---|
| Tipo reducido IS (15% primeros ejercicios) | [PLACEHOLDER] | Art. 29 LIS |
| Tipo reducido IS empresa emergente (15%, 4 ejercicios) | [PLACEHOLDER] | Art. 7 Ley 28/2022 |
| Deducción por inversión en empresa nueva | [PLACEHOLDER] | Art. 68.1 LIRPF (30%, base máx. 100.000 EUR para empresas emergentes) |
| Diferimiento stock options empleados | [PLACEHOLDER] | Art. 13 Ley 28/2022 |
| Deducción I+D+i | [PLACEHOLDER] | Arts. 35-36 LIS |
| Certificación empresa emergente ENISA | [PLACEHOLDER — solicitada / obtenida / no aplica] | |

*Referencia: Ley 28/2022 (Ley de Startups); LIRPF; LIS.*

---

## Primeras contrataciones

| Campo | Valor |
|---|---|
| Plantilla actual | [PLACEHOLDER] |
| Convenio colectivo aplicable | [PLACEHOLDER — convenio TIC, oficinas, etc.] |
| Tipos de contrato usados | [PLACEHOLDER — indefinido, temporal, formación] |
| Becarios/prácticas | [PLACEHOLDER — convenio con universidad, Sí/No] |
| Autónomos/freelance | [PLACEHOLDER — falsos autónomos: riesgo evaluado Sí/No] |
| Teletrabajo | [PLACEHOLDER — acuerdo de trabajo a distancia firmado] |

*Referencia: ET (RDLeg 2/2015); Ley 10/2021 de trabajo a distancia; RD 1493/2011 (prácticas).*

---

## Propiedad intelectual para startups

| Campo | Valor |
|---|---|
| Titularidad del código | [PLACEHOLDER — cesión de empleados art. 97.4 LPI, cesión de autónomos] |
| Contratos de cesión IP firmados | [PLACEHOLDER] |
| NDAs modelo | [PLACEHOLDER — ruta] |
| Marcas registradas | [PLACEHOLDER — OEPM/EUIPO] |
| Dominios | [PLACEHOLDER] |

*Referencia: arts. 97-100 LPI (RDLeg 1/1996); Ley 17/2001 de Marcas.*

---

## Protección de datos para startups

**Mínimo viable de compliance:**

| Elemento | Estado |
|---|---|
| Política de privacidad publicada | [PLACEHOLDER] |
| Registro de actividades de tratamiento | [PLACEHOLDER] |
| Base jurídica identificada por tratamiento | [PLACEHOLDER] |
| Consentimiento para cookies (LSSI-CE) | [PLACEHOLDER] |
| Contrato de encargado con proveedores clave | [PLACEHOLDER] |
| Cláusulas informativas en formularios | [PLACEHOLDER] |

*Referencia: RGPD (2016/679); LOPDGDD (LO 3/2018); LSSI-CE (Ley 34/2002).*

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Slack / Teams | [PLACEHOLDER] | Notificaciones entregadas inline |
| Tareas programadas | [PLACEHOLDER] | Revisiones bajo demanda |

*Re-comprobar: `/startups:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan pactos, actas, informes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Cabecera de trabajo:**

- Si el Rol es Abogado/a: `CONFIDENCIAL — TRABAJO PROFESIONAL — PREPARADO BAJO DIRECCIÓN LETRADA`
- Si el Rol es Fundador/a o no jurista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON ABOGADO ANTES DE ACTUAR`

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Ley de Startups | Ley 28/2022, de 21 de diciembre | Empresa emergente, incentivos fiscales, stock options |
| LSC | RDLeg 1/2010 | Sociedades de capital (SL) |
| LIRPF | Ley 35/2006 | Deducción inversión empresa nueva (art. 68.1) |
| LIS | Ley 27/2014 | Tipo reducido, deducciones I+D+i |
| ET | RDLeg 2/2015 | Estatuto de los Trabajadores |
| LPI | RDLeg 1/1996 | Propiedad intelectual (cesión código) |

---

*Re-ejecutar: `/startups:cold-start-interview --redo`*
