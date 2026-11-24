# MongoDB — `eventia_management`
MongoDB almacena los datos operativos. El `user_id` corresponde al UUID de `users.id` en PostgreSQL y se utiliza como referencia lógica validada por el backend.

## Colecciones propuestas
- `events`: nombre, fecha, horario, espacio, cliente, tipo y estado.
- `reservations`: `user_id`, `event_id`, fecha de solicitud, fecha del evento, estado y observaciones.
- `packages`: nombre, descripción, precio y servicios incluidos.
- `services`: nombre, descripción, costo y disponibilidad.
- `quotations`: cliente, servicios, cantidades, costos y total estimado.
- `chat_history`: `user_id`, mensajes y fecha de conversación.

## Índices iniciales sugeridos
```javascript
db.reservations.createIndex({ user_id: 1, event_date: 1 })
db.events.createIndex({ event_date: 1, space_id: 1 })
db.packages.createIndex({ name: 1 }, { unique: true })
db.chat_history.createIndex({ user_id: 1, created_at: -1 })
```
Los nombres y tipos definitivos de campos deberán mantenerse consistentes con los modelos y validaciones del backend.
