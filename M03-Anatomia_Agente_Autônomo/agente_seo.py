import os

# =====================================================================
# 1. PERFIL E IDENTIDADE (Persona)
# =====================================================================
PROMPT_SISTEMA = """
Você é um Agente Especialista em SEO Técnico. 
Seu objetivo é analisar arquivos HTML locais e garantir que a tag <title> 
contenha a palavra-chave ideal estipulada na sua memória de longo prazo.
"""

# =====================================================================
# 3. MEMÓRIA (Longo Prazo / Contexto)
# =====================================================================
# Simulando uma busca em banco vetorial/arquivo de configuração
MEMORIA_LONGO_PRAZO = {
    "palavra_chave_foco": "Inteligência Artificial"
}

# Memória de curto prazo (histórico da execução atual)
memoria_curto_prazo = []

# =====================================================================
# 4. FERRAMENTAS (Tools / Actions)
# =====================================================================
def ler_html_local(caminho_arquivo):
    """Ferramenta para ler o arquivo HTML do ambiente Ubuntu."""
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    return "Erro: Arquivo não encontrado."

def aplicar_correcao_seo(caminho_arquivo, novo_conteudo):
    """Ferramenta para salvar as alterações de SEO no disco."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)
    return "Sucesso: Página HTML atualizada com a nova tag de SEO!"

# =====================================================================
# 2. MOTOR DE PLANEJAMENTO E RACIOCÍNIO (The Brain / Loop ReAct)
# =====================================================================
def executar_agente(arquivo_alvo):
    print(f"[*] Inicializando Agente com Perfil: {PROMPT_SISTEMA.strip()}")
    
    # --- PASSO 1: Percepção e Ação Inicial ---
    print("\n[Pensamento] Preciso primeiro inspecionar o arquivo HTML atual para ver o estado das tags.")
    conteudo_atual = ler_html_local(arquivo_alvo)
    memoria_curto_prazo.append(f"Conteúdo lido: {conteudo_atual}")
    
    # --- PASSO 2: Raciocínio (Avaliação contra a Memória) ---
    palavra_alvo = MEMORIA_LONGO_PRAZO["palavra_chave_foco"]
    print(f"[Pensamento] Analisando o conteúdo. A palavra-chave obrigatória é '{palavra_alvo}'.")
    
    if palavra_alvo in conteudo_atual:
        print("[Pensamento] O HTML já está otimizado. Nenhuma ação é necessária.")
        return "Processo finalizado: SEO já estava correto."
    
    else:
        print("[Pensamento] Alerta! A palavra-chave não foi encontrada no título. Preciso agir.")
        
        # --- PASSO 3: Tomada de Decisão e Nova Ação ---
        # Simulando o LLM gerando o novo HTML corrigido
        print(f"[Ação] Utilizando a ferramenta 'aplicar_correcao_seo' para embutir a tag de SEO...")
        
        novo_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{palavra_alvo} - O Guia Definitivo</title>
</head>
<body>
    <h1>Bem-vindo ao estudo de agentes autônomos.</h1>
</body>
</html>"""
        
        resultado_ferramenta = aplicar_correcao_seo(arquivo_alvo, novo_html)
        memoria_curto_prazo.append(f"Resultado da correção: {resultado_ferramenta}")
        
        # --- PASSO 4: Avaliação Final ---
        print(f"[Pensamento] Ferramenta retornou: {resultado_ferramenta}. Objetivo concluído.")
        return "Processo finalizado: SEO atualizado com sucesso."

# =====================================================================
# EXECUÇÃO DO AMBIENTE
# =====================================================================
if __name__ == "__main__":
    # Criando um arquivo HTML desatualizado para o teste no Ubuntu
    arquivo_teste = "index.html"
    with open(arquivo_teste, 'w') as f:
        f.write("<html><head><title>Página Antiga</title></head></html>")
        
    # Executa o ciclo do agente
    status_final = executar_agente(arquivo_teste)
    print(f"\n[Status Final do Agente]: {status_final}")
    
    # Limpando o arquivo de teste após a execução
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)