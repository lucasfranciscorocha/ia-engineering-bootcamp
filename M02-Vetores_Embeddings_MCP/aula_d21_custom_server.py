from mcp.server.fastmcp import FastMCP

# 1. Inicializa o servidor usando a API moderna FastMCP
# Ela configura automaticamente os metadados de identificação
app = FastMCP("personal-help-desk-automation")

# =========================================================================
# 📄 CAMADA DE RESOURCES (Leitura de Dados Estáticos)
# =========================================================================
@app.resource("file:///briefings/proposal_structure.txt")
def fetch_proposal_structure() -> str:
    """Modelo padrão da agência de divisão de escopo (Design e Código) para projetos 72h."""
    return "DIRETRIZ DE ESCOPO: Projetos padrão de 72h devem ser divididos em: Design UI (22h) e Desenvolvimento/WordPress (50h)."

# =========================================================================
# 🛠️ CAMADA DE TOOLS (Ações Dinâmicas baseadas em funções Python)
# =========================================================================
# O FastMCP gera o JSON Schema automaticamente a partir dos Type Hints e da Docstring!
@app.tool()
def calculate_project_hours(total_hours: int = 72) -> str:
    """
    Calcula a divisão exata de horas de design e código com base no escopo total do projeto.
    
    Args:
        total_hours: Total de horas estimadas para o contrato (Ex: 72)
    """
    # Regra de negócio da sua agência (30% Design, 70% Dev)
    design_hours = int(total_hours * 0.3)
    code_hours = int(total_hours * 0.7)
    
    return f"📊 [PHD AUTOMATION]: Distribuição calculada: {design_hours}h para Design Gráfico/UI e {code_hours}h para Desenvolvimento WordPress."

if __name__ == "__main__":
    # O próprio FastMCP gerencia a inicialização do Stdio internamente!
    app.run()