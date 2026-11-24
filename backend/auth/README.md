# Autenticación y autorización
Implementar aquí registro, inicio de sesión, emisión/validación de token y dependencias de autorización.

Roles definidos en la propuesta:
- `client`: consulta sus propios datos y solicita cotizaciones/reservaciones.
- `staff`: administra información operativa conforme a permisos.
- `admin`: administra usuarios, roles y configuración.

Regla obligatoria: el `user_id` y el rol se obtienen de la sesión/token validado en el backend. Nunca confiar en un `user_id` enviado libremente por el frontend o por el modelo de IA.
