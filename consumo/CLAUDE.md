<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /consumo:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /consumo:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/consumo/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho de Consumo

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/consumo:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo encargado de derecho de consumo lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos aproximadamente [N] reclamaciones/consultas de consumo al mes.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Asociación de consumidores]

**Sector:** [PLACEHOLDER — ej., "E-commerce, retail, telecomunicaciones, banca, seguros, viajes, alimentación"]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a colegiado/a | Responsable de atención al cliente con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Canales de venta

| Canal | Activo | Normativa específica | Notas |
|---|---|---|---|
| Online (web propia) | [PLACEHOLDER ✓/✗] | LGDCU + LSSI-CE | [PLACEHOLDER — ej., "Tienda Shopify / WooCommerce / desarrollo propio"] |
| Online (marketplace) | [PLACEHOLDER ✓/✗] | LGDCU + LSSI-CE + condiciones marketplace | [PLACEHOLDER — ej., "Amazon, eBay, Wallapop Pro"] |
| Presencial (tienda física) | [PLACEHOLDER ✓/✗] | LGDCU | [PLACEHOLDER] |
| Teléfono | [PLACEHOLDER ✓/✗] | LGDCU art. 92 + normativa autonómica | [PLACEHOLDER] |
| Mixto (click & collect) | [PLACEHOLDER ✓/✗] | LGDCU | [PLACEHOLDER] |

**CCAA con operaciones:** [PLACEHOLDER — ej., "Madrid, Cataluña, Andalucía" — relevante por normativa autonómica de consumo]

---

## Condiciones generales de contratación

### Control de inclusión (art. 5 LCGC)

**Requisitos cumplidos:**
- [ ] Información previa sobre existencia de CGC
- [ ] Entrega o puesta a disposición antes de la contratación
- [ ] Redacción clara, concreta y sencilla
- [ ] Accesibilidad y legibilidad (tamaño de fuente, contraste)
- [ ] Aceptación expresa (no casillas premarcadas)
- [PLACEHOLDER — requisitos adicionales del sector]

**Estado de las CGC:** [PLACEHOLDER — ej., "Última revisión DD/MM/AAAA; redactadas por despacho X; revisión anual"]

### Control de contenido (arts. 82-91 LGDCU)

**Cláusulas revisadas contra el listado de cláusulas abusivas:**
- [ ] Art. 85 LGDCU — vinculación del contrato a la voluntad del empresario
- [ ] Art. 86 LGDCU — limitación de derechos del consumidor
- [ ] Art. 87 LGDCU — falta de reciprocidad
- [ ] Art. 88 LGDCU — garantías
- [ ] Art. 89 LGDCU — cláusulas abusivas en contratos con consumidores (numerus apertus art. 82)
- [PLACEHOLDER — cláusulas específicas del sector bajo vigilancia]

**Posición house:** [PLACEHOLDER — ej., "Revisión semestral de CGC contra jurisprudencia reciente del TS sobre cláusulas abusivas; consultar siempre con letrado antes de modificar"]

### Doble clic / Contratación electrónica

**Proceso de contratación online:** [PLACEHOLDER — ej., "1) Selección producto → 2) Resumen pedido → 3) Aceptación CGC (checkbox no premarcado) → 4) Confirmación pedido → 5) Email de confirmación (art. 28 LSSI-CE)"]

**Información precontractual obligatoria (art. 97 LGDCU para contratos a distancia):**
- [ ] Características principales del bien/servicio
- [ ] Identidad y dirección del empresario
- [ ] Precio total con impuestos incluidos
- [ ] Gastos de envío
- [ ] Forma de pago, entrega y ejecución
- [ ] Derecho de desistimiento (o su exclusión motivada)
- [ ] Garantía legal
- [ ] Duración del contrato y condiciones de resolución
- [ ] Funcionalidad e interoperabilidad (contenido digital)

---

## Derecho de desistimiento

**Plazo:** 14 días naturales desde recepción del bien / celebración del contrato de servicios (art. 102 LGDCU)

**Plazo ampliado por falta de información:** 12 meses + 14 días si no se informó del derecho (art. 105 LGDCU)

**Excepciones aplicables al negocio (art. 103 LGDCU):**
- [PLACEHOLDER — marcar las que apliquen:
  - [ ] Bienes precintados no aptos para devolución por higiene/salud
  - [ ] Bienes personalizados o confeccionados a medida
  - [ ] Contenido digital sin soporte material con ejecución comenzada con consentimiento
  - [ ] Servicios completamente ejecutados con consentimiento previo
  - [ ] Bienes que se mezclan de forma indisociable con otros
  - [ ] Prensa periódica
  - [ ] Alojamiento, transporte, comida en fecha determinada (viajes)
  - [ ] Suministro de bienes precintados que por su naturaleza no son aptos para ser devueltos]

