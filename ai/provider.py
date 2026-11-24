\"\"\"PENDIENTE\"\"\"

class AIProvider:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    async def answer(self, message: str, tool_results: list[dict] | None = None) -> str:
        return "La integración del proveedor de IA está pendiente."
