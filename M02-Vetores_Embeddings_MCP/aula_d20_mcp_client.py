import asyncio
import os  # 1. Importa o gerenciador do sistema operacional
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def run_mcp_client():
    # 2. Captura automaticamente o caminho exato da pasta onde o script está rodando
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "-y", 
            "@modelcontextprotocol/server-filesystem", 
            current_directory  # Injeta o caminho dinâmico blindado
        ]
    )
    
    print(f"🚀 Iniciando servidor MCP Filesystem para o diretório: {current_directory}")
    
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("🔐 Conexão estabelecida e inicializada com o servidor open-source!")
            
            tools_response = await session.list_tools()
            print("\n🛠️  Ferramentas de sistema liberadas para uso:")
            
            if tools_response.tools is not None:
                for tool in tools_response.tools:
                    description = tool.description if tool.description else "Sem descrição"
                    print(f"  - [{tool.name}]: {description[:70]}...")
            else:
                print("⚠️ Nenhuma ferramenta foi retornada pelo servidor Filesystem.")

if __name__ == "__main__":
    asyncio.run(run_mcp_client())