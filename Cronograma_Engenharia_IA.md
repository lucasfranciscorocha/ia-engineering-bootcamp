
# 🥷 AI Engineering & Agentes Autónomos

Este ficheiro representa a árvore completa de competências e o cronograma de execução local para a transição definitiva para a Engenharia de IA. 

---

## 🏁 Módulo 0: Fundação de Sistemas, Deep Learning e APIs (Concluído)
*Foco: O que acontece "sob o capô", matemática linear de redes e os primeiros pipelines estruturados.*

- [x] **DIA 1: O Panorama Global e Limitações**
	- *Abordagem:* Entendimento do ecossistema de IA e separação do hype.
	- *Foco Técnico:* Limitações de modelos (ausência de raciocínio causal puro, falhas de generalização fora da distribuição de treino).
	- *Métrica:* Diferenciar automação estatística previsível de intervenção humana.
- [x] **DIA 2: A Matemática das Escolhas e Otimização**
	- *Abordagem:* Base matemática linear que sustenta a inferência.
	- *Foco Técnico:* Papel de Weights (Pesos) e Biases (Vieses) como coeficientes de ajuste.
	- *Equação de Base:* $$z = w^T x + b$$
$$\text{Sinal Total } (z) = (\text{Dados do Utilizador } [x] \times \text{Importância de Cada Dado } [w]) + \text{Inércia do Modelo } [b]$$


- [x] **DIA 3: Deep Learning, Camadas Ocultas e Redes Temporais**
	- *Abordagem:* Funções encadeadas e processamento sequencial de dados.
	- *Foco Técnico:* Camadas ocultas com ativação ReLU, algoritmo de Backpropagation (derivadas parciais) e transição para dados temporais (RNNs, GRUs, LSTMs) mitigando o desaparecimento do gradiente (*vanishing gradients*) via portões de memória (*gates*).
- [x] **DIA 4: O Divisor de Águas: Transformers e Atenção**
	- *Abordagem:* Transição definitiva para a arquitetura moderna de Attention Blocks.
	- *Foco Técnico:* Mecanismo de *Self-Attention* (correlação simultânea global de texto) e algoritmos de geração como *Beam Search* para seleção de caminhos probabilísticos de tokens.
- [x] **DIA 5: Tokenização e Espaços Vetoriais (Embeddings)**
	- *Abordagem:* Ponte entre texto bruto e álgebra linear.
	- *Foco Técnico:* Algoritmo BPE (Byte Pair Encoding) e projeção de IDs em matrizes de Embedding densas (Word2Vec, GloVe).
	- *Evidência no Ubuntu:* Análise do "imposto do idioma" via script `token_test.py` com a biblioteca `tiktoken`.
- [x] **DIA 6: Exploração e Manipulação de Open Weights**
	- *Abordagem:* Infraestrutura e ecossistema de modelos abertos.
	- *Foco Técnico:* Mapeamento do Hugging Face Hub via CLI/Web, formatos de ficheiros de parâmetros (`.safetensors`) e quantizações binárias (`.gguf`) para execução local.
- [x] **DIAS 7 & 8: Pipelines de Código, Parâmetros e Chain of Thought**
	- *Abordagem:* Automação de chamadas de API com controlo probabilístico e expansão computacional.
	- Foco Técnico:* Configuração estrita de Temperatura ($T=0.0$) pós-Softmax para análise de logs. Injeção de instruções de raciocínio forçado (*Chain of Thought*), alimentando o KV Cache para mitigar alucinações.
	- *Evidência no Ubuntu:** Execução do script `pipeline_logica.py` sob ambiente isolado `mise` (Python 3.12), contornando o bloqueio da PEP 668 (Externally Managed Environment) do Ubuntu e persistindo a credencial `$GEMINI_API_KEY` via `~/.bashrc` para herança nativa de subprocessos.
