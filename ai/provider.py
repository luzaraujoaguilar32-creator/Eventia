\"\"\"Adaptador pendiente para el proveedor de modelo de lenguaje elegido.\"\"\"

class AIProvider:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    async def answer(self, message: str, tool_results: list[dict] | None = None) -> str:
        # TODO: integrar SDK oficial del proveedor elegido y ciclo de invocación MCP.
        return "La integración del proveedor de IA está pendiente."
