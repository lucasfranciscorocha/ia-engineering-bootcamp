

## Dia 23: Anatomia de um Agente Autônomo

Para entender como orquestrar múltiplos agentes mais adiante, precisamos primeiro entender a engenharia interna de um único agente. Ao contrário de um script linear ou de uma chamada simples de API de LLM, um agente autônomo opera em um ciclo contínuo de percepção, tomada de decisão e ação.

Podemos dividir a anatomia padrão de um agente em **4 pilares fundamentais**:
```
                  ┌────────────────────────┐
                  │   Perfil / Identidade  │
                  └───────────┬────────────┘
                              ▼
┌───────────┐     ┌────────────────────────┐     ┌───────────┐
│           │ ──► │  Memória (Curto/Longo) │ ──► │           │
│ Percepção │     └────────────────────────┘     │   Ações   │
│ (Inputs)  │     ┌────────────────────────┐     │  (Tools)  │
│           │ ──► │   Planejamento / Razão │ ──► │           │
└───────────┘     └────────────────────────┘     └───────────┘
```

### 1. Perfil e Identidade (Persona / Role)

É a definição do escopo, tom, restrições e objetivos do agente. No desenvolvimento de software, isso se traduz no _System Prompt_.

- **O que faz:** Define as fronteiras do que o agente _pode_ e _deve_ fazer. Se ele for um designer de interfaces, seu perfil garantirá que ele avalie o mundo sob a ótica de acessibilidade e design responsivo, ignorando ruídos irrelevantes.
    

### 2. O Núcleo de Planejamento e Raciocínio (Brain)

É aqui que o LLM entra como o "motor de busca conceitual" e tomador de decisões. O agente decompõe grandes objetivos em subtarefas. Os frameworks modernos utilizam técnicas específicas de design de prompt para isso:

- **Chain-of-Thought (CoT):** O agente resolve problemas passo a passo, verbalizando seu raciocínio antes de entregar o resultado.
    
- **ReAct (Reason + Act):** O agente alterna entre pensar (Raciocínio) e executar comandos (Ação). Ele analisa o contexto, decide usar uma ferramenta, observa o resultado e planeja o próximo passo.
    

### 3. Memória (Memory)

Um agente sem memória é apenas uma função pura que esquece o contexto a cada execução. Dividimos a memória em duas camadas:

- **Memória de Curto Prazo (In-Context):** O histórico imediato da conversa ou da sessão de execução atual (limitado pela janela de contexto do modelo).
    
- **Memória de Longo Prazo (Externalized):** Bancos de dados vetoriais (Vector DBs) onde o agente pode buscar informações históricas ou documentos de referência usando buscas por similaridade (RAG) através do tempo.
    

### 4. Ferramentas e Execução (Tools / Actions)

É a capacidade do agente de impactar o mundo real ou coletar dados dinâmicos. Sem ferramentas, o agente apenas "fala". Com ferramentas, ele se torna funcional.

- **Exemplos de ferramentas:** Scripts Python/Bash locais, APIs de busca web, conectores de banco de dados, ou comandos de sistema para ler/escrever arquivos.


# Módulo 3 • Dia 04: Anatomia de um Agente Autônomo
**Tags:** #estudo/ia #agentes #orquestracao
**Data:** 2026-06-04

## 📌 Visão Geral
O ciclo de um agente autônomo baseia-se no modelo **ReAct (Reason + Act)**:
1. **Percepção:** Captura dados do ambiente (ex: lê um arquivo no Ubuntu).
2. **Raciocínio:** Avalia o cenário com base nas regras de negócio (Prompt).
3. **Ação:** Executa ferramentas (scripts, chamadas de API).

## 🫀 Os 4 Pilares Fundamentais
- **Perfil (Persona):** Escopo de atuação definido no System Prompt.
- **Raciocínio (Brain):** Onde o LLM processa e quebra tarefas (CoT / ReAct).
- **Memória:** Curto prazo (histórico da sessão) vs. Longo prazo (bancos vetoriais).
- **Ferramentas (Tools):** Pontes com o mundo externo (scripts Python, APIs).

## 🛠️ Protótipo Prático (Script de SEO Técnico)

```python
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
        
```


## 🧠 Insights & Conexões

- _Links:_ [[Conceitos de LLM]], [[Bancos Vetoriais e RAG]]
    
