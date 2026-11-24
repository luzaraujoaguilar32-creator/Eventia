 MongoDB — `eventia_management`

En esta parte del proyecto se utilizará MongoDB para almacenar la información relacionada con la administración y organización de los eventos dentro de Eventia.

La base de datos se llamará `eventia_management` y permitirá guardar información sobre los eventos, reservaciones, paquetes, servicios, cotizaciones y conversaciones realizadas mediante el asistente de inteligencia artificial.

## Colecciones propuestas

Se crearán las siguientes colecciones para organizar la información del sistema:

- **events:** almacenará los datos de los eventos, como nombre, fecha, horario, espacio donde se realizará, cliente, tipo de evento y estado.
- **reservations:** guardará las solicitudes de reservación, incluyendo el identificador del usuario, el evento relacionado, la fecha de solicitud, la fecha del evento, su estado y observaciones.
- **packages:** contendrá la información de los paquetes disponibles, como nombre, descripción, precio y servicios que incluyen.
- **services:** almacenará los servicios que ofrece Eventia, junto con su descripción, costo y disponibilidad.
- **quotations:** permitirá guardar las cotizaciones realizadas, incluyendo los servicios solicitados, cantidades, costos y total estimado.
- **chat_history:** se utilizará para almacenar el historial de conversaciones de los usuarios con el asistente de inteligencia artificial, junto con la fecha de cada conversación.

## Índices iniciales

Se crearán algunos índices en MongoDB para facilitar las búsquedas y mejorar el acceso a la información. Entre los índices que se tienen contemplados se encuentran:

```javascript
db.reservations.createIndex({ user_id: 1, event_date: 1 })
db.events.createIndex({ event_date: 1, space_id: 1 })
db.packages.createIndex({ name: 1 }, { unique: true })
db.chat_history.createIndex({ user_id: 1, created_at: -1 })
```

Estos índices permitirán consultar las reservaciones por usuario y fecha, localizar eventos según su fecha y espacio, evitar que existan paquetes con el mismo nombre y consultar el historial de conversaciones de cada usuario.

El identificador `user_id` se relacionará con el UUID del usuario registrado en PostgreSQL, que será la base de datos encargada de almacenar la información principal de las cuentas. Esta relación se validará desde el backend para mantener la consistencia entre ambas bases de datos.

Los nombres y tipos de los campos se definirán de acuerdo con los modelos que se desarrollen durante la implementación del sistema.
