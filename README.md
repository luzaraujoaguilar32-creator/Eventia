# Eventia
**Aplicación web para la gestión inteligente de eventos y reservaciones mediante IA y MCP.**

## Datos del equipo
- **Asignatura:** Programación Lógica y Funcional
- **Grupo/equipo:** PLYF
- **Docente:** Alvarez Aspeitia Mauricio Alberto
- **Integrantes:**
  - Luz Karina Araujo Aguilar
  - Carlos Emanuel Lopez Villanueva


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