- [x] **DIAS 9 & 10: MLOps, Saídas Estruturadas (JSON) e Red-Teaming**
	- *Abordagem:* Acoplamento estrito de LLMs em sistemas de backend e segurança de infraestrutura.
	- *Foco Técnico:* JSON Estrito via modelos Pydantic (`BaseModel`), forçando o decodificador de tokens a obedecer ao JSON Schema. Uso da estrutura como barreira arquitetural contra ataques de *Prompt Injection*.
	- *Evidência no Ubuntu:* Execução do script `pipeline_avancado.py` gerando payloads limpos de saudações, prontos para consumo de software.

#### 📈 Resumo das Entregas de Código (Workspace do Lucas)

A tua pasta `/home/lucasrocha/#dev/#aulas-praticas/` contém a seguinte infraestrutura validada:
1. `D_01_tokens/token_test.py` -> Validou a biblioteca `tiktoken` e a quebra de texto em IDs.
2. `D_03_04_api_logica/pipeline_logica.py` -> Implementou o cliente `google-genai` com isolamento da chave `$GEMINI_API_KEY` via `~/.bashrc` e teste de Temperatura.
3. `D_03_04_api_logica/pipeline_avancado.py` -> Implementou o motor de extração de logs com parsing automatizado para JSON estruturado via Pydantic.

#### 🗂️ Estrutura de Conhecimento e Ativos Corporativos
* **Conceitos Core (03-Conceitos_Core/):** Fundações teóricas imutáveis documentadas:
  * `stdio_vs_http.md` -> Controle de fluxo JSON-RPC e prevenção de Broken Pipes.
  * `similaridade_cosseno.md` -> A matemática geométrica por trás da busca do RAG.
  * `sandboxing_seguranca.md` -> Defesa de perímetro do Ubuntu contra Prompt Injection.
* **Projetos & Ferramentas (04-Projetos_Minhas_Ferramentas/):** Ativos práticos da Personal Help Desk:
  * `automacoes_design_gutenberg.md` -> Esteira de geração automatizada de CSS estruturado.
  * `configuracoes_git_servidor.md` -> Arquitetura de deploy e versionamento local-para-servidor.
---

## ⚡ Próximos Passos: Execução da Agenda Ativa (22 Dias)

### 🔌 Módulo 1: APIs, Engenharia de Prompt e Saídas Estruturadas (6 Dias)
*Foco: Domínio avançado do SDK unificado da Google em Python e técnicas de extração industrial.*

- [x] **DIA 11: Tokenização Autorregressiva e Gestão de Contexto**
	- Mecânica de predição do próximo token e o impacto do crescimento do KV Cache na Janela de Contexto do Gemini.
- [x] **DIA 12: Frameworks de Prompt e Mitigação de Viés**
	- Aplicação do Framework RTOS (Role, Task, Context, Constraint) e uso de tags delimitadoras (XML/Markdown) para blindar inputs. Tratamento de *Few-shot bias*.
- [x] **DIA 13: Raciocínio Lógico e Padrão ReAct**
	- Técnicas para forçar o modelo a decompor problemas complexos antes da resposta final através do padrão Reason + Action (ReAct).
- [x] **DIA 14: Parâmetros Técnicos e Configuração de Segurança**
	- Ajuste fino de Temperatura, Top-P (Nucleus Sampling) e isolamento de instruções na *System Message*. Configuração rápida de *Billing Alarms* no painel do Google AI Studio para proteção do cartão.
- [x] **DIA 15: Structured Outputs com Pydantic Avançado**
	- Acoplamento de tipagem estrita (`int`, `str`, `List`) e injeção de metadados em `Field()` que atuam como instruções nativas de prompt para o modelo gerar dados JSON sem falhas de sintaxe.
- [x] **DIA 16: Prompt Defensivo e Tratamento de Exceções**
	- Engenharia reversa de prompts para prevenir Jailbreaking e criação de blocos `try/except` em Python para gerir erros de ligação e limites de taxa (*Rate Limits*) da API.

