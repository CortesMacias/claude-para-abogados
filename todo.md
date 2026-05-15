# Claude para Abogados (España) — Tareas

## Fase 1 — Estructura base ✅

- [x] Crear estructura de carpetas para los 20 módulos
- [x] Traducir README.md principal al castellano
- [x] Traducir QUICKSTART.md
- [x] Traducir CONTRIBUTING.md
- [x] Traducir CONNECTORS.md
- [x] Adaptar plugin.json de cada módulo al castellano
- [x] Crear plantilla de perfil de empresa compartido
- [x] Crear READMEs individuales para los 20 módulos
- [x] Crear prompt.md con contexto del proyecto

## Fase 2 — CLAUDE.md y entrevistas iniciales ✅

- [x] Escribir CLAUDE.md para los 20 módulos (legislación española, placeholders)
- [x] Crear entrevista-inicial (cold-start) para los 20 módulos

## Fase 3 — Skills principales ✅

- [x] Mercantil: revision, historial-adendas, escalado, renovaciones (4 skills)
- [x] Societario: revision-tabular, extraccion-incidencias, acuerdo-social, cumplimiento, checklist-cierre (5 skills)
- [x] Laboral: revision-despido, revision-contratacion, indemnizacion, consulta, politica (5 skills)
- [x] Propiedad intelectual: busqueda-marca, burofax, oss, clausulas, portfolio (5 skills)
- [x] Procesal: cronologia, demanda, requerimiento-recibido, plazos, intake, briefing, portfolio (7 skills)
- [x] Privacidad: derechos, encargo, eipd, triaje, gap (5 skills)
- [x] Consumo: lanzamiento, claims, condiciones-generales, consulta (4 skills)
- [x] Regulatorio: diff, gaps, redaccion, alertas (4 skills)
- [x] Gobernanza IA: triaje, evaluacion, proveedor, gap (4 skills)
- [x] Fiscal: calendario, revision, consulta, procedimiento (4 skills)
- [x] Administrativo: procedimiento, contratacion, contencioso (3 skills)
- [x] Inmobiliario: arrendamiento, compraventa, comunidad (3 skills)
- [x] Concursal: diagnostico, plan, creditos (3 skills)
- [x] Familia: convenio, regimen-economico, pensiones (3 skills)
- [x] Protección de datos: rat, eipd, brecha, aepd (4 skills)
- [x] Startups: constitucion, stock-options, ronda, incentivos, contratacion (5 skills)
- [x] Clínica jurídica: intake, memo, investigacion, plazos, carta (5 skills)
- [x] Estudiante de derecho: socratico, irac, esquema, oposiciones, acceso, fichas, plan (7 skills)

## Fase 4 — Pulido y validación ✅

- [x] Auditoría de coherencia entre módulos (paths, idioma, formato) — 0 errores
- [x] Crear 17 agentes programados (vigilantes, monitores, alertas)
- [x] Crear scripts de validación (validate.py, lint-tool-scope.py, contar-estadisticas.sh, verificar-legislacion.py)
- [x] Ejecutar validación — 20/20 módulos españoles PASS

## Pendiente (mejoras futuras)

- [ ] Verificar manualmente las referencias legislativas con verificar-legislacion.py
- [ ] Testear entrevistas iniciales con casos reales
- [ ] Testear skills principales con documentos reales
- [x] Eliminar módulos originales en inglés
- [x] Publicar en GitHub (público, con atribución)

### MCPs por desarrollar

| Prioridad | MCP | Fuente |
|---|---|---|
| **Alta** | CENDOJ | Jurisprudencia CGPJ |
| **Alta** | BOE | Legislación y disposiciones |
| **Alta** | EUR-Lex | Normativa UE |
| **Alta** | AEPD Resoluciones | Resoluciones de protección de datos |
| **Media** | Registro Mercantil | Información registral de sociedades |
| **Media** | OEPM | Marcas y patentes nacionales |
| **Media** | EUIPO | Marcas y diseños UE |
| **Media** | DGT Consultas | Consultas vinculantes tributarias |
| **Media** | PLACE | Contratación pública |
| **Media** | LexNET | Notificaciones judiciales |
| **Baja** | Registro Público Concursal | Procedimientos concursales |
| **Baja** | Catastro | Información catastral |
| **Baja** | Registro de la Propiedad | Notas simples |
| **Baja** | CGPJ Tablas | Tablas pensiones alimenticias |
| **Baja** | AESIA | Sandbox regulatorio de IA |

## Estadísticas del proyecto

| Concepto | Cantidad |
|---|---|
| Módulos españoles | 20 |
| Skills totales | 100 |
| Agentes programados | 17 |
| Scripts de validación | 4 |
| Archivos en módulos españoles | ~260 |
| Documentación raíz | 8 archivos |
