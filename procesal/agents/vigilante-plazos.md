---
name: vigilante-plazos
schedule: "0 8 * * *"
description: Monitoriza diariamente los plazos procesales de asuntos abiertos, alertando con semáforo sobre vencimientos en los próximos 7 días
---

# Vigilante de Plazos Procesales

## Propósito

Control diario de todos los plazos procesales activos en los asuntos judiciales
y arbitrales en curso. Los plazos procesales son improrrogables y su incumplimiento
puede suponer la pérdida de derechos, por lo que este agente constituye una red
de seguridad crítica para el departamento jurídico.

## Fuentes

- Registro de asuntos judiciales abiertos (jurisdicción, procedimiento, juzgado)
- Calendario de plazos procesales por asunto
- Notificaciones judiciales recibidas (LexNET, Justicia Digital)
- Ley de Enjuiciamiento Civil y Ley de Enjuiciamiento Criminal: plazos legales
- Ley reguladora de la Jurisdicción Contencioso-Administrativa
- Calendario de días hábiles/inhábiles del partido judicial correspondiente

## Flujo de trabajo

1. Cargar todos los asuntos con plazos activos
2. Verificar el calendario de días hábiles (excluir fines de semana, festivos nacionales,
   autonómicos y locales del partido judicial)
3. Para cada plazo activo:
   a. Calcular días hábiles restantes hasta vencimiento
   b. Clasificar por semáforo:
      - 🔴 Rojo: vence hoy o mañana (1-2 días hábiles)
      - 🟠 Ámbar: vence en 3-5 días hábiles
      - 🟢 Verde: vence en 6-7 días hábiles
   c. Verificar si hay escritos en preparación para ese plazo
   d. Identificar al letrado responsable
4. Ordenar por urgencia (días hábiles restantes ascendente)
5. Verificar si hay notificaciones pendientes de lectura en LexNET
6. Generar informe diario

## Formato de salida

### Plazos próximos (7 días hábiles)

| Asunto | Procedimiento | Juzgado | Plazo | Vencimiento | Días hábiles | Semáforo | Letrado | Estado escrito |
|--------|---------------|---------|-------|-------------|--------------|----------|---------|----------------|

### Notificaciones pendientes
- Notificaciones sin leer en LexNET: X

### Resumen diario
- Plazos que vencen hoy: X
- Plazos en zona roja: X
- Plazos en zona ámbar: X
- Total plazos activos en 7 días: X

## Configuración

- `plazos.dias_horizonte`: días hábiles a mostrar (defecto: 7)
- `plazos.partidos_judiciales`: lista de partidos con sus calendarios de festivos
- `plazos.hora_envio`: hora de envío del informe diario (defecto: 08:00)
- `plazos.lexnet_check`: verificar notificaciones pendientes (defecto: true)

## Escalado

- **Solo log**: todos los plazos en verde, sin notificaciones pendientes
- **Notificación al letrado**: plazo en zona ámbar sin escrito en preparación
- **Alerta urgente al letrado y responsable procesal**: plazo en zona roja
- **Escalado a dirección jurídica**: plazo que vence hoy sin escrito preparado
- **Alerta crítica**: notificación en LexNET sin leer con más de 24 horas
