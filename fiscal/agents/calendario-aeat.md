---
name: calendario-aeat
schedule: "0 9 1 * *"
description: Genera el calendario de obligaciones fiscales del mes con modelos, plazos y estado de cumplimiento
---

# Calendario de Obligaciones Fiscales AEAT

## Propósito

Generar mensualmente el calendario de obligaciones tributarias de la entidad
ante la Agencia Estatal de Administración Tributaria (AEAT) y, en su caso,
las haciendas forales o autonómicas. Permite al equipo fiscal y contable
planificar con antelación la preparación y presentación de declaraciones,
evitando recargos por presentación extemporánea.

## Fuentes

- Calendario del contribuyente de la AEAT (publicación anual)
- Perfil fiscal de la entidad: forma jurídica, régimen IVA, obligaciones específicas
- Modelos tributarios aplicables a la entidad
- Registro de presentaciones anteriores (modelo, período, fecha, resultado)
- Calendario de festivos nacionales y autonómicos (afecta a plazos)
- Haciendas forales aplicables (País Vasco, Navarra) si procede

## Flujo de trabajo

1. Cargar el perfil fiscal de cada entidad gestionada
2. Identificar los modelos tributarios a presentar en el mes en curso:
   - Autoliquidaciones mensuales: Modelo 303 (IVA), 111 (retenciones IRPF),
     115 (retenciones alquileres), 123 (retenciones capital mobiliario)
   - Autoliquidaciones trimestrales (si aplica): mismos modelos para pymes
   - Declaraciones informativas: 347, 349, 720, etc.
   - Pagos fraccionados: Modelo 202 (IS), 130/131 (IRPF)
   - Impuesto sobre Sociedades: Modelo 200 (julio, plazo 25 días tras 6 meses)
   - Cuentas anuales e IS: coordinar con módulo societario
3. Para cada obligación:
   a. Verificar el plazo exacto de presentación (día del mes)
   b. Comprobar si hay aplazamientos o fraccionamientos vigentes
   c. Verificar el estado de preparación (datos disponibles, borrador, revisado)
   d. Calcular días restantes hasta el vencimiento
4. Generar el calendario mensual con todas las obligaciones

## Formato de salida

### Obligaciones fiscales — [Mes Año]

| Modelo | Concepto | Período | Plazo presentación | Días restantes | Estado | Responsable |
|--------|----------|---------|--------------------|----------------|--------|-------------|

- Estados: ✅ Presentado | 📝 En preparación | ⏳ Pendiente | 🔴 Vencido

### Aplazamientos vigentes

| Referencia | Importe pendiente | Próximo vencimiento | Estado |
|------------|-------------------|---------------------|--------|

### Resumen del mes
- Obligaciones del mes: X
- Ya presentadas: X
- En preparación: X
- Pendientes de iniciar: X
- Importe estimado total: X EUR

## Configuración

- `fiscal.entidades`: lista de entidades con su perfil fiscal
- `fiscal.regimen_iva`: mensual o trimestral por entidad
- `fiscal.hacienda`: AEAT, Hacienda Foral de Bizkaia/Gipuzkoa/Araba, Navarra
- `fiscal.modelos_aplicables`: lista de modelos por entidad
- `fiscal.responsable_fiscal`: persona responsable por defecto
- `fiscal.alerta_anticipacion_dias`: días de antelación para alertar (defecto: 10)

## Escalado

- **Solo log**: todas las obligaciones presentadas o con más de 15 días de margen
- **Notificación al responsable fiscal**: obligación a menos de 10 días sin borrador preparado
- **Alerta al equipo**: obligación a menos de 5 días sin datos completos
- **Escalado a dirección financiera**: riesgo de presentación extemporánea con recargo