- Substituir a lógica de `if/else` por chamadas dinâmicas nos próximos dias.
--- 
### 2. O Mapa Mental (Para Visão Espacial e Arquitetura) 
Como você atua na área de design e comunicação visual, a sua mente naturalmente se apoia em fluxos visuais. Para o design de sistemas e a orquestração de múltiplos agentes que veremos à frente, faça o seguinte no Obsidian: 
1. Use o comando `Ctrl + P` (ou `Cmd + P`) no Obsidian. 
2. Digite `Canvas: Create new canvas`. 
3. Renomeie para `Mapa Mental - Orquestração de Agentes`. 
4. Crie cartões visuais interligados mapeando os 4 pilares, conectando-os ao cartão central "Agente Autônomo". 
O Canvas te dará a clareza macro de como a informação flui, enquanto a nota em Markdown guardará a precisão técnica e os snippets de código para você rodar no terminal. Quer que eu te ajude a desenhar a lógica de conexões do mapa mental para você montar no seu Canvas, ou prefere seguir direto para o próximo passo do dia?


## 🐧 Comandos de Terminal (Ubuntu) para Dev de Agentes

Como você está rodando no Linux, esses comandos de terminal (`bash`) são os blocos de construção para criar, testar e monitorar seus scripts de IA e arquivos de configuração.

Bash
```
# --- NAVEGAÇÃO E ARQUIVOS ---
cd /caminho/do/projeto    # Navega até a pasta onde estão seus scripts de agentes
ls -la                    # Lista todos os arquivos da pasta (incluindo ocultos e permissões)
mkdir nome_do_projeto     # Cria uma nova pasta para organizar os módulos de código
touch agente_seo.py       # Cria um arquivo Python em branco instantaneamente

# --- EXECUÇÃO E MONITORAMENTO ---
python3 agente_seo.py     # Executa o seu script de agente no terminal
cat index.html            # Exibe o conteúdo do arquivo HTML direto no terminal (bom para checar o SEO)
tail -f log_agente.txt    # Monitora em tempo real a saída de um arquivo de log (útil para loops longos)

# --- GERENCIAMENTO DE AMBIENTE ---
python3 -m venv venv      # Cria um ambiente virtual isolado (essencial para não quebrar o Python do Ubuntu)
source venv/bin/activate  # Ativa o ambiente virtual (faça isso antes de instalar ferramentas de IA)
pip install crewai        # Instala bibliotecas e frameworks de orquestração de agentes
```

> **💡 Dica de Fluxo de Trabalho:** No Ubuntu, você pode dividir a sua tela ao meio (`Tecla Super/Windows + Seta Esquerda` e `Seta Direita`), deixando o Obsidian de um lado para documentar o mapa mental e o terminal do outro para rodar os scripts em Python.

Se quiser, podemos avançar e aplicar esses comandos para estruturar o ambiente de desenvolvimento isolado no seu Ubuntu, preparando o terreno para o código do próximo dia. O que acha?

**você viu que estruturar um agente simples com `if/else` estáticos funciona para um arquivo isolado. Mas e se o seu agente de SEO precisasse:

1. Pesquisar os concorrentes no Google.
    
2. Escrever um relatório de melhorias.
    
3. Passar esse relatório para um _segundo_ agente programador aplicar o código.
    
4. Validar se o código não quebrou o layout.
    

Fazer isso com condicionais puras geraria um código impossível de manter. É aqui que entram os **Frameworks de Orquestração**. Eles são as "redes de transporte" e os "gerentes de projeto" que coordenam a comunicação entre múltiplos agentes e ferramentas.

Hoje, o mercado é dominado por duas grandes filosofias de desenvolvimento:

### 1. CrewAI: A Filosofia de "Equipe de Empresa" (Role-Playing)

O **CrewAI** é atualmente um dos frameworks mais populares do ecossistema Python pela sua simplicidade e abordagem intuitiva. Ele modela a IA como se fosse uma agência ou equipe humana.

- **Conceito-chave:** Você define **Agentes** (com cargos, histórias de fundo e ferramentas) e **Tarefas** (o que precisa ser feito). O framework se encarrega de passar o bastão de um agente para o outro de forma sequencial ou hierárquica.
    
- **Para que serve:** Fluxos de trabalho baseados em processos de negócios bem definidos. Ex: Agência de Marketing Digital, Produção de Conteúdo, Automação de Propostas Comerciais.
    

### 2. LangGraph: A Filosofia de "Fluxograma de Engenharia" (Graph-Based)

