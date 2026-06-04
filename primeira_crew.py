import os
from crewai import Agent, Task, Crew, Process

# 1. CONFIGURAÇÃO DE AMBIENTE (Simulando chaves de API)
# Nota: Em produção, você usaria uma chave real da OpenAI/Gemini aqui.
os.environ["OPENAI_API_KEY"] = "sua_chave_aqui"

# =====================================================================
# 2. DEFINIÇÃO DOS AGENTES (Papel, História de Fundo e Meta)
# =====================================================================

pesquisador = Agent(
    role="Analista de Tecnologia Sênior",
    goal="Explicar conceitos complexos de IA de forma extremamente simples.",
    backstory="""Você trabalha mapeando tendências tecnológicas. Sua habilidade principal 
    é ler documentações densas e extrair apenas o que é prático e vital.""",
    verbose=True,  # Mostra o raciocínio ("pensamentos") no terminal do Ubuntu
    allow_delegation=False
)

redator = Agent(
    role="Especialista em Engenharia de Conhecimento",
    goal="Formatar relatórios técnicos em Markdown limpo para bases de conhecimento locais.",
    backstory="""Você é um mestre da organização visual em texto. Sabe exatamente quando 
    usar tabelas, listas e blocos de código para tornar o conteúdo escaneável.""",
    verbose=True,
    allow_delegation=False
)

# =====================================================================
# 3. DEFINIÇÃO DAS TAREFAS (O que deve ser feito e quem faz)
# =====================================================================

tarefa_pesquisa = Task(
    description="""Faça um resumo executivo explicando o que é a técnica 'ReAct' (Reason + Act) 
    no contexto de agentes autônomos.""",
    expected_output="Um resumo de 3 pontos fundamentais sobre o funcionamento do ReAct.",
    agent=pesquisador
)

tarefa_redacao = Task(
    description="""Pegue o resumo do Analista e transforme em uma nota Markdown perfeitamente 
    estruturada, pronta para ser copiada para o Obsidian.""",
    expected_output="O conteúdo formatado em Markdown com títulos (##) e pontos-chave.",
    agent=redator
)

# =====================================================================
# 4. A ORQUESTRAÇÃO (Colocando a equipe para trabalhar)
# =====================================================================

equipe_obsidian = Crew(
    agents=[pesquisador, redator],
    tasks=[tarefa_pesquisa, tarefa_redacao],
    process=Process.sequential # A tarefa 2 começa exatamente quando a tarefa 1 termina
)

# Para rodar o fluxo (quando tiver suas credenciais configuradas):
# resultado = equipe_obsidian.kickoff()
# print(resultado)

print("[*] Estrutura da Crew configurada com sucesso!")