**Formulario de desistimiento:** [PLACEHOLDER — ej., "Disponible en web + incluido en email de confirmación de pedido; modelo del Anexo B LGDCU"]

**Proceso de devolución del importe:** [PLACEHOLDER — ej., "Reembolso en 14 días desde la comunicación de desistimiento; mismo medio de pago; podemos retener hasta recibir los bienes (art. 107 LGDCU)"]

**Coste de devolución:** [PLACEHOLDER — ej., "A cargo del consumidor si se informó previamente; a cargo de la empresa si no se informó"]

---

## Garantías

### Garantía legal (art. 114-126 LGDCU)

**Plazo:** 3 años desde la entrega del bien (desde reforma por Directiva 2019/771, transpuesta por RDL 7/2021)

**Presunción de falta de conformidad:** 2 años desde la entrega (el defecto se presume preexistente)

**Remedios del consumidor (art. 118-122 LGDCU):**
1. Reparación o sustitución (primera opción del consumidor)
2. Reducción del precio
3. Resolución del contrato

**Posición house:** [PLACEHOLDER — ej., "Ofrecer siempre reparación/sustitución primero; aceptar resolución si no es posible o no se realiza en plazo razonable; documentar toda reclamación"]

### Garantía comercial

**¿Se ofrece garantía comercial adicional?** [PLACEHOLDER — Sí / No]
**Condiciones:** [PLACEHOLDER — ej., "2 años adicionales a la garantía legal; cubre XYZ; excluye ABC; documento de garantía según art. 125 LGDCU"]
**Obligaciones del documento de garantía (art. 125 LGDCU):**
- [ ] Indicar que no afecta a los derechos legales del consumidor
- [ ] Contenido, duración, ámbito territorial, vías de reclamación

---

## Claims de marketing — Control de legalidad

### Publicidad engañosa (art. 5 LCD)

**Posición house:** [PLACEHOLDER — ej., "Toda afirmación sobre el producto debe ser verificable y documentada; claims de salud solo con respaldo científico; claims ambientales según directrices UE sobre greenwashing"]

**Claims de alto riesgo que requieren revisión legal previa:**
- [PLACEHOLDER — ej., "Claims de salud/bienestar"]
- [PLACEHOLDER — ej., "Claims medioambientales/sostenibilidad (greenwashing)"]
- [PLACEHOLDER — ej., "Superlativos ('el mejor', 'el primero', 'el único')"]
- [PLACEHOLDER — ej., "Comparativas con competidores (art. 10 LCD)"]
- [PLACEHOLDER — ej., "Testimonios y opiniones de clientes"]

### Publicidad comparativa (art. 10 LCD)

**Requisitos para que sea lícita:**
- Bienes/servicios con la misma finalidad
- Comparación objetiva y verificable
- No denigrante ni confusoria
- No aprovechamiento indebido de reputación ajena

**Posición house:** [PLACEHOLDER — ej., "Evitar publicidad comparativa directa salvo que el departamento jurídico apruebe; comparativa genérica permitida"]

### Influencers y publicidad en redes sociales

**Posición house:** [PLACEHOLDER — ej., "Identificación obligatoria como publicidad (#publi #ad); contrato escrito con cláusula de cumplimiento legal; aprobación previa del contenido; cumplimiento Código de Conducta sobre publicidad en redes sociales de Autocontrol"]

---

## Lanzamiento de producto — Checklist de riesgo

**Antes de lanzar un producto/servicio B2C, verificar:**

- [ ] Información precontractual completa (art. 97 LGDCU si venta a distancia)
- [ ] CGC revisadas y actualizadas
- [ ] Política de devoluciones/desistimiento visible y correcta
- [ ] Etiquetado y marcado CE si aplica
- [ ] Claims de marketing revisados por legal
- [ ] Política de privacidad y cookies actualizada
- [ ] Precio final con impuestos visible (art. 60 LGDCU)
- [ ] Desglose de gastos de envío
- [ ] Botón de pedido con obligación de pago (art. 98.7 LGDCU: "Pedido con obligación de pago")
- [ ] Canal de atención al cliente / reclamaciones disponible
- [ ] Hojas de reclamaciones disponibles (si venta presencial)
- [ ] Registro en plataforma ODR si venta online en la UE
- [PLACEHOLDER — ítems adicionales específicos del sector]

**Aprobación necesaria:** [PLACEHOLDER — ej., "Checklist firmado por responsable jurídico y responsable de marketing"]

---

## Hojas de reclamaciones

**Obligatoriedad:** [PLACEHOLDER — ej., "Obligatorio en establecimiento físico por normativa autonómica de [CCAA]; no obligatorio online pero sí recomendable tener canal de reclamaciones"]