Criado pelos desenvolvedores do _LangChain_, o **LangGraph** enxerga a orquestração como um **Grafo** (Nós e Arestas).

- **Conceito-chave:** Cada ação ou agente é um "Nó" (Node), e as decisões de para onde ir a seguir são as "Arestas" (Edges). É uma lógica de máquina de estados de altíssima precisão.
    
- **Para que serve:** Fluxos complexos onde há muitos loops de feedback (ex: se o agente de testes rejeitar o código, o fluxo _volta_ obrigatoriamente para o agente programador até estar perfeito).
    

### 📊 Tabela Comparativa para o seu Obsidian

|**Critério**|**CrewAI**|**LangGraph**|
|---|---|---|
|**Abordagem**|Baseada em Papéis (Cargos/Tarefas)|Baseada em Grafos (Estados/Fluxos)|
|**Curva de Aprendizado**|Baixa (Rápido de colocar em produção)|Alta (Exige conceitos de computação)|
|**Flexibilidade**|Média (Focado em fluxos estruturados)|Altíssima (Você controla cada milissegundo)|
|**Ideal para...**|Automações de marketing, design, relatórios|Sistemas críticos, IA de agentes industriais|

## 🚀 Conclusão do Módulo 4
- **Status do Ambiente:** Ubuntu configurado com venv e pacotes instalados (`crewai`, `crewai-tools`).
- **Aprendizado:** Entendi a diferença crucial entre agentes baseados em papéis/cargos (CrewAI) e baseados em grafos/máquina de estados (LangGraph).
- **Próximo Passo:** Configurar as chaves de API/Modelos locais para ver a Crew executando as tarefas de ponta a ponta.


---
tags:
  - ia-engineering
  - agents
  - crewai
  - python
  - linux
data: 2026-06-03
modulo: M04 - Orquestração de Agentes Autônomos
---

# Orquestração de Agentes: Da Anatomia ao Multi-Agent System (CrewAI)

## 🧠 1. O Loop de Paradigma: Percept ➔ Plan ➔ Action
A transição de um Chatbot reativo para um Agente Autônomo baseia-se na quebra da execução linear. Enquanto o chat tradicional responde ao input imediato do usuário, o agente opera em um ciclo contínuo de determinação de estado.

* **Percept (Percepção):** Captura de variáveis de ambiente, instruções do sistema e inputs contextuais.
* **Plan (Planejamento):** Decomposição de tarefas complexas em submetas executáveis utilizando técnicas como CoT (Chain of Thought) e auto-reflexão.
* **Action (Ação):** Invocação de ferramentas externas (Tool Calling) para alterar ou consultar o estado do ambiente (ex: ler arquivos do Linux, buscar APIs).

---

## 🛠️ 2. Arquitetura do Ambiente Local (Fix do Terminal Linux)
Durante a implementação prática dos primeiros agentes (`primeira_crew.py` e `agente_seo.py`), identificou-se um vazamento crítico de escopo no Python global do sistema. 

### Alinhamento de Escopo Técnico:
* **Ambiente Global:** Contém pacotes internos do Ubuntu Linux (ex: `alembic`, `ufw`, `cloud-init`). Exportar dependências sem isolamento polui o `requirements.txt` com distribuições do sistema (`.dev0`).
* **Ambiente Isolado (`.venv`):** Deve residir estritamente na raiz do workspace. O arquivo `.env` contendo credenciais de LLMs (OpenAI, Anthropic) deve ficar na raiz do projeto e **nunca** dentro da `.venv`, mitigando o risco de exfiltração via Git ou deleção acidental durante rotinas de MLOps (`rm -rf .venv`).

---

## 🤖 3. Implementação Prática: CrewAI & Orquestração Hierárquica
No script `primeira_crew.py`, aplicou-se o framework **CrewAI** para abstrair a deleção e execução horizontal de tarefas complexas através de papéis bem definidos.

```python
from crewai import Agent, Task, Crew, Process

# Definição do Agente com Especialidade Restrita
seo_agent = Agent(
    role='Especialista em SEO Técnico',
    goal='Auditar e otimizar a estrutura de metadados e tags de páginas web',
    backstory='Um analista focado em dados e performance de rankeamento algorítmico.',
    verbose=True,
    allow_delegation=False
)

# Acoplamento de Tarefa Determinística
audit_task = Task(
    description='Analisar o posicionamento de palavras-chave estruturais no arquivo de notas.',
    expected_output='Um relatório em Markdown contendo os pontos de melhoria de SEO.',
    agent=seo_agent
)

# Instanciação da Crew (Orquestração Sequencial)
crew = Crew(
    agents=[seo_agent],
    tasks=[audit_task],
    process=Process.sequential
)
```

