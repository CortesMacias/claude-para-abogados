<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /regulatorio:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /regulatorio:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/regulatorio/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Cumplimiento Regulatorio
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/regulatorio:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de cumplimiento regulatorio se quedan aquí.*

[Empresa] es una [tipo de entidad — sociedad mercantil / entidad financiera / operador de telecomunicaciones / etc.].
Operamos en los sectores [PLACEHOLDER]. El equipo de cumplimiento regulatorio cuenta con [N] personas.
[Responsable de cumplimiento: nombre o ninguno]. La escalación va a [nombre].

**Huella regulatoria:** [PLACEHOLDER — sectores regulados que aplican: financiero, energía, telecomunicaciones, sanitario, alimentario, farmacéutico, medioambiental, transporte, etc.] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos regulatorios abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente; barrido de monitor normativo solo en modo consulta directa |
| Slack / Teams | [PLACEHOLDER ✓/✗] | Alertas regulatorias entregadas inline en vez de publicadas en canal |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Barrido de monitor normativo solo bajo demanda |
| BOE / DOUE / boletines autonómicos (RSS/API) | [PLACEHOLDER ✓/✗] | Consulta manual de fuentes oficiales |

*Re-comprobar: `/regulatorio:entrevista-inicial --check-integraciones`*

---

## Sectores regulados

| Sector | Supervisores principales | Normativa marco | Activo |
|---|---|---|---|
| Financiero | CNMV, Banco de España, DGS | Ley del Mercado de Valores, LOSSEC, normativa MiFID II | [PLACEHOLDER ✓/✗] |
| Energía | CNMC, MITECO | Ley del Sector Eléctrico (24/2013), Ley de Hidrocarburos | [PLACEHOLDER ✓/✗] |
| Telecomunicaciones | CNMC, SETSI | LGTel (11/2022), Código Europeo de Comunicaciones Electrónicas | [PLACEHOLDER ✓/✗] |
| Sanitario | AEMPS, Ministerio de Sanidad | Ley de Garantías y Uso Racional de Medicamentos (29/2006) | [PLACEHOLDER ✓/✗] |
| Alimentario | AESAN, AECOSAN | Reglamento (CE) 178/2002, legislación de seguridad alimentaria | [PLACEHOLDER ✓/✗] |
| Medioambiental | MITECO, CCAA | Ley de Evaluación Ambiental (21/2013), IPPC | [PLACEHOLDER ✓/✗] |
| Transporte | MITMA, CNMC | LOTT, normativa ferroviaria y marítima | [PLACEHOLDER ✓/✗] |
| [Otro sector] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER ✓/✗] |

---

## Supervisores relevantes

| Supervisor | Ámbito | Contacto habitual | Procedimientos abiertos |
|---|---|---|---|
| CNMC | Competencia y sectores regulados | [PLACEHOLDER] | [PLACEHOLDER] |
| CNMV | Mercados de valores | [PLACEHOLDER] | [PLACEHOLDER] |
| Banco de España | Entidades de crédito | [PLACEHOLDER] | [PLACEHOLDER] |
| DGS (DGSFP) | Seguros y fondos de pensiones | [PLACEHOLDER] | [PLACEHOLDER] |
| AEMPS | Medicamentos y productos sanitarios | [PLACEHOLDER] | [PLACEHOLDER] |
| AESAN | Seguridad alimentaria y nutrición | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro supervisor] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Fuentes normativas monitorizadas

| Fuente | Tipo | Frecuencia de consulta | Filtros aplicados |
|---|---|---|---|
| BOE (Boletín Oficial del Estado) | Legislación estatal | [PLACEHOLDER — diaria/semanal] | [PLACEHOLDER — secciones, materias] |
| DOUE (Diario Oficial de la UE) | Legislación europea | [PLACEHOLDER] | [PLACEHOLDER] |
| Boletines autonómicos (BOJA, DOGC, BOCM, etc.) | Legislación autonómica | [PLACEHOLDER] | [PLACEHOLDER — CCAA relevantes] |
| Circulares y guías de supervisores | Soft law | [PLACEHOLDER] | [PLACEHOLDER] |
| Consultas y resoluciones | Doctrina administrativa | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Biblioteca de políticas internas

| Política | Ubicación | Última revisión | Próxima revisión | Responsable |
|---|---|---|---|---|
| Política de cumplimiento normativo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Manual de prevención de blanqueo (si aplica) | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Código de conducta | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otra política] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Umbral de materialidad

*Define qué cambio normativo requiere acción inmediata vs. seguimiento ordinario.*

| Nivel | Criterio | Acción | Plazo |
|---|---|---|---|
| 🔴 Crítico | Cambio que afecta directamente a la operativa o licencia; sanción posible por incumplimiento | Alerta inmediata + análisis de impacto urgente | 24-48 horas |
| 🟠 Alto | Nueva obligación con plazo de adaptación < 6 meses | Análisis de gaps + plan de acción | 1 semana |
| 🟡 Medio | Modificación relevante con plazo de adaptación > 6 meses | Seguimiento + planificación | 1 mes |
| 🟢 Bajo | Cambio informativo o de impacto marginal | Registro + revisión periódica | Próximo ciclo |

**Criterios adicionales de materialidad:** [PLACEHOLDER — umbrales cuantitativos, criterios específicos del sector]

---

## Proceso de gaps regulatorios

```
Detección → Análisis de impacto → Propuesta de adaptación → Aprobación interna → Implementación → Verificación
```

| Fase | Responsable | Plazo estándar | Documentación |
|---|---|---|---|
| Detección | [PLACEHOLDER] | Continua | Alerta normativa |
| Análisis de impacto | [PLACEHOLDER] | [PLACEHOLDER] días | Informe de gaps |
| Propuesta de adaptación | [PLACEHOLDER] | [PLACEHOLDER] días | Memo de propuesta |
| Aprobación interna | [PLACEHOLDER] | [PLACEHOLDER] días | Acta de aprobación |
| Implementación | [PLACEHOLDER] | [PLACEHOLDER] días | Plan de implementación |
| Verificación | [PLACEHOLDER] | [PLACEHOLDER] días | Informe de cierre |

---

## Calendario regulatorio

| Obligación | Periodicidad | Plazo | Modelo/Formato | Supervisor destinatario |
|---|---|---|---|---|
| [PLACEHOLDER — p.ej. informe anual de cumplimiento] | Anual | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| [PLACEHOLDER — p.ej. comunicación de operaciones sospechosas] | Puntual | Inmediato | [PLACEHOLDER] | SEPBLAC |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Cambio normativo rutinario | Equipo de cumplimiento | — | — |
| Gap regulatorio material | Equipo de cumplimiento | Dirección jurídica | Impacto 🟠 o superior |
| Requerimiento de supervisor | — | Dirección jurídica + Dirección General | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Consejo | Siempre |
| Inspección o visita del supervisor | — | Dirección jurídica + área afectada | Siempre |

---

## Referencias legislativas principales

- **LPAC** — Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas
- **LRJSP** — Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público
- **Normativa sectorial específica** — según sectores activos en la tabla de sectores regulados
- **Reglamentos UE directamente aplicables** — según sector (MiFID II, DORA, SFDR, etc.)

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Mapa regulatorio vigente | [PLACEHOLDER] | [PLACEHOLDER] | |
| Política de cumplimiento | [PLACEHOLDER] | [PLACEHOLDER] | |
| Último informe de gaps | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan los análisis de gaps, alertas normativas y calendarios regulatorios]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo** (se antepone a análisis de gaps, alertas regulatorias, informes de cumplimiento):

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/regulatorio:entrevista-inicial --redo`*
