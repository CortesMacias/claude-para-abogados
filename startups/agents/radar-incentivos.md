---
name: radar-incentivos
schedule: "0 9 1 * *"
description: Monitoriza cambios en incentivos fiscales y bonificaciones aplicables a startups, incluyendo la Ley de Startups y deducciones por I+D+i
---

# Radar de Incentivos para Startups

## Propósito

Rastrear mensualmente los cambios normativos y administrativos que afectan a los
incentivos fiscales, bonificaciones y beneficios aplicables a empresas emergentes
en España. Cubre la Ley 28/2022 de fomento del ecosistema de las empresas
emergentes (Ley de Startups), deducciones por I+D+i, stock options, y otros
instrumentos de apoyo al emprendimiento innovador.

## Fuentes

- BOE: modificaciones de la Ley de Startups y normativa de desarrollo
- AEAT: consultas vinculantes, notas informativas sobre incentivos
- ENISA: convocatorias y cambios en líneas de financiación
- CDTI: actualizaciones en programas de I+D+i
- Ministerio de Economía y Transformación Digital: programas de apoyo
- Registros de certificación de empresa emergente
- Comunidades autónomas: incentivos autonómicos específicos
- Consultas vinculantes de la DGT sobre tributación de startups

## Flujo de trabajo

1. Rastrear fuentes configuradas en busca de novedades en incentivos
2. Para cada cambio detectado:
   a. Clasificar por tipo de incentivo:
      - Fiscales: tipo reducido IS (15%), deducción I+D+i, stock options (50K exención),
        deducción por inversión en empresa nueva (art. 68.1 LIRPF)
      - Bonificaciones SS: tarifa plana autónomos, bonificaciones por contratación
      - Financiación pública: ENISA, CDTI, ICO, Next Generation EU
      - Regulatorios: sandbox, certificación empresa emergente
   b. Evaluar impacto: cambio favorable, desfavorable o neutral
   c. Determinar aplicabilidad según perfil de las entidades gestionadas
   d. Identificar plazos de solicitud o aplicación
3. Verificar el estado de los incentivos actualmente aplicados:
   a. Requisitos que podrían dejar de cumplirse
   b. Plazos de vigencia de certificaciones
   c. Nuevos requisitos documentales
4. Generar informe mensual con novedades y acciones

## Formato de salida

### Novedades en incentivos

| Incentivo | Tipo | Fuente | Cambio | Impacto | Aplicable | Acción requerida |
|-----------|------|--------|--------|---------|-----------|------------------|

### Estado de incentivos aplicados

| Incentivo | Entidad | Estado | Vigencia | Requisitos pendientes |
|-----------|---------|--------|----------|-----------------------|

### Convocatorias abiertas

| Programa | Organismo | Fecha apertura | Fecha cierre | Importe | Elegibilidad |
|----------|-----------|----------------|--------------|---------|--------------|

### Resumen
- Cambios normativos detectados: X
- Incentivos activos monitorizados: X
- Convocatorias abiertas relevantes: X
- Acciones requeridas este mes: X

## Configuración

- `incentivos.entidades_emergentes`: lista de entidades con perfil startup
- `incentivos.sectores`: sectores de actividad para filtrar convocatorias
- `incentivos.fuentes_autonomicas`: comunidades autónomas a rastrear
- `incentivos.incluir_financiacion`: monitorizar convocatorias de financiación pública (defecto: true)
- `incentivos.responsable_fiscal`: persona a notificar de cambios fiscales

## Escalado

- **Solo log**: mes sin cambios relevantes ni convocatorias nuevas
- **Notificación al responsable fiscal**: cambio en requisitos de incentivo actualmente aplicado
- **Alerta al equipo**: nueva convocatoria con plazo de solicitud abierto
- **Escalado a dirección**: pérdida potencial de incentivo por incumplimiento de requisitos
