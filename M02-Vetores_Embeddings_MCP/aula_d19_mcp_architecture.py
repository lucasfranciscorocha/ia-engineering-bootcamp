import asyncio
from typing import List
import mcp.types as types
from mcp.server import Server  # 1. Correção do caminho de importação explícito
from pydantic import AnyUrl    # 2. Importação do validador de URL exigido pelo Pylance

# Inicializa o servidor com a importação direta corrigida
server = Server("personal-help-desk-gateway")

@server.list_resources()
async def handle_list_resources() -> List[types.Resource]:
    """Expõe caminhos estáticos de documentação técnica como recursos para a IA."""
    return [
        types.Resource(
            # 3. Força a string a virar um objeto AnyUrl compatível com o contrato do MCP
            uri=AnyUrl("file:///briefings/identity.txt"),
            name="Diretrizes de Identidade Visual da Vita",
            mimeType="text/plain",
            description="Logotipos, paleta de cores e tipografia padrão para os layouts da Vita."
        )
    ]

async def main():
    print("🔌 [MCP CONFIGURATION]: Protocolo de contexto inicializado no venv!")
    print(f"Nome do Gateway de Dados: {server.name}")
    print("Pronto para estabelecer canais de transporte assíncronos no Ubuntu.")

if __name__ == "__main__":
    asyncio.run(main())