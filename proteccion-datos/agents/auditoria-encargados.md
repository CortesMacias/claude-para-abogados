---
name: auditoria-encargados
schedule: "0 9 1 1,4,7,10 *"
description: Revisión trimestral de contratos de encargado de tratamiento y calendario de auditorías a proveedores que tratan datos personales
---

# Auditoría de Encargados de Tratamiento

## Propósito

Controlar trimestralmente el estado de los contratos de encargado de tratamiento
(art. 28 RGPD) y el cumplimiento del plan de auditorías a proveedores que tratan
datos personales por cuenta de la organización. Asegura que todos los encargados
tienen contrato vigente y que se cumplen las auditorías periódicas pactadas.

## Fuentes

- Registro de encargados de tratamiento con datos contractuales
- Contratos de encargado vigentes (art. 28 RGPD / LOPDGDD)
- Plan de auditorías a encargados (anual o según contrato)
- Informes de auditorías realizadas
- Registro de Actividades de Tratamiento (RAT): tratamientos delegados a cada encargado
- Registro de incidentes y brechas de seguridad por encargado
- Certificaciones del encargado (ISO 27001, ENS, SOC 2, etc.)

## Flujo de trabajo

1. Cargar el registro de encargados de tratamiento activos
2. Para cada encargado:
   a. Verificar existencia y vigencia del contrato art. 28 RGPD
   b. Comprobar que el contrato cubre todos los tratamientos delegados según el RAT
   c. Verificar fecha de vencimiento del contrato y necesidad de renovación
   d. Revisar el plan de auditorías:
      - Última auditoría realizada (fecha, resultado)
      - Próxima auditoría programada
      - Acciones correctivas pendientes de auditorías anteriores
   e. Comprobar vigencia de certificaciones aportadas
   f. Verificar si ha habido incidentes o brechas en el trimestre
3. Identificar encargados con contrato vencido o próximo a vencer
4. Identificar auditorías vencidas o próximas según el plan
5. Generar informe trimestral con estado y acciones requeridas

## Formato de salida

### Estado de contratos de encargado

| Encargado | Tratamientos | Contrato vigente | Vencimiento | Días restantes | Acciones |
|-----------|--------------|------------------|-------------|----------------|----------|

### Plan de auditorías

| Encargado | Última auditoría | Resultado | Próxima programada | Estado | Correctivas pendientes |
|-----------|------------------|-----------|--------------------|--------|------------------------|

### Certificaciones

| Encargado | Certificación | Fecha emisión | Fecha caducidad | Estado |
|-----------|---------------|---------------|-----------------|--------|

### Resumen trimestral
- Encargados activos: X
- Contratos vigentes: X / Con renovación próxima: X / Vencidos: X
- Auditorías realizadas en el trimestre: X / Pendientes: X
- Acciones correctivas abiertas: X
- Incidentes reportados: X

## Configuración

- `encargados.registro`: ubicación del registro de encargados
- `encargados.frecuencia_auditoria_defecto`: meses entre auditorías (defecto: 12)
- `encargados.alerta_renovacion_dias`: días de antelación para renovación (defecto: 60)
- `encargados.verificar_certificaciones`: comprobar vigencia de certificaciones (defecto: true)
- `encargados.dpo_contacto`: DPO a notificar en caso de incidencias

## Escalado

- **Solo log**: todos los contratos vigentes, auditorías al día, sin incidencias
- **Notificación al DPO**: contrato próximo a vencer (≤60 días) o auditoría programada próxima
- **Alerta al equipo de privacidad**: contrato vencido o auditoría vencida sin reprogramar
- **Escalado urgente**: encargado sin contrato vigente que sigue tratando datos, o brecha detectada
