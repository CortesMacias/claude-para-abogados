<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /privacidad:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /privacidad:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/privacidad/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Privacidad y Protección de Datos

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/privacidad:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de privacidad y protección de datos lo forman [N] personas. [Nombre del responsable / DPO] es el punto final de escalado.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna / DPO interno | DPO externo]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a colegiado/a | DPO | Compliance officer | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Rol en el tratamiento de datos

**Condición principal:** [PLACEHOLDER — Responsable del tratamiento | Encargado del tratamiento | Corresponsable]

**Detalle por actividad principal:**

| Actividad de tratamiento | Rol (R/E/CR) | Base jurídica | Categorías de datos |
|---|---|---|---|
| [PLACEHOLDER — ej., "Gestión de clientes/CRM"] | [R] | [PLACEHOLDER — ej., "Ejecución contrato art. 6.1.b RGPD"] | [PLACEHOLDER — ej., "Identificativos, contacto, financieros"] |
| [PLACEHOLDER — ej., "Gestión de empleados/RRHH"] | [R] | [PLACEHOLDER — ej., "Obligación legal art. 6.1.c + ejecución contrato art. 6.1.b"] | [PLACEHOLDER — ej., "Identificativos, financieros, salud (IT)"] |
| [PLACEHOLDER — ej., "Prestación de servicio SaaS"] | [E] | [PLACEHOLDER — ej., "Contrato de encargado art. 28 RGPD"] | [PLACEHOLDER] |
| [PLACEHOLDER] | | | |

---

## Delegado de Protección de Datos (DPO)

**Designación obligatoria:** [PLACEHOLDER — ej., "Sí (art. 34 LOPDGDD: tratamiento a gran escala / categorías especiales / observación sistemática)"]

**Tipo:** [PLACEHOLDER — Interno | Externo]
**Nombre:** [PLACEHOLDER]
**Datos de contacto:** [PLACEHOLDER — email, teléfono]
**Comunicación a la AEPD:** [PLACEHOLDER — ej., "Inscrito en el registro de DPO de la AEPD con fecha DD/MM/AAAA"]

**Funciones (art. 39 RGPD):**
- Informar y asesorar al responsable/encargado
- Supervisar el cumplimiento del RGPD y la LOPDGDD
- Cooperar con la AEPD como punto de contacto
- [PLACEHOLDER — funciones adicionales asignadas]

---

## Registro de actividades de tratamiento (RAT)

**Estado:** [PLACEHOLDER — ej., "Actualizado a fecha DD/MM/AAAA; revisión semestral"]
**Ubicación:** [PLACEHOLDER — ej., "Documento en Drive / herramienta de compliance X / Excel compartido"]
**Responsable de actualización:** [PLACEHOLDER]

**Tratamientos registrados:** [PLACEHOLDER — ej., "15 actividades de tratamiento como responsable; 8 como encargado"]

**Revisión periódica:** [PLACEHOLDER — ej., "Semestral; obligatoria ante cualquier nueva actividad de tratamiento, nuevo proveedor con acceso a datos, o cambio de base jurídica"]

---

## Bases jurídicas habituales

| Base jurídica | Artículo RGPD | Uso principal | Notas |
|---|---|---|---|
| Consentimiento | Art. 6.1.a | [PLACEHOLDER — ej., "Marketing, cookies no esenciales, comunicaciones comerciales"] | [PLACEHOLDER — ej., "Granular, específico, revocable; conservar prueba"] |
| Ejecución de contrato | Art. 6.1.b | [PLACEHOLDER — ej., "Prestación del servicio, gestión de clientes"] | |
| Obligación legal | Art. 6.1.c | [PLACEHOLDER — ej., "Nóminas, facturación, prevención de blanqueo"] | [PLACEHOLDER — ej., "Identificar la norma concreta"] |
| Interés legítimo | Art. 6.1.f | [PLACEHOLDER — ej., "Prevención de fraude, seguridad de red, marketing directo a clientes (LSSI art. 21.2)"] | [PLACEHOLDER — ej., "Realizar test de ponderación y documentar"] |
| Interés vital | Art. 6.1.d | [PLACEHOLDER — ej., "Emergencias sanitarias"] | Uso excepcional |
| Interés público | Art. 6.1.e | [PLACEHOLDER — ej., "Solo si administración pública"] | |

**Categorías especiales de datos (art. 9 RGPD):**
- [PLACEHOLDER — ej., "Datos de salud de empleados (IT/AT) — base: obligación legal art. 9.2.b; datos sindicales de representantes — base: art. 9.2.b"]

---

## Transferencias internacionales

**¿Se realizan transferencias fuera del EEE?** [PLACEHOLDER — Sí / No]

**Mecanismos utilizados:**

