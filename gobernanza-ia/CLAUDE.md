<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /gobernanza-ia:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /gobernanza-ia:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/gobernanza-ia/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Gobernanza de Inteligencia Artificial
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/gobernanza-ia:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de gobernanza de IA se quedan aquí.*

[Empresa] es una [tipo de entidad]. Nuestro rol respecto a sistemas de IA es [proveedor / implementador / importador / distribuidor / usuario / combinación].
Desarrollamos o usamos [N] sistemas de IA. El equipo de gobernanza de IA cuenta con [N] personas.
[Responsable de IA / DPO / Comité de IA: nombre o ninguno]. La escalación va a [nombre].

**Huella regulatoria IA:** [PLACEHOLDER — Reglamento IA (UE), RGPD art. 22, normativa sectorial específica] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos abiertos de gobernanza IA:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Empresa tecnológica] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Slack / Teams | [PLACEHOLDER ✓/✗] | Alertas entregadas inline |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Revisiones solo bajo demanda |
| Registro de sistemas de IA (interno) | [PLACEHOLDER ✓/✗] | Registro manual en hoja de cálculo |

*Re-comprobar: `/gobernanza-ia:entrevista-inicial --check-integraciones`*

---

## Registro de sistemas de IA

| Sistema | Proveedor | Propósito | Categoría de riesgo | Estado | Responsable interno |
|---|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — inaceptable/alto/limitado/mínimo] | [PLACEHOLDER — activo/desarrollo/retirado] | [PLACEHOLDER] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Criterios para inclusión en el registro:** [PLACEHOLDER — qué se considera "sistema de IA" a efectos internos]
**Frecuencia de actualización:** [PLACEHOLDER — trimestral / semestral / ante cambio material]

---

## Clasificación de riesgo según Reglamento IA (UE 2024/1689)

| Categoría | Definición resumida | Sistemas propios afectados | Acción requerida |
|---|---|---|---|
| Inaceptable (art. 5) | Prácticas prohibidas: scoring social, manipulación subliminal, explotación de vulnerabilidades, identificación biométrica en tiempo real (con excepciones) | [PLACEHOLDER] | Prohibición absoluta — retirada inmediata |
| Alto riesgo (Anexo III) | Biometría, infraestructuras críticas, educación, empleo, servicios esenciales, law enforcement, migración, justicia | [PLACEHOLDER] | Sistema de gestión de riesgos, datos de entrenamiento, transparencia, supervisión humana, registro |
| Limitado (art. 50) | Chatbots, deepfakes, generación de contenido | [PLACEHOLDER] | Obligaciones de transparencia |
| Mínimo | Todo lo demás | [PLACEHOLDER] | Códigos de conducta voluntarios |

**Sistemas de IA de propósito general (GPAI):** [PLACEHOLDER — si usamos o desarrollamos modelos GPAI, clasificación de riesgo sistémico]

---

## Evaluaciones de impacto de IA

**Cuándo es obligatoria:** [PLACEHOLDER — sistemas de alto riesgo, decisiones automatizadas art. 22 RGPD, evaluaciones de impacto en derechos fundamentales art. 27 Reglamento IA]

| Evaluación | Sistema | Fecha | Resultado | Próxima revisión |
|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Formato estándar:** [PLACEHOLDER — plantilla interna, formato AESIA, otro]
**Aprobación:** [PLACEHOLDER — quién firma la evaluación de impacto]

---

## Proveedores de IA — Cláusulas clave

| Cláusula | Nuestra posición estándar | Aceptable | Nunca aceptar |
|---|---|---|---|
| Entrenamiento con nuestros datos | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Responsabilidad por resultados del modelo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Cambio de modelo sin aviso | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| SLAs de disponibilidad y latencia | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Auditoría del sistema | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Subprocesamiento / subcontratación | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Propiedad intelectual de outputs | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Localización de datos y procesamiento | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Línea roja contractual:** [PLACEHOLDER — la cláusula que rompe el acuerdo]

---

## Transparencia y explicabilidad

**Política de transparencia:** [PLACEHOLDER — cómo informamos a los usuarios de que interactúan con IA]
**Obligaciones art. 50 Reglamento IA:** [PLACEHOLDER — etiquetado de contenido generado, notificación de chatbots]
**Mecanismo de explicabilidad:** [PLACEHOLDER — cómo explicamos las decisiones automatizadas a los afectados]
**Derecho de oposición a decisiones automatizadas (art. 22 RGPD):** [PLACEHOLDER — proceso implementado]

---

## Supervisión humana

**Política de human-in-the-loop:** [PLACEHOLDER — en qué decisiones se requiere intervención humana]
**Niveles de automatización:** [PLACEHOLDER — totalmente automatizado / semiautomatizado / asistido]
**Mecanismo de override:** [PLACEHOLDER — cómo un humano puede anular la decisión del sistema]
**Registro de intervenciones:** [PLACEHOLDER — dónde se documentan las intervenciones humanas]

---

## Sandbox regulatorio — AESIA

**Participación en sandbox AESIA:** [PLACEHOLDER — sí/no/en evaluación]
**Sistemas candidatos:** [PLACEHOLDER]
**Estado de solicitud:** [PLACEHOLDER]
**Contacto AESIA:** [PLACEHOLDER]

*La Agencia Española de Supervisión de la Inteligencia Artificial (AESIA) es la autoridad nacional de supervisión del Reglamento IA.*

---

## Política interna de uso de IA generativa

**Existe política aprobada:** [PLACEHOLDER — sí/no/en borrador]
**Ubicación:** [PLACEHOLDER]
**Alcance:** [PLACEHOLDER — toda la organización / departamentos específicos]
**Usos permitidos:** [PLACEHOLDER]
**Usos prohibidos:** [PLACEHOLDER]
**Datos que no se pueden introducir en herramientas de IA:** [PLACEHOLDER — datos personales, secretos empresariales, información confidencial de clientes]
**Revisión y aprobación de outputs:** [PLACEHOLDER — qué requiere revisión humana antes de uso externo]
**Formación:** [PLACEHOLDER — programa de formación en uso responsable de IA]

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Clasificación de nuevo sistema de IA | Equipo de gobernanza IA | — | — |
| Sistema clasificado como alto riesgo | — | Dirección jurídica + Comité de IA | Siempre |
| Incidente de IA (sesgo, error material, daño) | — | DPO + Dirección jurídica + Dirección | Siempre |
| Requerimiento de AESIA u otro supervisor | — | Dirección jurídica + Dirección General | Siempre |
| Nuevo proveedor de IA con acceso a datos | Equipo de gobernanza IA | DPO | Si datos personales |

---

## Referencias legislativas principales

- **Reglamento IA** — Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo (Ley de Inteligencia Artificial)
- **Directiva de responsabilidad por IA** — Propuesta de Directiva sobre responsabilidad en materia de IA
- **RGPD** — Reglamento (UE) 2016/679, en particular art. 22 (decisiones individuales automatizadas)
- **LOPDGDD** — Ley Orgánica 3/2018, de Protección de Datos y Garantía de los Derechos Digitales
- **Sandbox AESIA** — Real Decreto 817/2023 que establece un entorno controlado de pruebas
- **Directiva de responsabilidad por productos defectuosos** — Directiva (UE) 2024/2853 (incluye software y IA)

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Registro de sistemas de IA | [PLACEHOLDER] | [PLACEHOLDER] | |
| Política de uso de IA generativa | [PLACEHOLDER] | [PLACEHOLDER] | |
| Evaluación de impacto de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan evaluaciones de impacto, revisiones de proveedores y análisis de clasificación]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/gobernanza-ia:entrevista-inicial --redo`*