### Insights de Execução:

1. **Verbose=True:** Essencial para auditar o fluxo de pensamento do agente (`Thought:`, `Action:`, `Action Input:`), permitindo rastrear onde ocorrem loops infinitos de execução.
    
2. **Separação de Contexto:** Garantir que o interpretador do VS Code (`Ctrl+Shift+P` -> `Python: Select Interpreter`) aponte estritamente para `./.venv/bin/python` para evitar falsos positivos de importação no Pylance.
    

## 🛑 4. Proteção de Repositório (`.gitignore`)

Configuração final aplicada para blindagem de metadados locais do Obsidian e dados sensíveis de infraestrutura:

# Ambientes Virtuais e Caches
.venv/
__pycache__/

# Infraestrutura de Credenciais
.env

# Lixo e Configurações de Workspace Local
**/workspace.json
**/workspace-mobile.json
.trash/


# Setup de Agentes Autônomos em Nuvem

**Data:** 04 de Junho de 2026

**Módulo:** 04 - Orquestração de Agentes Autônomos

**Ambiente:** Google Cloud Shell (Ephemeral Instance)

## 1. Objetivo da Atividade

Estabelecer um ambiente de desenvolvimento em nuvem para orquestração de agentes, realizando a transição de um ambiente de desenvolvimento local para uma arquitetura _Stateful_ baseada no framework do projeto `storygen-learning`.

## 2. Fluxo de Execução (Local-to-Cloud)

### A. Autenticação e Autorização (Identity Management)

- **Ferramenta:** GitHub CLI (`gh`).
    
- **Processo:** Execução de `gh auth login` com autenticação via `device-code` (flow `[https://github.com/login/device](https://github.com/login/device)`).
    
- **Resultado:** Conexão segura do terminal da nuvem com o _GitHub Profile_ (`lucasfranciscorocha`) para permitir operações de _fork_ e _versionamento_.
    

### B. Forking e Provisionamento (Infrastructure)

- **Comando:** `gh repo fork cuppibla/storygen-learning --clone=true`
    
- **Justificativa:** Criação de uma cópia legível e editável no repositório do usuário para implementação de lógicas de agentes sem interferir na base upstream.
    

### C. Gestão de Variáveis de Ambiente (Security & Config)

- **Desafio:** O projeto utiliza `env.template` como schema público.
    
- **Procedimento:**
    
    1. Criação do ambiente operacional: `mv env.template .env`.
        
    2. Configuração de chaves sensíveis (Gemini API Key, Project ID).
        
- **Nota Técnica:** O arquivo `.env` foi mantido fora do rastreamento do Git (`.gitignore`) para evitar exposição de credenciais (_Credential Exposure Mitigation_).
    

## 3. Arquitetura do Sistema (Aprendizado Teórico)

O laboratório atua como um sistema determinístico baseado em ciclos:

- **Percepção:** Entrada de keywords via interface web.
    
- **Planejamento:** Decomposição da narrativa em _4-Scene Structure_ via LLM (Gemini 1.5 Flash).
    
- **Ação:** Orquestração de chamadas de ferramentas (Imagen API) para geração de ativos visuais consistentes.
    

## 4. Diferenciais da Implementação (Log de Erros e Soluções)

- **Visibilidade de Arquivos:** Ajuste na visualização de _hidden files_ no editor do Cloud Shell (`.env` não estava sendo exibido na UI após a renomeação).
    
- **Git Status Clean-up:** Identificação da remoção do template original (`env.template`) e validação da segurança do novo arquivo de configuração.
    

### 📝 Observação para seu portfólio/nota:

_Este processo demonstra a capacidade de transitar de uma infraestrutura local (Docker-based) para um ambiente nativo em nuvem (Cloud Shell), utilizando ferramentas de automação de fluxo de trabalho (GitHub CLI) e seguindo as melhores práticas de **Secret Management** exigidas em ambientes de produção de agentes autônomos._

Você pode copiar esse conteúdo para um arquivo chamado `LOG_AULA_DAY_23.md` dentro da sua pasta e mantê-lo como seu registro oficial! Vamos seguir para a primeira tarefa prática do Codelab agora?


