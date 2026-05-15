# Mercantil — Contratos mercantiles

Este módulo asiste en la revisión, gestión y seguimiento de contratos mercantiles: compraventas, distribución, agencia, suministro, franquicia y cualquier acuerdo entre empresas. Permite detectar cláusulas problemáticas, controlar vencimientos, preparar adendas de forma estructurada y escalar resúmenes ejecutivos a socios o clientes. Funciona tanto para el lado de ventas (la empresa como proveedor) como para el lado de compras (la empresa como cliente), adaptando el análisis de riesgos según la posición contractual.

## Skills disponibles

| Skill | Comando | Descripción |
|-------|---------|-------------|
| Revisión de contrato | `/revision` | Analiza un contrato mercantil e identifica riesgos, cláusulas abusivas y omisiones relevantes |
| Historial de adendas | `/historial-adendas` | Genera un cuadro cronológico de todas las modificaciones contractuales |
| Escalado | `/escalado` | Prepara un resumen ejecutivo del contrato para escalar a socio o cliente |
| Renovaciones | `/renovaciones` | Controla fechas de vencimiento y condiciones de renovación tácita o expresa |

## Primeros pasos

1. Ejecuta la entrevista inicial del proyecto para configurar tu perfil y preferencias.
2. Prueba `/revision` con un contrato de distribución o suministro para ver el análisis de riesgos.
3. Usa `/renovaciones` para crear un calendario de vencimientos de tu cartera contractual.
4. Configura `/escalado` para generar resúmenes adaptados al interlocutor (socio, cliente, dirección).

## Casos de uso típicos

- Revisión de un contrato SaaS recibido de un proveedor tecnológico.
- Análisis de cláusulas de limitación de responsabilidad e indemnización en un acuerdo de distribución.
- Control de renovaciones tácitas para evitar compromisos plurianuales no deseados.
- Preparación de un cuadro comparativo de adendas para una negociación en curso.

## Legislación de referencia

- **Código Civil** (arts. 1254-1314 — obligaciones y contratos)
- **Código de Comercio** (Real Decreto de 22 de agosto de 1885 — contratos mercantiles, compraventa mercantil, comisión, depósito)
- **LSSI-CE** — Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (contratación electrónica)
- **LCGC** — Ley 7/1998, sobre Condiciones Generales de la Contratación (control de inclusión y contenido)

## Lo que este plugin no hace

- **No proporciona asesoramiento fiscal** sobre la tributación de contratos (IVA, retenciones, precios de transferencia).
- **No gestiona litigio contractual**: no redacta demandas, contestaciones ni recursos derivados de incumplimientos.
- **No ejecuta firmas electrónicas**: no firma ni envía contratos a través de plataformas de firma digital.
- **No sustituye el criterio profesional** del abogado: las sugerencias deben ser revisadas por un letrado colegiado.

## Navegación

- [Volver al README principal](../README.md)
