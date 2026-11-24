# MongoDB — `eventia_management`

En esta base de datos se guardará la información relacionada con los eventos y los servicios que ofrecerá Eventia. Se utilizará MongoDB para almacenar los datos de las reservaciones, paquetes, servicios, cotizaciones y conversaciones con el asistente de IA.

Se tendrán las siguientes colecciones:

- **events:** aquí se guardará la información de los eventos, como su nombre, fecha, horario, espacio, cliente y estado.
- **reservations:** contendrá los datos de las reservaciones, el usuario que las solicita, la fecha del evento y su estado.
- **packages:** se guardarán los paquetes disponibles, sus precios, descripciones y los servicios que incluyen.
- **services:** tendrá la información de los servicios que ofrece Eventia, junto con sus costos y disponibilidad.
- **quotations:** aquí se almacenarán las cotizaciones, los servicios solicitados, las cantidades y el total estimado.
- **chat_history:** guardará las conversaciones que tengan los usuarios con el asistente de IA.

También se agregarán algunos índices para facilitar las búsquedas de información, por ejemplo, para encontrar reservaciones por usuario y fecha, consultar eventos y revisar el historial de conversaciones.

```javascript
db.reservations.createIndex({ user_id: 1, event_date: 1 })
db.events.createIndex({ event_date: 1, space_id: 1 })
db.packages.createIndex({ name: 1 }, { unique: true })
db.chat_history.createIndex({ user_id: 1, created_at: -1 })
```

El campo `user_id` se utilizará para relacionar la información de los usuarios con PostgreSQL, donde se guardarán sus cuentas. Esta relación se validará desde el backend para evitar que se consulte información de otros usuarios.
