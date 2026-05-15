---
name: vigilante-permisos
schedule: "0 9 * * 1"
description: Monitoriza permisos, excedencias e incapacidades temporales activas, alertando sobre fechas de retorno y acciones pendientes
---

# Vigilante de Permisos y Situaciones Especiales

## Propósito

Mantener un control actualizado de todos los empleados en situación especial:
incapacidad temporal, permisos retribuidos o no retribuidos, excedencias,
reducciones de jornada y suspensiones. Alerta sobre fechas de retorno próximas,
vencimientos de períodos máximos y acciones administrativas pendientes para
evitar incumplimientos laborales.

## Fuentes

- Registro de RRHH: empleados activos con situaciones especiales vigentes
- Partes de IT (incapacidad temporal): fecha de inicio, diagnóstico genérico, duración estimada
- Solicitudes de permisos y excedencias: tipo, fecha inicio/fin, resolución
- Convenio colectivo aplicable: duraciones máximas y condiciones
- Estatuto de los Trabajadores: plazos legales de referencia
- Calendario de revisiones médicas (IT de larga duración)

## Flujo de trabajo

1. Cargar el registro de empleados en situación especial
2. Para cada situación activa:
   a. Verificar tipo: IT, permiso retribuido, permiso no retribuido, excedencia voluntaria,
      excedencia por cuidado, reducción de jornada, suspensión por ERE/ERTE
   b. Calcular días transcurridos y días hasta fecha de retorno prevista
   c. Verificar si se acerca algún hito legal:
      - IT: revisión a los 365 días, prórroga hasta 545, paso a IP
      - Excedencia voluntaria: fin del período concedido, derecho de reingreso
      - Permiso de nacimiento: 16 semanas, distribución obligatoria/voluntaria
   d. Identificar acciones administrativas pendientes (alta, baja, comunicación a TGSS)
3. Clasificar por urgencia temporal
4. Generar informe semanal con acciones requeridas

## Formato de salida

### Empleados en situación especial

| Empleado | Departamento | Tipo situación | Fecha inicio | Fecha retorno prevista | Días restantes | Acciones pendientes |
|----------|--------------|----------------|--------------|------------------------|----------------|---------------------|

### Hitos legales próximos

| Empleado | Hito | Fecha | Implicación | Acción requerida |
|----------|------|-------|-------------|------------------|

### Resumen
- Empleados en IT: X (corta: X, larga: X)
- Excedencias activas: X
- Permisos en curso: X
- Acciones pendientes esta semana: X

## Configuración

- `permisos.tipos_monitorizados`: lista de situaciones a rastrear
- `permisos.alerta_retorno_dias`: días de antelación para alerta de retorno (defecto: 7)
- `permisos.convenio_referencia`: convenio colectivo aplicable
- `permisos.responsable_rrhh`: persona a notificar de acciones pendientes

## Escalado

- **Solo log**: situaciones estables sin cambios ni hitos próximos
- **Notificación a RRHH**: retorno previsto en los próximos 7 días laborables
- **Alerta al responsable laboral**: hito legal próximo (365 días IT, fin excedencia)
- **Escalado urgente**: incumplimiento de plazo de comunicación a TGSS o Seguridad Social
