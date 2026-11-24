\"\"\"Servidor MCP inicial de Eventia.

Antes de exponer herramientas en producción, conectar cada función con servicios
del backend y obtener el contexto autenticado de forma segura.
\"\"\"
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Eventia MCP")

@mcp.tool()
def get_packages() -> dict:
    \"\"\"Consultar paquetes publicados. Pendiente: consulta real a MongoDB.\"\"\"
    return {"status": "not_implemented", "items": []}

@mcp.tool()
def check_availability(event_date: str, start_time: str, end_time: str, space_id: str) -> dict:
    \"\"\"Consultar disponibilidad de un espacio y horario.\"\"\"
    return {"status": "not_implemented", "available": None}

@mcp.tool()
def create_quotation(items: list[dict]) -> dict:
    \"\"\"Calcular una cotización con servicios y cantidades.\"\"\"
    return {"status": "not_implemented", "total": None}

@mcp.tool()
def get_reservations() -> dict:
    \"\"\"Consultar reservaciones permitidas para el usuario autenticado.\"\"\"
    return {"status": "not_implemented", "items": []}

@mcp.tool()
def create_reservation(event_date: str, space_id: str, details: dict) -> dict:
    \"\"\"Crear solicitud después de verificar permisos y disponibilidad.\"\"\"
    return {"status": "not_implemented", "reservation_id": None}

@mcp.tool()
def get_event_details(event_id: str) -> dict:
    \"\"\"Consultar detalles de un evento con validación de acceso.\"\"\"
    return {"status": "not_implemented", "event": None}

if __name__ == "__main__":
    mcp.run()