**Normativa autonómica aplicable:** [PLACEHOLDER — ej., "Decreto XX/XXXX de la Comunidad de Madrid sobre hojas de reclamaciones"]

**Proceso interno de gestión:**
1. [PLACEHOLDER — ej., "Recepción de la hoja de reclamaciones"]
2. [PLACEHOLDER — ej., "Registro en sistema interno (24h)"]
3. [PLACEHOLDER — ej., "Respuesta al consumidor en 10 días hábiles"]
4. [PLACEHOLDER — ej., "Envío de copia a la Administración si procede"]
5. [PLACEHOLDER — ej., "Seguimiento hasta resolución"]

---

## Arbitraje de consumo

**Adhesión al Sistema Arbitral de Consumo:** [PLACEHOLDER — Sí (total/limitada) / No]

**Junta Arbitral competente:** [PLACEHOLDER — ej., "Junta Arbitral de Consumo de Madrid"]

**Limitaciones a la adhesión:** [PLACEHOLDER — ej., "Excluidas reclamaciones >€X; excluidos temas de intoxicación/lesiones; excluidos servicios financieros"]

**Posición house:** [PLACEHOLDER — ej., "Adherirse al arbitraje como señal de confianza; participar activamente en la mediación previa; cumplir laudos dentro del plazo"]

---

## Acciones colectivas

**Directiva UE 2020/1828 (acciones de representación):**
- Transpuesta por [PLACEHOLDER — ej., "Pendiente de transposición completa / Ley XX/XXXX"]
- Entidades legitimadas para accionar: asociaciones de consumidores (art. 11 LEC, art. 37 LGDCU)
- Acción de cesación + acción de reparación

**Posición house ante acciones colectivas:**
- [PLACEHOLDER — ej., "Escalar inmediatamente a socio/a responsable y despacho externo; revisar seguro de RC; preparar defensa proactiva"]

**Monitorización de riesgo:**
- [PLACEHOLDER — ej., "Vigilar reclamaciones recurrentes (>X reclamaciones sobre el mismo tema en Y meses = alerta)"]
- [PLACEHOLDER — ej., "Monitorizar redes sociales y plataformas de opinión"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Atención al cliente] | [PLACEHOLDER — ej., "Reclamaciones rutinarias, devoluciones estándar, información"] | [Responsable jurídico/consumo] | [método] |
| [Responsable jurídico/consumo] | [PLACEHOLDER — ej., "Reclamaciones complejas, hojas de reclamaciones, consultas de CGC"] | [Socio/a / dirección] | [método] |
| [Socio/a / dirección] | [PLACEHOLDER — ej., "Todo excepto acciones colectivas y sanciones administrativas"] | [Despacho externo / comité de dirección] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda demanda colectiva, toda sanción de consumo, toda inspección, reclamaciones de asociaciones de consumidores, retirada de producto"]

---

## Estilo house

**Formato de respuesta a reclamaciones:** [PLACEHOLDER — ej., "Modelo house: acuse de recibo (24h) → investigación interna → respuesta motivada (máx. 10 días hábiles)"]
**Tono en comunicaciones con consumidores:** [PLACEHOLDER — ej., "Empático, claro, sin tecnicismos; ofrecer solución concreta"]
**Citas normativas:** [PLACEHOLDER — ej., "art. 102 LGDCU, art. 5 LCD, art. 21 LSSI-CE"]
**Idioma:** [PLACEHOLDER — ej., "Español; catalán/euskera/gallego según CCAA del consumidor si lo solicita"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **LGDCU** — Ley General para la Defensa de los Consumidores y Usuarios (Real Decreto Legislativo 1/2007, de 16 de noviembre)
- **LCD** — Ley de Competencia Desleal (Ley 3/1991, de 10 de enero)
- **LCGC** — Ley de Condiciones Generales de la Contratación (Ley 7/1998, de 13 de abril)
- **LSSI-CE** — Ley de Servicios de la Sociedad de la Información y Comercio Electrónico (Ley 34/2002, de 11 de julio)
- **LGP** — Ley General de Publicidad (Ley 34/1988, de 11 de noviembre)
- **Directiva 2011/83/UE** sobre derechos de los consumidores
- **Directiva 2019/771/UE** sobre compraventa de bienes (transpuesta por RDL 7/2021)
- **Directiva 2019/770/UE** sobre contenido y servicios digitales (transpuesta por RDL 7/2021)
- **Directiva 2020/1828/UE** sobre acciones de representación para la protección de los intereses colectivos de los consumidores
- **Normativa autonómica de consumo** (según CCAA de operación)
- **Reglamento ODR** (Reglamento UE 524/2013) — plataforma de resolución de litigios en línea

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/consumo:entrevista-inicial --repetir`*
