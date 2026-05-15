# Claude Legal España — Especificación del Proyecto

## Objetivo

Adaptar el repositorio [claude-for-legal](https://github.com/anthropics/claude-for-legal) al derecho español y castellano. El resultado es un conjunto de agentes legales especializados que cubren las principales ramas del derecho en España.

## Público objetivo

- **Despachos de abogados** pequeños y medianos
- **Abogados in-house** de empresas
- **Startups** (módulo específico con enfoque práctico)

## Decisiones de diseño

- Idioma: castellano en todo (UI, prompts, skills, documentación)
- Nivel de profundidad inicial: ligero (playbooks básicos, sin escalation matrices complejas)
- Estructura: misma arquitectura de plugins que el repo original
- Legislación: siempre referenciada con nombre completo y artículos relevantes

---

## Módulos — Adaptados del original

| # | Módulo | Fuente original | Legislación clave española |
|---|--------|----------------|---------------------------|
| 1 | **mercantil** | commercial-legal | Código de Comercio, Código Civil (obligaciones), LSSI-CE |
| 2 | **societario** | corporate-legal | LSC, Reglamento del Registro Mercantil, LME, CNMV |
| 3 | **laboral** | employment-legal | Estatuto de los Trabajadores, LISOS, convenios colectivos, FOGASA |
| 4 | **propiedad-intelectual** | ip-legal | LPI, Ley de Marcas, Ley de Patentes, OEPM, directivas UE |
| 5 | **procesal** | litigation-legal | LEC, LECrim, LJCA, LOPJ |
| 6 | **privacidad** | privacy-legal | RGPD, LOPDGDD, AEPD |
| 7 | **consumo** | product-legal | LGDCU, Ley de Competencia Desleal, directivas UE |
| 8 | **regulatorio** | regulatory-legal | BOE, CNMC, CNMV, Banco de España, supervisores sectoriales |
| 9 | **gobernanza-ia** | ai-governance-legal | Reglamento IA (EU AI Act), sandbox AESIA |
| 10 | **clinica-legal** | legal-clinic | Turno de oficio, Ley de Asistencia Jurídica Gratuita |
| 11 | **estudiante-derecho** | law-student | Grado en Derecho, oposiciones, acceso a la abogacía |
| 12 | **hub-constructor** | legal-builder-hub | Sin cambios legales, solo traducción |
| 13 | **recetas-agentes** | managed-agent-cookbooks | Sin cambios legales, solo traducción |

## Módulos — Nuevos para España

| # | Módulo | Justificación | Legislación clave |
|---|--------|--------------|-------------------|
| 14 | **fiscal** | No existe en el original. IRPF, IS, IVA, procedimientos tributarios | LGT, LIRPF, LIS, LIVA, reglamentos de desarrollo |
| 15 | **administrativo** | Procedimiento administrativo y contencioso | LPAC, LRJSP, LJCA |
| 16 | **inmobiliario** | Compraventa, arrendamientos, propiedad horizontal | CC (derechos reales), LAU, LPH, Ley Hipotecaria |
| 17 | **concursal** | Insolvencia y reestructuración | TRLC (Texto Refundido Ley Concursal) |
| 18 | **familia** | Divorcios, custodia, régimen económico | CC (Libro IV), LEC (procesos de familia), legislación autonómica |
| 19 | **proteccion-datos** | Separado de privacidad, más operativo | RGPD, LOPDGDD, guías AEPD, ENS |
| 20 | **startups** | Módulo práctico para fundadores | Ley de Startups, LSC (SL), pactos de socios, stock options, incentivos fiscales |

---

## Fases de ejecución

### Fase 1 — Estructura base
- Crear estructura de carpetas para los 20 módulos
- Traducir infraestructura común (README principal, QUICKSTART, CONTRIBUTING)
- Adaptar el sistema de cold-start interview al contexto español

### Fase 2 — Módulos adaptados (13)
- Reescribir CLAUDE.md de cada módulo con legislación española
- Crear skills básicos por módulo
- Sustituir todas las referencias US por españolas/UE

### Fase 3 — Módulos nuevos (7)
- Crear CLAUDE.md, skills y estructura para cada módulo nuevo
- Fiscal, administrativo, inmobiliario, concursal, familia, protección de datos, startups

### Fase 4 — Pulido y validación
- Revisar coherencia entre módulos
- Testear skills
- Documentación final

---

## Notas

- El módulo de **privacidad** (adaptado) se enfoca en cumplimiento normativo y DPAs
- El módulo de **protección de datos** (nuevo) se enfoca en operativa diaria: brechas, evaluaciones de impacto, registro de actividades, relación con la AEPD
- El módulo de **startups** cruza transversalmente societario, fiscal y laboral pero con un enfoque práctico para fundadores