| Destino | Proveedor/Receptor | Mecanismo | Estado |
|---|---|---|---|
| [PLACEHOLDER — ej., "EE.UU."] | [PLACEHOLDER — ej., "AWS, Google, Microsoft"] | [PLACEHOLDER — ej., "Marco de Privacidad UE-EE.UU. (decisión de adecuación 10/07/2023)"] | [PLACEHOLDER — ej., "Vigente; monitorizar estabilidad del marco"] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "Cláusulas contractuales tipo (Decisión 2021/914)"] | [PLACEHOLDER] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "Normas corporativas vinculantes (BCR)"] | [PLACEHOLDER] |

**Evaluación de impacto de transferencias (TIA):** [PLACEHOLDER — ej., "Realizada para transferencias a EE.UU. pre-DPF; actualizar si cae el marco"]

---

## Encargos de tratamiento — Playbook

**Posición como responsable (contratamos encargados):**

**Cláusulas mínimas exigidas (art. 28 RGPD):**
- [ ] Objeto, duración, naturaleza y finalidad del tratamiento
- [ ] Tipo de datos personales y categorías de interesados
- [ ] Obligación de tratar solo siguiendo instrucciones documentadas
- [ ] Deber de confidencialidad del personal
- [ ] Medidas de seguridad (art. 32 RGPD)
- [ ] Régimen de subencargados (autorización previa general/específica + notificación)
- [ ] Asistencia al responsable en derechos de los interesados
- [ ] Asistencia en EIPD y consulta previa
- [ ] Devolución o supresión de datos al finalizar
- [ ] Información y auditoría

**Posición ante subencargados:** [PLACEHOLDER — ej., "Autorización general con derecho de oposición en 15 días; lista accesible de subencargados; el encargado responde del subencargado"]

**Modelo house de contrato de encargado:** [PLACEHOLDER — ej., "Basado en las cláusulas contractuales tipo del CEPD / modelo AEPD; adaptado por el equipo jurídico"]

**Posición como encargado (nos contratan como encargados):**
- [PLACEHOLDER — ej., "Usar nuestro modelo house; aceptar modelo del cliente con revisión previa; nunca aceptar responsabilidad ilimitada como encargado"]

---

## Derechos ARCO-POL

| Derecho | Artículo RGPD | Plazo de respuesta | Formulario | Responsable |
|---|---|---|---|---|
| Acceso | Art. 15 | 1 mes (prorrogable 2 meses si complejidad) | [PLACEHOLDER] | [PLACEHOLDER] |
| Rectificación | Art. 16 | 1 mes | [PLACEHOLDER] | [PLACEHOLDER] |
| Supresión (olvido) | Art. 17 | 1 mes | [PLACEHOLDER] | [PLACEHOLDER] |
| Oposición | Art. 21 | 1 mes | [PLACEHOLDER] | [PLACEHOLDER] |
| Portabilidad | Art. 20 | 1 mes | [PLACEHOLDER] | [PLACEHOLDER] |
| Limitación | Art. 18 | 1 mes | [PLACEHOLDER] | [PLACEHOLDER] |

**Canal de recepción:** [PLACEHOLDER — ej., "Email dpd@empresa.com; formulario web; correo postal"]
**Verificación de identidad:** [PLACEHOLDER — ej., "Solicitar copia de DNI/NIE; verificar contra registros internos"]
**Proceso de respuesta:** [PLACEHOLDER — ej., "DPO recibe → verifica identidad (24h) → localiza datos (5 días) → prepara respuesta → firma responsable → envía al interesado"]

**Excepciones a la supresión:** [PLACEHOLDER — ej., "Obligaciones legales (facturación: 4 años CC; fiscal: 4 años LGT; prevención de blanqueo: 10 años Ley 10/2010)"]

---

## Evaluación de Impacto (EIPD)

**Cuándo es obligatoria (art. 35 RGPD + lista AEPD):**
- [ ] Elaboración de perfiles con efectos jurídicos o significativos
- [ ] Tratamiento a gran escala de categorías especiales
- [ ] Observación sistemática a gran escala de zonas públicas
- [ ] Tratamientos incluidos en la lista de la AEPD (2019)
- [PLACEHOLDER — supuestos adicionales aplicables al negocio]

**Formato house:** [PLACEHOLDER — ej., "Modelo AEPD (herramienta GESTIONA) / plantilla interna adaptada"]

**Proceso:**
1. [PLACEHOLDER — ej., "Identificar necesidad de EIPD (checklist)"]
2. [PLACEHOLDER — ej., "Describir tratamiento y evaluar necesidad/proporcionalidad"]
3. [PLACEHOLDER — ej., "Identificar y evaluar riesgos"]
4. [PLACEHOLDER — ej., "Determinar medidas para mitigar riesgos"]
5. [PLACEHOLDER — ej., "Consulta al DPO"]
6. [PLACEHOLDER — ej., "Consulta previa a AEPD si riesgo residual alto (art. 36 RGPD)"]

