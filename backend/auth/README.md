Autenticación y autorización

En esta parte del proyecto se desarrollará el sistema de autenticación y autorización de Eventia, el cual permitirá que los usuarios puedan registrarse e iniciar sesión para acceder a las funcionalidades de la aplicación.

Se implementará el registro de usuarios, el inicio y cierre de sesión, así como la generación y validación de tokens para mantener identificada la sesión de cada usuario.

También se manejarán tres tipos de roles, dependiendo de las funciones que tendrá cada usuario dentro de la plataforma:

- **client:** podrá consultar paquetes y servicios, revisar sus propios datos y realizar solicitudes de cotización y reservación.
- **staff:** tendrá acceso a las funciones relacionadas con la administración de la información operativa de Eventia, de acuerdo con los permisos asignados.
- **admin:** podrá administrar los usuarios, asignar roles y modificar la configuración general del sistema.

La validación de los permisos se realizará desde el backend, utilizando la información de la sesión del usuario. De esta manera, cada persona únicamente podrá acceder a las funciones y datos que le correspondan según su rol.

El identificador del usuario y sus permisos no se tomarán directamente de los datos enviados desde el frontend ni de las respuestas del asistente de inteligencia artificial, sino de la sesión previamente validada.