### 📐 Módulo 2: Matemática para Vetores e Embeddings (1 Dia - 2 Blocos)
*Foco: A intuição geométrica e espacial por trás do RAG, ligando o raciocínio visual ao desenvolvimento.*

- [x] **BLOCO 17: O Espaço de Ideias e Proximidade Semântica**
	- Como a IA transforma palavras e trechos do teu código WordPress em coordenadas numéricas em espaços de alta dimensão (768 ou 1536 dimensões).
	- *Prática:* Testar o *TensorFlow Projector* para inspecionar nuvens de dados em 3D. Comparar como o tokenizer do Gemini e do Llama 3 (`Hugging Face Tokenizers`) fragmentam o mesmo arquivo local no Linux.
- [x] **BLOCO 18: Métricas de Distância e Similaridade**
	- Estudo da **Similaridade de Cosseno** (medição do ângulo entre dois vetores) e do Produto Escalar ($Dot\ Product$) como o motor de busca do RAG.
	- *Intuição Visual:* Vetores que apontam para a mesma direção representam ideias idênticas.

### 📦 Módulo 3: Model Context Protocol (MCP) Local em Python (4 Dias)
*Foco: Implementação do protocolo aberto da Anthropic usando apenas o ecossistema Python nativo do teu venv, sem o software do Claude Desktop.*

- [x] **DIA 19: Arquitetura e Fluxo do Protocolo**
	- Estudo do ecossistema aberto: Host local, Server de dados e Client. Como o MCP elimina silos de informação comunicando via transporte Stdio.
- [x] **DIA 20: Consumo de Servidores Open-Source**
	- Configuração via terminal de conectores padrão do GitHub (Filesystem e SQLite) para dar leitura de arquivos locais ao ambiente de execução.
- [x] **DIA 21: Construção do teu Próprio MCP Server**
	- Desenvolvimento de um script em Python usando o SDK do MCP para expor **Resources** (leitura estática de briefings de design) e **Tools** (funções que executam ações no sistema, como criar um ficheiro `.css`).
- [x] **DIA 22: Depuração e Inspeção de Transporte**
	- Uso da ferramenta de CLI `mcp-cli` para testar as rotas de dados, analisar o tráfego de contexto e inspecionar erros de comunicação no teu Ubuntu.

## 🧭 Extensão_NPM_NPX_Python
* **Core Teórico de Infraestrutura:** Entendimento do protocolo JSON-RPC sobre transporte Stdio (`stdin`/`stdout`). Diagnóstico de corrupção de fluxo de dados causado por outputs não estruturados (como o uso indevido de comandos `print()` globais em background).
##### Etapa 1: Inspecionar Contratos Públicos (Filesystem Hub) 
- **O que aprendemos:** Lemos o "contrato" JSON-RPC do servidor oficial de Filesystem da Anthropic usando o MCP Inspector. Entendemos como a IA ganha superpoderes de leitura/escrita e como delimitar uma pasta específica por segurança usando caminhos absolutos no Linux.
##### Etapa 2: Configuração de Hosts Nativos ( Claude Desktop Integration )
- **O que vamos aprender:** Vamos sair do ambiente de testes (Inspector) e conectar nossos servidores (tanto os customizados em Python quanto os públicos em Node) diretamente no "coração" de um Host de IA real no Ubuntu.
- **Prática:** Manipular e debugar o arquivo oculto de configuração global `claude_desktop_config.json`, ensinando a IA a carregar os servidores automaticamente em background assim que o sistema inicia.
##### Etapa 3: Orquestração Multi-Servidor & Concorrência de I/O
- **O que vamos aprender:** O que acontece quando a IA precisa usar duas ferramentas de servidores diferentes ao mesmo tempo? Vamos aprender como o Host gerencia streams concorrentes de entrada e saída (Stdio) sem travar a memória RAM ou gerar conflitos de barramento de dados.
- **Prática:** Criar um cenário onde o agente autônomo lê um arquivo local (via servidor de Filesystem) e processa os dados usando uma ferramenta do nosso servidor customizado de matemática vetorial de forma simultânea.
##### Etapa 4: Auditoria de Logs de Produção & Segurança Avançada
- **O que vamos aprender:** Ferramentas profissionais de diagnóstico. Quando um agente de IA falha em background, ele não mostra uma tela de erro amigável; ele gera logs brutos de sistema. Vamos aprender a rastrear e ler esses logs no Linux.
- **Prática:** Forçar erros de conexão reais (como simular um _Broken Pipe_ ou permissão negada) e usar comandos do terminal para ler o arquivo de log do Host em tempo real (`tail -f`), identificando a falha exata em segundos.


