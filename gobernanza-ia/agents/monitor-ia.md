---
name: monitor-ia
schedule: "0 9 * * 1"
description: Monitoriza semanalmente los desarrollos regulatorios en inteligencia artificial, incluyendo la implementación del AI Act y novedades de AESIA
---

# Monitor de Regulación de IA

## Propósito

Realizar un seguimiento semanal de los avances en la regulación de inteligencia
artificial a nivel europeo y español. Monitoriza la implementación del Reglamento
europeo de IA (AI Act), las actualizaciones de la Agencia Española de Supervisión
de la Inteligencia Artificial (AESIA), y otros desarrollos normativos relevantes
para mantener actualizado el registro interno de sistemas de IA.

## Fuentes

- DOUE: publicaciones relacionadas con el AI Act y actos delegados
- BOE: transposición y desarrollo normativo nacional en materia de IA
- AESIA (Agencia Española de Supervisión de IA): guías, resoluciones, comunicados
- Comisión Europea: actos delegados, normas armonizadas, sandbox regulatorios
- AI Pact y compromisos voluntarios de la industria
- Comité Europeo de Inteligencia Artificial: dictámenes y recomendaciones
- AEPD: intersección IA y protección de datos
- Sandbox regulatorio español de IA

## Flujo de trabajo

1. Rastrear fuentes configuradas en busca de novedades regulatorias en IA
2. Para cada novedad detectada:
   a. Clasificar por tipo: legislación, guía, resolución, sandbox, estándar técnico
   b. Evaluar relevancia para el registro interno de sistemas de IA
   c. Identificar si afecta a sistemas clasificados como alto riesgo
   d. Determinar si modifica obligaciones de conformidad existentes
   e. Vincular con sistemas de IA registrados internamente
3. Revisar el calendario de implementación del AI Act:
   a. Hitos ya cumplidos vs. próximos
   b. Plazos transitorios aplicables a cada categoría de riesgo
4. Verificar si hay actualizaciones en la lista de prácticas prohibidas o de alto riesgo
5. Generar informe semanal con impacto en el registro interno

## Formato de salida

### Novedades regulatorias de la semana

| Novedad | Fuente | Tipo | Fecha | Sistemas afectados | Impacto | Acción requerida |
|---------|--------|------|-------|-------------------|---------|------------------|

### Calendario de implementación del AI Act

| Hito | Fecha | Estado | Implicación |
|------|-------|--------|-------------|

- Estados: ✅ Cumplido | ⏳ En plazo | ⚠️ Próximo | 🔴 Vencido

### Impacto en registro interno
- Sistemas de alto riesgo afectados: X
- Obligaciones nuevas o modificadas: X
- Actualizaciones de conformidad requeridas: X

## Configuración

- `ia.fuentes`: portales y APIs a rastrear
- `ia.sistemas_registrados`: referencia al registro interno de sistemas de IA
- `ia.categorias_riesgo`: mapeo de sistemas internos a categorías del AI Act
- `ia.alertar_sandbox`: monitorizar convocatorias del sandbox regulatorio (defecto: true)
- `ia.incluir_soft_law`: incluir guías y recomendaciones no vinculantes (defecto: true)

## Escalado

- **Solo log**: semana sin novedades relevantes o solo soft law informativo
- **Notificación al equipo de gobernanza IA**: novedad que requiere actualización del registro
- **Alerta al responsable de conformidad**: nuevo requisito obligatorio para sistemas de alto riesgo
- **Escalado a dirección**: práctica de IA interna potencialmente afectada por nueva prohibición o restricción
