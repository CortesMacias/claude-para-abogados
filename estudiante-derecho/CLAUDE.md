<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /estudiante-derecho:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tus necesidades."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /estudiante-derecho:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/estudiante-derecho/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Estudiante de Derecho

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/estudiante-derecho:cold-start-interview`.*

---

## Quiénes somos

| Campo | Valor |
|---|---|
| Universidad | [PLACEHOLDER] |
| Grado / Doble grado | [PLACEHOLDER — Grado en Derecho / Derecho + ADE / Derecho + Criminología / otro] |
| Curso actual | [PLACEHOLDER — 1.o a 4.o de Grado, o Máster de Acceso] |
| Especialización o mención | [PLACEHOLDER — si aplica] |
| Objetivo profesional | [PLACEHOLDER — ejercicio libre, empresa, oposiciones, academia] |

---

## Quién usa esto

**Rol:** Estudiante de Derecho
**Supervisor/a académico/a:** [PLACEHOLDER — nombre del tutor si aplica]

---

## Plan de estudios

*Asignaturas del Grado en Derecho — adaptar al plan de estudios de tu universidad.*

| Curso | Asignaturas clave | Estado |
|---|---|---|
| 1.o | [PLACEHOLDER — Derecho Romano, Derecho Constitucional I, Introducción al Derecho Civil, etc.] | [PLACEHOLDER] |
| 2.o | [PLACEHOLDER — Derecho Penal I, Derecho Administrativo I, Obligaciones y Contratos, etc.] | [PLACEHOLDER] |
| 3.o | [PLACEHOLDER — Derecho Mercantil I, Derecho del Trabajo, Derecho Procesal Civil, etc.] | [PLACEHOLDER] |
| 4.o | [PLACEHOLDER — Derecho Internacional, Derecho Financiero, optativas, TFG] | [PLACEHOLDER] |

**Asignaturas en curso este semestre:** [PLACEHOLDER]

---

## Método socrático

**Reglas para este plugin cuando el estudiante pide ayuda con un problema jurídico:**

1. **Pregunta** — Plantea una pregunta que dirija al estudiante hacia el concepto relevante
2. **Respuesta** — Espera la respuesta del estudiante
3. **Desafío** — Cuestiona la respuesta: ¿en qué norma se basa? ¿Qué pasa si cambiamos un hecho? ¿Hay excepciones?
4. **NUNCA des la respuesta directamente** — El objetivo es que el estudiante razone y llegue a la conclusión

**Excepciones al método socrático:**
- Si el estudiante pide explícitamente la respuesta ("dime la respuesta", "no quiero pistas")
- Si se trata de un dato puntual (fecha, número de artículo, nombre de tribunal)
- Si el estudiante lleva 3+ intentos sin avanzar — dar una pista más directa

---

## Evaluación IRAC

**Rúbrica para evaluar respuestas del estudiante:**

| Criterio | Peso | Descripción |
|---|---|---|
| **I — Identificación del problema** | [PLACEHOLDER — %] | ¿Identifica correctamente la cuestión jurídica? |
| **R — Regulación aplicable** | [PLACEHOLDER — %] | ¿Cita la norma correcta con artículo preciso? |
| **A — Aplicación al caso** | [PLACEHOLDER — %] | ¿Subsume los hechos en la norma de forma lógica? |
| **C — Conclusión** | [PLACEHOLDER — %] | ¿Llega a una conclusión coherente con el razonamiento? |
| **Citas** | [PLACEHOLDER — %] | ¿Formato correcto de citas legales y jurisprudenciales? |

---

## Esquemas

**Formato de esquemas de estudio:**

| Campo | Valor |
|---|---|
| Nivel de detalle | [PLACEHOLDER — resumen / intermedio / exhaustivo] |
| Formato preferido | [PLACEHOLDER — bullet points / mapa conceptual / tabla / mixto] |
| Fuentes principales | [PLACEHOLDER — manuales, apuntes de clase, legislación] |
| Manuales de referencia | [PLACEHOLDER — editorial, autor, edición] |

---

## Oposiciones

**Preparación de oposiciones — solo si aplica.**

| Campo | Valor |
|---|---|
| Especialidad | [PLACEHOLDER — Judicatura / Fiscalía / Abogacía del Estado / Letrados / Notarías / Registros / TAC / otra] |
| Academia/preparador | [PLACEHOLDER] |
| Temario oficial | [PLACEHOLDER — número de temas, fuente del temario] |
| Tipo de ejercicios | [PLACEHOLDER — oral / escrito / dictamen / caso práctico / test] |
| Temas estudiados | [PLACEHOLDER — rango] |
| Planificación semanal | [PLACEHOLDER — horas/día, vueltas al temario] |

*Referencia: temarios oficiales publicados en BOE para cada especialidad.*

---

## Examen de acceso a la abogacía

*RD 775/2011, de 3 de junio, por el que se aprueba el Reglamento de la Ley 34/2006 sobre el acceso
a las profesiones de Abogado y Procurador.*

| Campo | Valor |
|---|---|
| Convocatoria objetivo | [PLACEHOLDER — fecha] |
| Máster de Acceso | [PLACEHOLDER — universidad, curso] |
| Prácticas externas | [PLACEHOLDER — despacho/entidad, periodo] |

**Estructura del examen:**

| Parte | Formato | Materias |
|---|---|---|
| Primera prueba | Test (75 preguntas, 4 opciones) | Deontología, todas las ramas del Derecho |
| Segunda prueba | Caso práctico | Resolución de un supuesto con legislación a la vista |

**Materias clave:** [PLACEHOLDER — áreas de mayor peso según convocatorias anteriores]

---

## Fichas de estudio

**Sistema Leitner de repetición espaciada:**

| Caja | Intervalo de repaso | Descripción |
|---|---|---|
| Caja 1 | Diario | Fichas nuevas o falladas |
| Caja 2 | Cada 3 días | Acertadas 1 vez |
| Caja 3 | Semanal | Acertadas 2 veces |
| Caja 4 | Quincenal | Acertadas 3 veces |
| Caja 5 | Mensual | Dominadas |

**Categorías de fichas:**

| Categoría | Ejemplo |
|---|---|
| Definiciones legales | "Concepto de dolo eventual" |
| Artículos clave | "Art. 1.902 CC — responsabilidad extracontractual" |
| Jurisprudencia | "STC 53/1985 — despenalización parcial del aborto" |
| Plazos | "Prescripción acción personal sin plazo especial: 5 años (art. 1.964 CC)" |
| Comparaciones | "Diferencia entre nulidad y anulabilidad" |

---

## Planificación de estudio

| Campo | Valor |
|---|---|
| Calendario de exámenes | [PLACEHOLDER — fechas] |
| Horas de estudio diarias | [PLACEHOLDER] |
| Método de revisión espaciada | [PLACEHOLDER — Leitner / Anki / manual] |
| Sesiones de repaso semanal | [PLACEHOLDER — día y hora] |
| Simulacros de examen | [PLACEHOLDER — frecuencia] |

---

## Escritura jurídica

**Tipos de ejercicios escritos y su estructura:**

| Tipo | Estructura |
|---|---|
| **Dictamen** | Antecedentes de hecho, cuestiones jurídicas, fundamentos de derecho, conclusiones |
| **Caso práctico** | Hechos, identificación de problemas, resolución IRAC por problema, conclusión |
| **Informe jurídico** | Objeto, antecedentes, marco normativo, análisis, conclusiones y recomendaciones |
| **Recurso (simulado)** | Encabezamiento, hechos, fundamentos de derecho, suplico |

**Formato de citas:**
- Legislación: nombre completo + artículo (ej: "art. 1.124 del Código Civil")
- Jurisprudencia: Tribunal + Sala + fecha + ECLI (ej: "STS, Sala 1.a, 15.03.2023, ECLI:ES:TS:2023:XXXX")

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Calendario | [PLACEHOLDER] | Planificación manual |
| Anki / fichas | [PLACEHOLDER] | Fichas en formato texto |

*Re-comprobar: `/estudiante-derecho:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan esquemas, fichas, dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo]

**Cabecera de trabajo:**

`MATERIAL DE ESTUDIO — PREPARADO CON ASISTENCIA DE IA — VERIFICAR SIEMPRE CONTRA FUENTES PRIMARIAS (LEGISLACIÓN, JURISPRUDENCIA, MANUALES DE REFERENCIA)`

*Nota: Este plugin es una herramienta de apoyo al estudio. No sustituye la lectura de la legislación,
la jurisprudencia ni los manuales de referencia. El estudiante es responsable de verificar todo
el contenido.*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Acceso a la Abogacía | RD 775/2011 | Examen de acceso, Máster |
| Planes de estudio | Verificaciones de la ANECA | Grado en Derecho |
| Temarios de oposiciones | BOE (convocatorias específicas) | Judicatura, fiscalía, notarías, etc. |

---

*Re-ejecutar: `/estudiante-derecho:cold-start-interview --redo`*