## 🛠️ Exercício 

## Módulo 4 - Dia 27: Arquitetura com LangGraph

Vamos desenhar o mapa do fluxo do seu **Extrator de Mailing Seguro** usando a lógica de Grafos. Imagine que o sistema possui 3 Nós e 1 Aresta Condicional. Escreva no seu Obsidian como ficaria esse desenho de fluxo:

1. **Nó 1 (Agente Coletor):** Recebe o texto bruto e executa a ferramenta de RegEx. Ele salva os números encontrados no `State`.
    
2. **Aresta Condicional (Roteador):** Avalia a quantidade de contatos no `State`.
    
    - _Condição A:_ Se a lista de contatos estiver vazia → Desvia o fluxo para o **Nó 3 (Agente de Ajuste)**.
        
    - _Condição B:_ Se a lista contiver contatos → Envia o fluxo direto para o **Nó 2 (Agente Formatador)**.
        
3. **Nó 2 (Agente Formatador):** Organiza os dados em um JSON/CSV final para o seu mailing e encerra o processo.
    
4. **Nó 3 (Agente de Ajuste/Alerta):** Solicita ao operador humano uma nova entrada de texto mais limpa, impedindo o sistema de travar ou quebrar em produção.
    

No seu Obsidian, responda: **Qual é a grande vantagem de usar uma Aresta Condicional controlando o fluxo do agente em vez de simplesmente deixar a própria LLM decidir por texto livre o que fazer quando a extração falha?** Pense na previsibilidade do seu sistema.

Assim que registrar esse desenho de arquitetura no seu vault e estiver pronto para avançar para os sistemas de multi-agentes hierárquicos com **CrewAI e AutoGen (Dia 28)**, me dê o sinal aqui!


### 👥 EQUIPE VIRTUAL: AGÊNCIA IA LOCAL "ORIGINAL"

#### 1. Agente: Designer de Interfaces UX/UI
* **Role:** Designer Especialista em Sistemas de Design e Acessibilidade.
* **Goal:** Transformar briefings brutos em estruturas de tokens visuais organizados.
* **Backstory:** [Escreva aqui 1 ou 2 frases detalhando a personalidade/foco desse agente. Ex: "Você tem um olho clínico para consistência e rejeita qualquer layout que viole as diretrizes da WCAG..."]

#### 2. Agente: Desenvolvedor WordPress Core
* **Role:** Engenheiro de Software Sênior especializado em PHP e CSS limpo.
* **Goal:** Traduzir especificações de design em código otimizado para o ecossistema WordPress.
* **Backstory:** [Escreva aqui 1 ou 2 frases definindo a rigidez técnica dele com performance e semântica de código.]

---

### 📋 MAPEAMENTO DE TASKS (Fluxo Sequencial)

#### Task 1: Estruturação Visual (Executada pelo Designer)
* **Descrição:** Analisar o briefing fornecido pelo operador e gerar a tabela de tokens de design.
* **Expected Output (Resultado Esperado):** Uma lista estruturada em Markdown contendo: Cores Primárias/Secundárias em Hexadecimal, Escala de Fontes (rem) e Margens padrão.

#### Task 2: Codificação de Infraestrutura (Executada pelo Dev)
* **Descrição:** Ler o Markdown gerado pela Task 1 e gerar os arquivos de código.
* **Contexto de Entrada:** Output da Task 1.
* **Expected Output (Resultado Esperado):** [Defina exatamente o que o desenvolvedor deve cuspir como entrega final para a sua pasta de desenvolvimento.]


### 👥 EQUIPE VIRTUAL: CÉLULA DE SETUP E AUDITORIA "AJUSTADO"

#### 1. Agente: Analista de Soluções e Templates (Pesquisador)

- **Role:** Arquiteto de Soluções WordPress e Pesquisador de Componentes.
    
- **Goal:** Mapear os melhores templates, layouts e módulos estruturais baseados nas necessidades de negócio do cliente.
    
- **Backstory:** Você é especialista no ecossistema WordPress, Elementor e blocos Gutenberg. Seu foco é identificar estruturas prontas que resolvam problemas comuns (como catálogos de produtos, formulários de conversão e blocos de redes sociais) sem reinventar a roda.
    

#### 2. Agente: Engenheiro de Performance e Auditoria (Consultor)