---

## Brechas de seguridad — Protocolo

**Obligación de notificación a la AEPD:** 72 horas desde conocimiento (art. 33 RGPD)

**Protocolo interno:**

| Fase | Plazo | Responsable | Acción |
|---|---|---|---|
| Detección | Inmediato | Cualquier empleado | Comunicar al DPO / equipo de seguridad |
| Evaluación inicial | <12h | [PLACEHOLDER — DPO + IT] | Clasificar severidad, datos afectados, interesados afectados |
| Notificación a AEPD | <72h | [PLACEHOLDER — DPO] | Sede electrónica AEPD si riesgo para derechos y libertades |
| Comunicación a interesados | Sin dilación | [PLACEHOLDER — DPO + Comunicación] | Si riesgo alto (art. 34 RGPD) |
| Documentación | <7 días | [PLACEHOLDER] | Registro interno (art. 33.5 RGPD): hechos, efectos, medidas |
| Post-mortem | <30 días | [PLACEHOLDER] | Análisis de causa raíz y medidas correctivas |

**Canal de notificación AEPD:** [PLACEHOLDER — ej., "Sede electrónica sedeagpd.gob.es; formulario de notificación de brechas"]

**Plantilla de comunicación a interesados:** [PLACEHOLDER — ej., "Modelo house aprobado; incluir: naturaleza de la brecha, datos de contacto DPO, consecuencias probables, medidas adoptadas y recomendadas"]

---

## Política de privacidad

### Web

**Estado:** [PLACEHOLDER — ej., "Publicada en [URL]; última revisión DD/MM/AAAA"]
**Contenido mínimo (art. 13 RGPD):**
- [ ] Identidad y datos de contacto del responsable
- [ ] Datos de contacto del DPO
- [ ] Fines y bases jurídicas de cada tratamiento
- [ ] Destinatarios o categorías de destinatarios
- [ ] Transferencias internacionales y garantías
- [ ] Plazos de conservación o criterios
- [ ] Derechos del interesado y cómo ejercerlos
- [ ] Derecho a reclamar ante la AEPD
- [ ] Existencia de decisiones automatizadas

### Política de cookies

**Estado:** [PLACEHOLDER — ej., "Banner implementado con [herramienta]; cumple guía AEPD sobre cookies"]
**Herramienta de gestión de consentimiento (CMP):** [PLACEHOLDER — ej., "Cookiebot / OneTrust / CookieYes / desarrollo propio"]
**Posición:** [PLACEHOLDER — ej., "Solo cookies técnicas sin consentimiento; resto requiere consentimiento previo, granular y revocable; no cookie walls"]

### Empleados

**Cláusula informativa en contrato de trabajo:** [PLACEHOLDER — ej., "Modelo house; incluye videovigilancia, geolocalización, control de dispositivos según art. 87-91 LOPDGDD"]

### Apps móviles

**Estado:** [PLACEHOLDER — ej., "Política integrada en la app; permisos solicitados con just-in-time notice"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Analista/paralegal] | [PLACEHOLDER — ej., "Ejercicio de derechos rutinario, actualización de RAT"] | [DPO / Abogado/a] | [método] |
| [DPO / Abogado/a] | [PLACEHOLDER — ej., "EIPDs, contratos de encargado, consultas de bases jurídicas"] | [Responsable jurídico / Socio/a] | [método] |
| [Responsable jurídico] | [PLACEHOLDER — ej., "Brechas sin riesgo alto, inspecciones AEPD de rutina"] | [Comité dirección / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda brecha con riesgo alto, toda resolución sancionadora AEPD, toda transferencia internacional nueva, tratamiento de datos biométricos"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **RGPD** — Reglamento General de Protección de Datos (Reglamento UE 2016/679, de 27 de abril de 2016)
- **LOPDGDD** — Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales (LO 3/2018, de 5 de diciembre)
- **Guías de la AEPD** — guías sobre cookies, videovigilancia, relaciones laborales, brechas de seguridad, evaluaciones de impacto, transferencias internacionales, etc.
- **Directrices del CEPD (EDPB)** — directrices sobre consentimiento, interés legítimo, transferencias, derecho de acceso, DPO, etc.
- **LSSI-CE** (Ley 34/2002) — en lo relativo a comunicaciones comerciales electrónicas y cookies
- **Ley 10/2010** de prevención del blanqueo de capitales — plazos de conservación
- **Ley 34/2002** (LSSI-CE) — comunicaciones comerciales y cookies

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/privacidad:entrevista-inicial --repetir`*