### 🤖 Módulo 4: Orquestração de Agentes Autónomos (11 Dias)
*Foco: Criação de sistemas inteligentes cíclicos com capacidade de tomada de decisão, uso de ferramentas e aprovação humana.*

- [ ] **DIA 23: Anatomia de um Agente Autónomo**
	- O loop de execução agêntica: Percepção de ambiente -> Planeamento interno -> Ação. A diferença entre automação sequencial e agentes.
- [ ] **DIA 24: Planeamento de Tarefas e Auto-Reflexão**
	- Técnicas de decomposição de problemas complexos e mecanismos de auto-crítica (*Self-Criticism*), ensinando o agente a validar o seu próprio output antes de o entregar.
- [ ] **DIA 25: Gestão de Memória Agêntica**
	- Implementação de memória de curto prazo (estados do chat e janelas de contexto dinâmicas) e memória de longo prazo (armazenamento persistente de logs no disco rígido do Linux).
- [ ] **DIA 26: Tool Use e Function Calling Prático**
	- Escrever funções nativas em Python e ensinar o Gemini a decidir autonomamente se precisa de invocar essas funções com base no input do terminal.
- [ ] **DIA 27: Grafos de Decisão Cíclicos (LangGraph)**
	- Introdução ao desenvolvimento estruturado em grafos (Nós e Arestas). Criação de fluxos onde o agente pode reverter caminhos se encontrar um erro na execução de uma tarefa.
- [ ] **DIA 28: Sistemas Multi-Agente com CrewAI**
	- Orquestração e divisão de tarefas entre múltiplos agentes especialistas. Configuração de uma equipa virtual onde um agente atua como Designer UX e o outro como Programador WordPress.
- [ ] **DIA 29: RAG Dinâmico Orientado a Agentes**
	- Implementação de uma ferramenta onde o próprio agente calcula a similaridade vetorial (Módulo 2) e decide de forma autónoma *quando* precisa de consultar a documentação externa.
- [ ] **DIA 30: Integração do teu Servidor MCP Local**
	- Acoplamento do servidor MCP que construíste no Módulo 3 ao teu Agente. A IA passa a usar o protocolo como um braço mecânico para ler e escrever ficheiros reais na tua pasta `/home/lucasrocha/#dev/#aulas-praticas/`.
- [ ] **DIA 31: Desenvolvimento do Mini-Projeto (Agente Designer/Dev)**
	- *Projeto Prático:* Criar uma automação local isolada no teu `venv` que recebe um briefing de um cliente em Markdown, analisa os requisitos visuais, planeia os blocos e cospe um arquivo `variables.css` higienizado e a estrutura de pastas do tema WordPress correspondente.
- [ ] **DIA 32: Tracing, Observabilidade e Diagnóstico**
	- Instalação e uso da ferramenta Phoenix de forma 100% local no teu Ubuntu para monitorizar as rotas do agente, identificar gargalos e ver onde ele se perdeu no raciocínio lógico.
- [ ] **DIA 33: Engenharia Defensiva e Human-in-the-Loop (HITL)**
	- Configuração de travas de segurança em Python para limitar o número máximo de iterações do agente (evitando loops infinitos e desperdício de tokens). Criação de uma interrupção manual no terminal que exige que digites `[Y/N]` para autorizar o agente a modificar qualquer arquivo crítico do sistema.

---

















