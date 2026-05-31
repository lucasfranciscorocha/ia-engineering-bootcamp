# 🚀 Engenharia de IA & Infraestrutura de Agentes Autônomos

Este repositório centraliza o laboratório de desenvolvimento, a base de conhecimento atômica e os motores de execução da **Personal Help Desk**. Aqui estão consolidados os códigos de produção, auditorias de infraestrutura e a evolução conceitual do meu ecossistema de Inteligência Artificial.

## 🛠️ Stack Tecnológica & Ambiente Operacional
* **Sistema Operacional:** Linux Ubuntu (Gerenciamento de subprocessos POSIX e canais Stdio)
* **Ambiente de Desenvolvimento:** Visual Studio Code & Android Studio
* **Linguagens & Ecossistemas:** Python 3 (FastMCP, Ambientes Virtuais Isolados) | Node.js (NPM/NPX)
* **Arquitetura de IA:** Model Context Protocol (MCP), Vetores de Alta Dimensão, Mecanismos RAG
* **Orquestração Nativa:** Multiplexação de Canais Stdio e Auditoria Estatística de I/O em Tempo Real

---

## 📈 Organização do Ecossistema (Estrutura do Repositório)

* **`NOTAS/`**: Minha base de conhecimento de alta performance integrada via Obsidian, centralizando conceitos core e o meu Dicionário Centralizado de Comandos.
* **`Glossário_Global.md`**: Repositório atemporal e unificado de jargões computacionais e definições geométricas de IA.
* **`Cronograma_Engenharia_IA.md`**: Registro linear de evolução contínua e telemetria das etapas concluídas.
* **`M01-APIs_Prompt_Engineering/`**: Práticas de gestão de contexto autorregressivo, engenharia de prompts estruturados e framework RTOS (tags XML) para mitigação de ruído estatístico.
* **`M02-Vetores_Embeddings_MCP/`**: Algoritmos locais baseados em matemática vetorial (Similaridade de Cosseno), além de conectores e servidores customizados utilizando o ecossistema MCP.
* **`PROJETOS_FERRAMENTAS/`**: Ativos práticos de código de produção e automações desenvolvidas para soluções do mundo real.

---

## 🧪 Práticas de Engenharia em Destaque

### 1. Orquestração e Multiplexação de Servidores MCP
Configuração avançada de hosts nativos através da injeção de contratos JSON-RPC estruturados. Implementação de concorrência paralela no Kernel do Linux, permitindo que servidores Python (ambientes `.venv` isolados) e servidores de arquivos de ecossistemas Node funcionem simultaneamente sob o mesmo barramento Stdio.

### 2. Sandboxing e Blindagem contra Quebras de Transporte (EPIPE)
Desenvolvimento focado em estabilidade de background, substituindo outputs textuais primitivos por fluxos de diagnóstico dedicados (`stderr`). Aplicação do princípio do privilégio mínimo para travar o raio de ação das ferramentas em caminhos absolutos seguros, neutralizando vulnerabilidades de escape de diretório.
