<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /proteccion-datos:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /proteccion-datos:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/proteccion-datos/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Protección de Datos (Operativo)

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/proteccion-datos:cold-start-interview`.*

---

## Quiénes somos

*El nombre de la empresa, sector, tamaño y jurisdicciones vienen de `perfil-empresa.md` — edita allí
para cambiar en todos los plugins. Los campos específicos de protección de datos van aquí.*

[Empresa] es una [tipo de entidad]. Tratamos datos personales como [responsable / encargado / ambos]
respecto a [de quién son los datos]. Los datos se alojan en [regiones/países]. El equipo de protección
de datos tiene [N] personas.

**Marco normativo aplicable:** [PLACEHOLDER — RGPD, LOPDGDD, ENS, normativa sectorial]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

**Expedientes abiertos con AEPD:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual | Despacho mediano/grande | In-house | Administración pública | Clínica jurídica]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## DPD — Delegado de Protección de Datos

**DPD designado:** [PLACEHOLDER — Sí (obligatorio art. 37 RGPD) / Sí (voluntario) / No]
**Nombre y contacto del DPD:** [PLACEHOLDER]
**Comunicación con AEPD:** [PLACEHOLDER — canal de comunicación registrado ante la AEPD]
**Inscripción en registro público de DPDs:** [PLACEHOLDER — Sí/No, fecha]

*Referencia: art. 37-39 RGPD; arts. 34-37 LOPDGDD (LO 3/2018).*

---

## Registro de Actividades de Tratamiento (RAT)

*Obligatorio para responsables y encargados según art. 30 RGPD.*

| Campo | Valor |
|---|---|
| Ubicación del RAT | [PLACEHOLDER — ruta o sistema] |
| Número de tratamientos registrados | [PLACEHOLDER] |
| Última actualización | [PLACEHOLDER — fecha] |
| Responsable del mantenimiento | [PLACEHOLDER] |

**Categorías de datos habituales:** [PLACEHOLDER — identificativos, contacto, financieros, salud, etc.]
**Bases jurídicas más utilizadas:** [PLACEHOLDER — consentimiento, ejecución contractual, interés legítimo, obligación legal]
**Plazos de conservación estándar:** [PLACEHOLDER — por categoría]
**Cesiones habituales:** [PLACEHOLDER — a quién, base jurídica]
**Transferencias internacionales:** [PLACEHOLDER — destinos, mecanismo: decisión de adecuación, CCT, BCR]

*Referencia: art. 30 RGPD; art. 31 LOPDGDD.*

---

## Evaluación de Impacto (EIPD)

**Cuándo es obligatoria:** Según lista de la AEPD (publicada conforme art. 35.4 RGPD) y criterios del art. 35.3 RGPD.

| Campo | Valor |
|---|---|
| Metodología utilizada | [PLACEHOLDER — guía AEPD, CNIL PIA, ISO 29134, propia] |
| Plantilla de EIPD | [PLACEHOLDER — ruta] |
| Umbral interno para EIPD | [PLACEHOLDER — criterios propios además de los obligatorios] |
| Consulta previa art. 36 RGPD | [PLACEHOLDER — se ha realizado alguna vez: Sí/No] |

*Referencia: arts. 35-36 RGPD; lista AEPD de tratamientos que requieren EIPD.*

---

## Brechas de seguridad

**Protocolo de gestión de brechas:**

1. **Detección** — Canales de notificación interna: [PLACEHOLDER]
2. **Evaluación de riesgo** — Responsable de evaluación: [PLACEHOLDER]. Metodología: [PLACEHOLDER — ENISA, propia]
3. **Notificación a la AEPD** — Plazo: 72 horas desde conocimiento (art. 33 RGPD). Canal: Sede electrónica AEPD.
4. **Comunicación a interesados** — Cuándo: si riesgo alto para derechos y libertades (art. 34 RGPD). Plantilla: [PLACEHOLDER]

| Campo | Valor |
|---|---|
| Registro de brechas | [PLACEHOLDER — ubicación] |
| Brechas notificadas a AEPD | [PLACEHOLDER — número, última fecha] |
| Equipo de respuesta | [PLACEHOLDER — nombres/roles] |
| Seguro de ciberriesgo | [PLACEHOLDER — Sí/No, cobertura] |

*Referencia: arts. 33-34 RGPD; guía AEPD sobre gestión y notificación de brechas.*

---

## Auditorías y compliance

| Campo | Valor |
|---|---|
| Programa de auditoría | [PLACEHOLDER — frecuencia, alcance] |
| Última auditoría interna | [PLACEHOLDER — fecha, resultado] |
| Última auditoría externa | [PLACEHOLDER — fecha, auditor, resultado] |
| Checklist de cumplimiento | [PLACEHOLDER — ruta al checklist] |

**Áreas auditadas:** [PLACEHOLDER — RAT, consentimientos, ejercicio de derechos, medidas de seguridad, encargados, transferencias internacionales]

---

## Relación con la AEPD

| Tipo de procedimiento | Estado | Referencia |
|---|---|---|
| Reclamaciones recibidas | [PLACEHOLDER] | |
| Información previa (art. 67 LOPDGDD) | [PLACEHOLDER] | |
| Procedimiento sancionador | [PLACEHOLDER] | |
| Recursos ante la AN | [PLACEHOLDER] | |

**Interlocutor habitual con AEPD:** [PLACEHOLDER]
**Apercibimientos recibidos:** [PLACEHOLDER]

*Referencia: arts. 63-78 LOPDGDD; Título VIII LOPDGDD (régimen sancionador).*

---

## Formación y concienciación

| Campo | Valor |
|---|---|
| Plan de formación | [PLACEHOLDER — frecuencia, destinatarios] |
| Última formación impartida | [PLACEHOLDER — fecha, tema] |
| Material formativo | [PLACEHOLDER — ruta] |
| Test de concienciación | [PLACEHOLDER — frecuencia, resultados] |

---

## Encargados de tratamiento

| Encargado | Servicio | Contrato art. 28 RGPD | Última auditoría | Próxima revisión |
|---|---|---|---|---|
| [PLACEHOLDER] | | | | |

**Modelo de contrato de encargado:** [PLACEHOLDER — ruta]
**Proceso de homologación de encargados:** [PLACEHOLDER]

*Referencia: art. 28 RGPD; art. 33 LOPDGDD.*

---

## ENS — Esquema Nacional de Seguridad

**Aplica ENS:** [PLACEHOLDER — Sí (sector público o prestador de servicios al sector público) / No]
**Categoría del sistema:** [PLACEHOLDER — Básica / Media / Alta]
**Certificación ENS:** [PLACEHOLDER — Sí/No, fecha, entidad certificadora]
**Declaración de aplicabilidad:** [PLACEHOLDER — ruta]

*Referencia: RD 311/2022 (Esquema Nacional de Seguridad).*

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Slack / Teams | [PLACEHOLDER] | Notificaciones de brechas entregadas inline |
| Tareas programadas | [PLACEHOLDER] | Auditorías y revisiones bajo demanda |
| Sede electrónica AEPD | [PLACEHOLDER] | Notificaciones manuales |

*Re-comprobar: `/proteccion-datos:cold-start-interview --check-integrations`*

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| RAT completo | [PLACEHOLDER] | | |
| Plantilla EIPD | [PLACEHOLDER] | | |
| Protocolo de brechas | [PLACEHOLDER] | | |
| Contrato tipo encargado | [PLACEHOLDER] | | |
| Política de protección de datos | [PLACEHOLDER] | | |

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan EIPD, informes de auditoría, notificaciones]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Cabecera de trabajo:**

- Si el Rol es Abogado/a o profesional jurídico: `CONFIDENCIAL — TRABAJO PROFESIONAL — PREPARADO BAJO DIRECCIÓN LETRADA`
- Si el Rol es No jurista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON ABOGADO ANTES DE ACTUAR`

*Nota: en Derecho español no existe la doctrina de "attorney work product" estadounidense. La cabecera
"Confidencial" tiene valor como marcado de confidencialidad. El secreto profesional del abogado se rige
por el art. 542.3 LOPJ y el Estatuto General de la Abogacía.*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| RGPD | Reglamento (UE) 2016/679 | Protección de datos — norma directamente aplicable |
| LOPDGDD | LO 3/2018, de 5 de diciembre | Desarrollo nacional del RGPD |
| Guías AEPD | aepd.es/guias | Criterios interpretativos y buenas prácticas |
| Lista EIPD AEPD | Publicada conforme art. 35.4 RGPD | Tratamientos que requieren EIPD |
| ENS | RD 311/2022, de 3 de mayo | Esquema Nacional de Seguridad |

---

*Re-ejecutar: `/proteccion-datos:cold-start-interview --redo`*
