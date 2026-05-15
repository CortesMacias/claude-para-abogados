<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /clinica-juridica:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu clínica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /clinica-juridica:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/clinica-juridica/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Clínica Jurídica

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/clinica-juridica:cold-start-interview`.*

---

## Quiénes somos

| Campo | Valor |
|---|---|
| Universidad | [PLACEHOLDER] |
| Facultad / Departamento | [PLACEHOLDER] |
| Nombre de la clínica | [PLACEHOLDER] |
| Director/a de la clínica | [PLACEHOLDER] |
| Supervisor/a académico/a | [PLACEHOLDER — nombre, área de especialización] |
| Abogado/a supervisor/a (colegiado/a) | [PLACEHOLDER — nombre, colegio, número de colegiado] |
| Curso académico | [PLACEHOLDER] |

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Estudiante de clínica | Supervisor/a académico/a | Abogado/a supervisor/a]
**Colegiación:** [PLACEHOLDER — Sí (número y colegio) / No (estudiante bajo supervisión)]

---

## Áreas de práctica de la clínica

| Área | Activa | Supervisor/a |
|---|---|---|
| [PLACEHOLDER — Extranjería] | | |
| [PLACEHOLDER — Consumo] | | |
| [PLACEHOLDER — Vivienda] | | |
| [PLACEHOLDER — Violencia de género] | | |
| [PLACEHOLDER — Derechos fundamentales] | | |
| [PLACEHOLDER — Otra] | | |

---

## Protocolo de intake

**Pasos del protocolo:**

1. **Recepción de la consulta** — Canal: [PLACEHOLDER — presencial, derivación de ONG, juzgado, colegio de abogados]
2. **Conflicto de intereses** — Verificación contra registro interno de clientes: [PLACEHOLDER — ruta/sistema]
3. **Evaluación de capacidad** — ¿La clínica tiene competencia para este asunto? Criterios: [PLACEHOLDER]
4. **Derivación a turno de oficio** — Si el asunto excede la capacidad de la clínica o requiere representación procesal que la clínica no puede asumir
5. **Apertura de expediente** — Registro: [PLACEHOLDER — sistema/carpeta]
6. **Firma de hoja de encargo** — Modelo: [PLACEHOLDER — ruta]
7. **Consentimiento informado** — El cliente entiende que le atienden estudiantes bajo supervisión

**Criterios de derivación:** [PLACEHOLDER — cuándo se deriva a turno de oficio, servicios sociales, o despacho externo]

---

## Justicia gratuita

*Ley 1/1996, de 10 de enero, de Asistencia Jurídica Gratuita.*

| Campo | Valor |
|---|---|
| Requisitos económicos | Ingresos inferiores a 2x IPREM (actualizar anualmente) |
| Documentación necesaria | [PLACEHOLDER — DNI/NIE, declaración de renta, certificado de empadronamiento, etc.] |
| Órgano de tramitación | Comisión de Asistencia Jurídica Gratuita de [PLACEHOLDER — provincia] |
| Formulario de solicitud | [PLACEHOLDER — ruta/modelo] |

**Supuestos de reconocimiento automático:** Víctimas de violencia de género, terrorismo, trata, menores, personas con discapacidad (art. 2 Ley 1/1996).

---

## Turno de oficio

| Campo | Valor |
|---|---|
| Colegio de Abogados de referencia | [PLACEHOLDER — ICAM, ICAB, etc.] |
| Protocolo de derivación | [PLACEHOLDER] |
| Contacto para designación de oficio | [PLACEHOLDER] |
| Sustitución de abogado de oficio | [PLACEHOLDER — procedimiento] |

*Referencia: art. 30-35 Ley 1/1996; Estatuto General de la Abogacía (RD 135/2021).*

---

## Estructura de memo — IRAC adaptado

Todo memo de la clínica sigue esta estructura:

1. **I — Identificación del problema:** Hechos relevantes y cuestión jurídica concreta
2. **R — Regulación aplicable:** Normas, jurisprudencia y doctrina aplicables (con citas completas)
3. **A — Aplicación al caso:** Subsunción de los hechos en la norma
4. **C — Conclusión:** Respuesta a la cuestión, opciones para el cliente, recomendación

**Formato de citas:**
- Legislación: Nombre completo + artículo (ej: "art. 1.902 del Código Civil")
- Jurisprudencia: Tribunal + Sala + fecha + ECLI si disponible (ej: "STS, Sala 1.a, de 15 de marzo de 2023, ECLI:ES:TS:2023:XXXX")
- Doctrina: Autor, título, editorial, año, página

**Plantilla de memo:** [PLACEHOLDER — ruta]

---

## Plazos y preclusión

**Sistema de alertas:** [PLACEHOLDER — calendario compartido, herramienta de gestión, manual]

| Tipo de plazo | Alerta previa | Responsable de control |
|---|---|---|
| Plazos procesales (LEC) | [PLACEHOLDER — días antes] | [PLACEHOLDER] |
| Prescripción y caducidad | [PLACEHOLDER] | [PLACEHOLDER] |
| Plazos administrativos (LPAC) | [PLACEHOLDER] | [PLACEHOLDER] |
| Citas y comparecencias | [PLACEHOLDER] | [PLACEHOLDER] |

**Regla de la clínica:** Ningún plazo se deja sin verificar por el supervisor antes de que transcurran 48 horas desde su identificación.

---

## Supervisión

**Workflow de revisión:**

1. Estudiante prepara borrador del memo/escrito
2. Revisión por compañero/a de clínica (peer review): [PLACEHOLDER — obligatorio/opcional]
3. Revisión por supervisor/a académico/a: [PLACEHOLDER — nombre]
4. Aprobación por abogado/a colegiado/a (si implica actuación procesal): [PLACEHOLDER — nombre]
5. Entrega/envío al cliente o presentación en juzgado/administración

**Plazo de revisión:** [PLACEHOLDER — días máximos entre borrador y aprobación]

---

## Correspondencia con cliente

**Plantillas disponibles:**

| Tipo | Ubicación |
|---|---|
| Citación para entrevista | [PLACEHOLDER] |
| Solicitud de documentos | [PLACEHOLDER] |
| Actualización de estado del caso | [PLACEHOLDER] |
| Comunicación de resultado | [PLACEHOLDER] |
| Cierre de expediente | [PLACEHOLDER] |

**Regla:** Toda comunicación con el cliente debe ser revisada por el supervisor antes de enviarla.

---

## Traspaso de semestre

**Protocolo de traspaso:**

Cuando un estudiante termina el semestre y el caso continúa:

1. **Memo de estado** — Resumen del caso, actuaciones realizadas, pendientes, plazos vivos
2. **Reunión de traspaso** — Con el estudiante entrante y el supervisor
3. **Actualización del expediente** — Documentos indexados, cronología actualizada
4. **Contacto con el cliente** — Comunicar el cambio de estudiante responsable

**Plantilla de memo de traspaso:** [PLACEHOLDER — ruta]

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Calendario compartido | [PLACEHOLDER] | Control manual de plazos |
| Tareas programadas | [PLACEHOLDER] | Revisiones bajo demanda |

*Re-comprobar: `/clinica-juridica:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan memos, escritos, correspondencia]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo]

**Cabecera de trabajo:**

`TRABAJO DE CLÍNICA JURÍDICA — [UNIVERSIDAD] — PREPARADO BAJO SUPERVISIÓN ACADÉMICA Y LETRADA — NO CONSTITUYE ASESORAMIENTO PROFESIONAL INDEPENDIENTE`

*Nota: Los trabajos de la clínica están supervisados por un abogado colegiado, pero el estudiante
no actúa como abogado. La cabecera refleja esta realidad.*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Ley de Asistencia Jurídica Gratuita | Ley 1/1996, de 10 de enero | Justicia gratuita, turno de oficio |
| LOPJ | LO 6/1985 | Organización del poder judicial |
| Estatuto General de la Abogacía | RD 135/2021, de 2 de marzo | Ejercicio de la abogacía, turno de oficio |
| LEC | Ley 1/2000 | Plazos procesales civiles |
| LPAC | Ley 39/2015 | Procedimiento administrativo común |

---

*Re-ejecutar: `/clinica-juridica:cold-start-interview --redo`*
