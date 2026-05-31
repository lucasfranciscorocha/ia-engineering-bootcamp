import os
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ==============================================================================
# ENVIRONMENT & BOOTSTRAP CONFIGURATION
# ==============================================================================

# Carrega as variáveis do arquivo .env local para a memória volátil do processo.
# Essencial para isolamento de escopo (Environment Isolation Pattern).
load_dotenv()

# ==============================================================================
# CORE COMPILER ENGINE (AI AGENT LAYER)
# ==============================================================================

def run_reasoning_compiler(file_path: str) -> str | None:
    """
    Age como um compilador determinístico. Recebe o path de um arquivo Markdown,
    utiliza raciocínio lógico (Few-Shot) via LLM e retorna o payload convertido em HTML.
    
    :param file_path: String representando o caminho local do arquivo de entrada.
    :return: String contendo o HTML processado ou None em caso de falha de I/O.
    """
    # Instancia o ponto de entrada da API. O SDK busca automaticamente a chave 
    # 'GEMINI_API_KEY' no ambiente físico (Fallback Automático).
    client = genai.Client()
    
    # Defensive Programming (Guarda de Segurança): Evita crash catastrófico de I/O
    # verificando a existência física do arquivo antes de alocar memória para leitura.
    if not os.path.exists(file_path):
        print(f"[ERROR] Fail-Soft Guard: Local file '{file_path}' target not found.")
        return None

    # Context Manager ('with'): Garante o encerramento seguro do stream do arquivo,
    # liberando os File Descriptors do Kernel do Linux mesmo se ocorrer um erro na leitura.
    with open(file_path, "r", encoding="utf-8") as f:
        raw_markdown: str = f.read()

    # SYSTEM INSTRUCTION: Define a arquitetura cognitiva, o escopo (boundaries)
    # e as restrições comportamentais do modelo (Structured Prompting).
    system_instruction = """
    [ROLE]
    You are an expert Data Engineer specialized in compiling raw Markdown strings into production-grade, semantic HTML blocks optimized for the WordPress Gutenberg layout engine.
    
    [TASK]
    Convert the raw data provided inside the <markdown_input> tags into clean, valid HTML.
    
    [IN-CONTEXT FEW-SHOT EXAMPLES]
    Example 1:
    Input: `## 🛠️ Setup`
    Output: `<h2>🛠️ Setup</h2>`
    
    Example 2:
    Input: ```bash\npython3 script.py\n```
    Output: `<pre class="wp-block-code"><code class="language-bash">python3 script.py</code></pre>`

    [CONSTRAINTS]
    - Do NOT include <html>, <body>, or markdown wrapping text.
    - Output ONLY the processed inner HTML blocks.
    - Ensure code structures carry standard language classes for frontend syntax styling.
    """

    print("🧠 [LLM REASONING] Requesting semantic compilation from Gemini Engine...")
    
    # Define os hyperparâmetros da execução. 
    # Temperature próxima de 0 desativa a aleatoriedade criativa, forçando
    # conformidade estrutural estrita (Deterministic Output).
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.1  
    )
    
    # Execução da chamada RPC síncrona enviando o payload envelopado em delimitadores estruturais.
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"<markdown_input>\n{raw_markdown}\n</markdown_input>",
        config=config
    )
    
    return response.text

# ==============================================================================
# REMOTE DEPLOYMENT LAYER (API GATEWAY CLIENT)
# ==============================================================================

def deploy_to_wordpress(html_content: str, title: str) -> None:
    """
    Injeta o payload de conteúdo HTML via chamadas HTTP autenticadas (REST API)
    diretamente no banco de dados do servidor destino.
    """
    # Extração de segurança: Puxa as credenciais injetadas pelo Dotenv.
    wp_user: str | None = os.getenv("WP_USERNAME")
    wp_pass: str | None = os.getenv("WP_APP_PASSWORD")
    wp_url: str | None = os.getenv("WP_SITE_URL")
    
    # Gatekeeper (Validação Estatística): Aborta a execução em tempo de runtime
    # se a infraestrutura local não possuir as variáveis de autenticação obrigatórias.
    if not all([wp_user, wp_pass, wp_url]):
        print("❌ [CRITICAL ERROR] Infrastructure Failure: Credentials missing in environment vault.")
        return

    # Constrói o REST Endpoint oficial do WordPress Core para manipulação de Posts.
    endpoint: str = f"{wp_url}/wp-json/wp/v2/posts"
    
    # Data Payload: Dicionário serializado que dita o estado final do recurso no servidor.
    # Definido como 'draft' para isolamento de segurança e auditoria visual pré-live.
    payload = {
        "title": title,
        "content": html_content,
        "status": "draft"  
    }
    
    print("🚀 [NETWORK DISPATCH] Transporting compiled payload over HTTP REST Gateway...")
    
    # Executa uma requisição HTTP POST assinalada com Basic Authentication via Tupla.
    res = requests.post(endpoint, json=payload, auth=(wp_user, wp_pass))
    
    # HTTP Status Code Evaluation: 201 indica "Created" com sucesso na arquitetura REST.
    if res.status_code == 201:
        print("\n" + "="*20 + " DEPLOYMENT SUCCESSFUL " + "="*20)
        print(f"Post created successfully as a DRAFT!")
        print(f"Review Link: {res.json().get('link')}")
        print("="*63)
    else:
        # Graceful Degradation: Captura o código de erro (Ex: 401 Unauthorized, 404 Not Found)
        # sem derrubar o terminal do desenvolvedor.
        print(f"❌ [API FAILURE] Gateway Rejected Payload (Status {res.status_code}): {res.text}")

# ==============================================================================
# APPLICATION ENTRY POINT (EXECUTION BOUNDARY)
# ==============================================================================

# O escopo '__main__' garante que este arquivo só execute os blocos abaixo se for
# invocado diretamente pelo terminal. Se for importado como módulo por outro script,
# ele não executa o teste automaticamente (Segregação de Escopo).
if __name__ == "__main__":
    
    # Define o alvo do pipeline de teste.
    target_file: str = "test_env.py" 
    
    # Executa o pipeline sequencial (Pipeline Dataflow Design).
    compiled_html = run_reasoning_compiler(target_file)
    
    if compiled_html:
        deploy_to_wordpress(compiled_html, title="Day 3 Automated Deployment Test")