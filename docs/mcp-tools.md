# Contratos iniciales de herramientas MCP

| Herramienta | Entradas principales | Salida esperada | Base |
|---|---|---|---|
| `get_packages` | filtros opcionales | paquetes y precios | MongoDB |
| `check_availability` | fecha, hora inicio/fin, espacio | disponibilidad y conflictos | MongoDB |
| `create_quotation` | servicios y cantidades | partidas, subtotal y total | MongoDB |
| `get_reservations` | filtros permitidos | reservaciones autorizadas | PostgreSQL + MongoDB |
| `create_reservation` | fecha, espacio y detalles | identificador y estado | PostgreSQL + MongoDB |
| `get_event_details` | `event_id` | detalle autorizado del evento | PostgreSQL + MongoDB |

## Reglas comunes
- El contexto de usuario autenticado debe proceder del backend.
- Validar tipos, rangos y campos obligatorios.
- No aceptar consultas SQL/NoSQL arbitrarias.
- Aplicar autorización por rol y propiedad.
- Las herramientas de escritura requieren validación previa y registro de errores.
- No devolver contraseñas, tokens, datos de pago ni información ajena al usuario.

**Estado:** las funciones del servidor son esqueletos de contrato; devolver `not_implemented` no cuenta como herramienta funcional para la evaluación. Conectar cada herramienta a servicios reales y probar llamadas desde el cliente MCP.
