---
name: cumplimiento-registral
schedule: "0 9 1 * *"
description: Monitoriza las obligaciones de cumplimiento registral y societario, alertando sobre plazos próximos como cuentas anuales, libros y renovación de cargos
---

# Vigilante de Cumplimiento Registral

## Propósito

Controlar el calendario de obligaciones registrales y societarias de todas las
entidades gestionadas, asegurando que se cumplen los plazos legales para el depósito
de cuentas anuales, legalización de libros, renovación de cargos sociales y demás
obligaciones ante el Registro Mercantil.

## Fuentes

- Registro de entidades gestionadas (denominación, CIF, forma jurídica, Registro Mercantil)
- Calendario legal de obligaciones societarias españolas:
  - Formulación de cuentas anuales: 3 meses desde cierre (31 marzo para ejercicio natural)
  - Aprobación en Junta General: 6 meses desde cierre (30 junio)
  - Depósito en Registro Mercantil: 1 mes desde aprobación (30 julio)
  - Legalización de libros: 4 meses desde cierre (30 abril)
  - Impuesto sobre Sociedades: 25 días naturales tras 6 meses desde cierre (25 julio)
- Registro de cargos sociales con fecha de nombramiento y duración estatutaria
- Histórico de cumplimiento de cada entidad

## Flujo de trabajo

1. Cargar la lista de entidades activas con sus datos registrales
2. Para cada entidad, calcular los plazos aplicables según su fecha de cierre de ejercicio
3. Verificar el estado de cada obligación:
   - ¿Se han formulado las cuentas anuales?
   - ¿Se ha convocado/celebrado la Junta General Ordinaria?
   - ¿Se han depositado las cuentas?
   - ¿Se han legalizado los libros?
   - ¿Hay cargos próximos a caducar o ya caducados?
4. Calcular días restantes para cada obligación pendiente
5. Clasificar por urgencia y generar el informe mensual
6. Verificar inscripciones pendientes en el Registro Mercantil

## Formato de salida

### Obligaciones próximas

| Entidad | CIF | Obligación | Plazo legal | Días restantes | Estado | Responsable |
|---------|-----|------------|-------------|----------------|--------|-------------|

- Estados: ✅ Cumplida | ⏳ En curso | ⚠️ Próxima | 🔴 Vencida

### Cargos sociales

| Entidad | Cargo | Titular | Fecha nombramiento | Duración | Fecha caducidad | Estado |
|---------|-------|---------|--------------------|----------|-----------------|--------|

### Resumen
- Entidades al día: X/Y
- Obligaciones pendientes urgentes: X
- Cargos por renovar en próximos 3 meses: X

## Configuración

- `cumplimiento.entidades`: lista de entidades a monitorizar
- `cumplimiento.cierre_ejercicio`: fecha de cierre por entidad (defecto: 31/12)
- `cumplimiento.alerta_anticipada_dias`: días de antelación para alertar (defecto: 30)
- `cumplimiento.responsable_defecto`: persona a notificar si no hay responsable asignado

## Escalado

- **Solo log**: obligaciones cumplidas o con más de 60 días de margen
- **Notificación al responsable**: obligación a menos de 30 días sin acción iniciada
- **Alerta al equipo societario**: obligación vencida o a menos de 7 días
- **Escalado a dirección**: riesgo de cierre registral o sanción por incumplimiento reiterado