- **Role:** Auditor de Código, UI e Ecossistema WordPress.
    
- **Goal:** Gerar relatórios detalhados de adequação de marca e recomendação de ferramentas.
    
- **Backstory:** Você avalia o trabalho do Pesquisador sob a ótica de performance, semântica e identidade visual. Você traduz o layout encontrado em tokens de design (cores, fontes) e dita quais plugins homologados e leves (ex: Rank Math para SEO, Fluent Forms para formulários) devem ser usados.
    

#### 3. Agente: Desenvolvedor Front-End Júnior (Executor)

- **Role:** Técnico de Implementação Web e Ajustes de UI.
    
- **Goal:** Executar modificações superficiais de estilo, parametrização e CSS de forma segura.
    
- **Backstory:** Você é o braço mecânico da equipe. Você não altera a arquitetura do core do tema; seu foco é aplicar os tokens de cores, configurar os plugins recomendados e injetar o CSS de ajustes finos (como paddings e margens) ditados pelo Auditor.
    

### 📋 NOVO MAPEAMENTO DE TASKS (Fluxo de Execução Triplo)

#### Task 1: Pesquisa Estrutural de Componentes

- **Responsável:** Analista de Soluções (Pesquisador)
    
- **Descrição:** Analisar o briefing do cliente e varrer os padrões de templates que contenham nativamente os módulos exigidos: **Módulo de Produtos/Portfólio**, **Formulários de Captura** e **Integrações de Redes Sociais**.
    
- **Expected Output (Resultado Esperado):** Um documento Markdown listando os 2 melhores caminhos estruturais ou templates de referência que possuem esses módulos nativos, justificando a escolha baseada nos requisitos do cliente.
    

#### Task 2: Auditoria Visual e Estratégia de Plugins

- **Responsável:** Engenheiro de Performance (Auditor)
    
- **Contexto de Entrada:** Output da Task 1.
    
- **Descrição:** Ler a estrutura recomendada pela Task 1. Extrair quais serão as alterações necessárias para adequar esse template à identidade do cliente. Mapear a paleta de cores substituta, a escala tipográfica e listar exatamente quais plugins específicos (e leves) devem ser instalados para cobrir os módulos (ex: produtos, formulário).
    
- **Expected Output (Resultado Esperado):** Um **Relatório Técnico de Alterações** contendo:
    
    1. Tabela de Cores e Fontes (De: Original -> Para: Nova Marca).
        
    2. Lista de Plugins Sugeridos com suas respectivas funções justificadas.
        

#### Task 3: Execução de Ajustes Superficiais e Setup

- **Responsável:** Dev Júnior (Executor)
    
- **Contexto de Entrada:** Output da Task 2 (O Relatório).
    
- **Descrição:** Receber o Relatório de Alterações. Simular ou aplicar as configurações recomendadas. Gerar o arquivo de estilos de CSS superficial (`custom-adjustments.css`) aplicando os paddings, cores e tipografia aprovados no relatório, além de listar os comandos de ativação de plugins.
    
- **Expected Output (Resultado Esperado):** O arquivo de código CSS final higienizado pronto para inserção e o log de modificações superficiais concluídas com sucesso.
    

### 🧠 Por que isso funciona tão bem no CrewAI?

Ao delegar a execução fina para o **Agente 3**, você isola o código de produção de grandes estragos. O Agente 3 não precisa decidir _o que_ instalar ou _qual_ cor usar; ele apenas lê o relatório mastigado e determinístico do **Agente 2** e executa a tarefa repetitiva. Isso reduz a taxa de erro do sistema para próximo de zero.

Organize essa estrutura no seu Obsidian. Quando terminar e estiver pronto para ver como o **RAG Dinâmico (Dia 29)** daria ao Agente 1 a capacidade de buscar essas documentações de templates em arquivos locais, me dê o sinal verde!


[Briefing do Cliente em Markdown] 
               │
               ▼  (O Agente lê usando o Servidor MCP Local)
      [ Agente Pesquisador ]
               │
               ▼  (Percebe que não conhece o template ideal)
   [ Ativa o RAG Dinâmico ] ───► (Busca termos no ChromaDB local)
               │
               ▼  (Retorna as especificações do template)
      [ Agente Pesquisador ]
               │
               ▼  (Escreve o plano de execução via MCP direto na sua pasta)
   [ Arquivo plano_web.md gerado no Ubuntu ]