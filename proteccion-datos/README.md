# Protección de Datos — Operativo

Este módulo cubre la gestión operativa diaria de protección de datos: registro de actividades de tratamiento, evaluaciones de impacto, gestión de brechas de seguridad y relación con la AEPD. Complementa al módulo de privacidad (compliance) con herramientas de trabajo práctico del DPO o responsable de protección de datos. Pensado para DPOs internos y externos, responsables de seguridad de la información y equipos de compliance operativo.

## Skills disponibles

| Skill | Comando | Descripción |
|-------|---------|-------------|
| RAT | `/rat` | Genera y mantiene el Registro de Actividades de Tratamiento conforme al art. 30 RGPD |
| EIPD | `/eipd` | Guía la elaboración de Evaluaciones de Impacto en Protección de Datos paso a paso |
| Brecha | `/brecha` | Gestiona la notificación de brechas de seguridad (art. 33-34 RGPD): evaluación, plazos y comunicación |
| AEPD | `/aepd` | Asiste en la preparación de respuestas y documentación para procedimientos ante la AEPD |

## Primeros pasos

1. Ejecuta la entrevista inicial del proyecto para configurar tu perfil y preferencias.
2. Prueba `/rat` para generar el registro de actividades de tratamiento de tu organización.
3. Usa `/brecha` ante un incidente de seguridad para gestionar los plazos de notificación (72 horas).
4. Ejecuta `/eipd` cuando inicies un tratamiento que requiera evaluación de impacto.

## Casos de uso típicos

- Creación del RAT completo de una organización a partir de entrevistas con los departamentos.
- Gestión de una brecha de datos: evaluación de riesgo, decisión de notificación a la AEPD y comunicación a los afectados.
- Elaboración de una EIPD para un nuevo sistema de monitorización de empleados.
- Preparación de la respuesta a un requerimiento de información de la AEPD en un procedimiento sancionador.

## Legislación de referencia

- **RGPD** — Reglamento (UE) 2016/679, de 27 de abril de 2016, General de Protección de Datos
- **LOPDGDD** — Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales
- **Guías AEPD** — Guías y directrices publicadas por la Agencia Española de Protección de Datos
- **ENS** — Real Decreto 311/2022, de 3 de mayo, Esquema Nacional de Seguridad

## Lo que este plugin no hace

- **No realiza auditoría técnica de seguridad informática**: no ejecuta análisis de vulnerabilidades, pentesting ni revisiones de configuración de sistemas.
- **No realiza pentesting**: no simula ataques ni pruebas de intrusión en infraestructuras TI.
- **No notifica brechas a la AEPD**: no envía comunicaciones formales a través del canal de la Agencia.
- **No sustituye el criterio profesional** del DPO o abogado: las recomendaciones deben ser validadas por un profesional cualificado.

## Navegación

- [Volver al README principal](../README.md)
