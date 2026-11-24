# Eventia
**Aplicación web para la gestión inteligente de eventos y reservaciones mediante IA y MCP.**

## Datos del equipo
- **Asignatura:** Programación Lógica y Funcional
- **Grupo/equipo:** PLYF
- **Docente:** Alvarez Aspeitia Mauricio Alberto
- **Integrantes:**
  - Luz Karina Araujo Aguilar
  - Carlos Emanuel Lopez Villanueva

> Los nombres de usuario de GitHub y la URL del repositorio están pendientes de agregar.

## Objetivo
Desarrollar una aplicación web para administrar clientes, eventos, espacios, paquetes, servicios, cotizaciones y reservaciones. El asistente de IA será la interfaz principal para consultar y ejecutar operaciones autorizadas mediante un cliente MCP y un servidor MCP.

## Arquitectura y tecnologías
| Componente | Tecnología | Responsabilidad |
|---|---|---|
| Interfaz web | Streamlit | Pantallas y chat |
| API | FastAPI | Autenticación, autorización y lógica de negocio |
| Cliente MCP | Python + SDK oficial MCP | Descubrir e invocar herramientas |
| Servidor MCP | Python + SDK oficial MCP | Exponer herramientas autorizadas |
| IA | API de un modelo de lenguaje | Interpretar solicitudes y redactar respuestas |
| Base de datos 1 | PostgreSQL (`eventia_users`) | Usuarios, roles y suscripciones |
| Base de datos 2 | MongoDB (`eventia_management`) | Eventos, reservaciones, paquetes, servicios, cotizaciones y chat |
| Pagos | Stripe | Suscripciones de prueba y webhooks |

## Estructura
- `frontend/`: interfaz Streamlit.
- `backend/`: API FastAPI, autenticación y servicios.
- `mcp_server/`: servidor y herramientas MCP.
- `mcp_client/`: cliente MCP.
- `ai/`: integración del modelo de IA.
- `database/`: conexiones, esquema SQL e índices/documentos MongoDB.
- `payments/`: integración Stripe y webhooks.
- `tests/`: pruebas iniciales.
- `docs/`: arquitectura, datos, MCP, pagos y evidencias.
- `scripts/`: inicialización y utilidades.

## Requisitos
- Python 3.11 o superior.
- PostgreSQL.
- MongoDB.
- Una clave de API del proveedor de IA elegido.
- Cuenta Stripe en modo de prueba.

## Instalación inicial
1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Copiar `.env.example` a `.env` y completar las variables localmente.
5. Crear la base PostgreSQL `eventia_users`.
6. Crear la base MongoDB `eventia_management`.
7. Ejecutar la API:
   ```bash
   uvicorn backend.main:app --reload
   ```
8. En otra terminal, iniciar Streamlit:
   ```bash
   streamlit run frontend/app.py
   ```

## Variables de entorno
Consultar `.env.example`. No subir `.env`, contraseñas, tokens ni claves al repositorio.

## Bases de datos
- PostgreSQL administra identidad, roles y suscripciones. Su esquema inicial está en `database/postgres/schema.sql`.
- MongoDB almacena datos operativos. La estructura propuesta y los índices están en `database/mongodb/README.md`.

La relación entre ambas bases se realiza mediante `user_id`: el identificador del usuario de PostgreSQL se guarda como referencia en los documentos MongoDB. El backend valida la existencia y los permisos; no se configura una relación SQL directa entre motores.

## Herramientas MCP propuestas
1. `get_packages`
2. `check_availability`
3. `create_quotation`
4. `get_reservations`
5. `create_reservation`
6. `get_event_details`

Los contratos iniciales están documentados en `docs/mcp-tools.md`. Las herramientas marcadas como pendientes deben implementarse y probarse antes de presentarlas como funcionales.

## Pagos
Stripe se utilizará para una suscripción de prueba Free/Premium. El backend crea la sesión de Checkout y actualiza PostgreSQL únicamente después de verificar la firma del webhook. Los pagos de anticipos o reservaciones de eventos quedan fuera del alcance inicial.

## Seguridad
- Contraseñas con hash seguro (bcrypt).
- Autorización en backend, no en el frontend ni en el modelo de IA.
- Filtrado por `user_id` y rol.
- Validación de entradas.
- HTTPS en producción.
- Secretos mediante variables de entorno.
- Webhooks verificados con la firma de Stripe.
- MCP con permisos mínimos y sin consultas arbitrarias a bases de datos.

## Pruebas
```bash
pytest
```
Las pruebas incluidas son una base inicial; ampliar los casos para autenticación, autorización, consultas a ambas bases, herramientas MCP, disponibilidad y pagos.

## Despliegue
Definir y documentar el proveedor elegido para Streamlit, FastAPI, PostgreSQL y MongoDB. Configurar variables secretas en el panel del proveedor. No se incluye una URL de producción hasta realizar el despliegue.

## Estado del repositorio
Esta entrega es una **estructura inicial de desarrollo**. Los conectores externos, el flujo completo de IA/MCP, el pago y el despliegue requieren configuración e implementación por el equipo.
