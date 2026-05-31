# 📂 MÓDULO: Engenharia de Prompt e Automação de Infraestrutura

---

# 📚 Dia 11: Fundamentos do SDK e Isolamento de Ambiente
**Data:** 2026-05-22 (Sexta-feira)  
**Status:** 🟢 Concluído

## 🧠 Conceitos Chave

### 1. O Novo ecossistema Google GenAI
* Transição do ecossistema antigo (`google-generativeai`) para o novo SDK unificado (`google-genai`).
* Uso da classe de entrada `genai.Client()` que gerencia conexões e sessões de forma otimizada.
* Modelo padrão adotado para automação leve e rápida: `gemini-2.5-flash`.

### 🧪 2. Sandboxing com Virtual Environments (.venv)
* **Conceito:** Criação de um diretório isolado do Python para o projeto atual, impedindo conflitos de dependências com o sistema operacional base (Linux Ubuntu).
* **Comandos de Inicialização no Cockpit:**

  '''Bash
  cd ~/dev/aulas-praticas/
  python3 -m venv .venv
  source .venv/bin/activate
  
  
  ## 🛠️ Execução Prática

- Instalação do core do SDK dentro do ambiente isolado.
    
- Teste de ping inicial com a API do Gemini para checagem de latência e integridade do token.
    

# 📚 Dia 12: Engenharia de Prompt e Estruturação de Contexto

**Data:** 2026-05-23 (Sábado)

**Status:** 🟢 Concluído

## 🧠 Conceitos Chave

### 1. Anatomia de uma System Message Eficiente

- A instrução do sistema (`system_instruction`) dita o comportamento basal e as regras inflexíveis do modelo.
    
- Uso de delimitadores estruturais (tags XML como `<user_payload>`) para envelopar o dado de entrada do usuário.
    

### 🛡️ 2. Prevenção de Injeção de Prompt (Prompt Injection Guard)

- **Mecânica:** Configurar o modelo para tratar todo e qualquer dado vindo de fora estritamente como uma string passiva (dados puros), neutralizando comandos imperativos disfarçados que tentam burlar o sistema (ex: "Ignore as instruções anteriores").
    

## 🛠️ Execução Prática (`aula_d2_rtos_isolation.py`)

- Construção de um script que simula um payload malicioso enviado por um cliente.
    
- O modelo analisa o conteúdo sem executar o comando invasor, devolvendo um relatório de segurança limpo.
    

# 📚 Dia 13: Raciocínio Lógico e Padrão ReAct

**Data:** 2026-05-24 (Domingo)

**Status:** 🟢 Concluído

## 🧠 Conceitos Chave

### 🔄 1. O Framework ReAct (Reason + Action)

- **Conceito:** Força o LLM a decompor problemas complexos dividindo a execução em etapas de **Pensamento (Thought) ➔ Ação (Action) ➔ Observação (Observation)** antes de entregar a resposta final.
    
- Evita conclusões precipitadas e permite que a inteligência artificial decida quando interagir com ferramentas externas.
    

### 🎯 2. In-Context Learning (Few-Shot Prompting)

- Injeção de exemplos reais de Entrada e Saída diretamente nas instruções primárias. O modelo aprende a estilização e a transformação sintática por analogia estrutural direta.
    

## 🛠️ Execução Prática (`aula_d3_wp_automation.py`)

- Criação da lógica de compilação: O modelo lê um código ou arquivo markdown local, aplica o raciocínio estrutural dos exemplos fornecidos e faz o mapeamento para tags HTML semânticas adequadas para o WordPress.
    

# 📚 Dia 14: Parâmetros Técnicos e Configuração de Segurança

**Data:** 2026-05-25 (Segunda-feira)

**Status:** 🟢 Concluído (Ambiente Estabilizado)

## 🧠 Conceitos Chave

### ⚙️ 1. Parâmetros de Amostragem (Sampling Parameters)

- **Temperature ($T$):** Modula a aleatoriedade das previsões de tokens.
    
    - `T = 0.1` (Modo Engenharia/Código): Saídas altamente previsíveis, técnicas e repetíveis.
        
- **Top-P (Nucleus Sampling):** Filtro de corte dinâmico baseado na massa de probabilidade acumulada. Elimina palavras irrelevantes do vocabulário de seleção do modelo.
    

### 🔒 2. Padrão Decoupled .env (Segurança de Credenciais)

- **Anti-Pattern:** Injetar senhas globalmente no terminal (`~/.zshrc`) abre brechas para roubo de chaves por dependências maliciosas.
    
- **Best Practice:** Restrição de escopo. As chaves residem em um arquivo oculto local (`.env`) que nunca é enviado para repositórios Git, controlado por um arquivo `.gitignore`.
    

## 🛠️ Execução Prática e Integração Completa

- Implementação do arquivo `.gitignore` blindando o workspace de vazamentos.
    
- Autenticação bem-sucedida via REST API usando as chaves isoladas do `.env` e despacho do primeiro rascunho (`draft`) com sucesso para o banco de dados do WordPress (`lucasfrancorocha.com.br`).
    
- Configuração preventiva de Billing Alarms de **$5.00** no painel da API para controle financeiro estrito.
---

## 📚 Dia 15 (Módulo 1 - Dia 5): Structured Outputs com Pydantic Avançado 

**Data:** 2026-05-26 (Terça-feira) 
**Status:** 🟢 Concluído (Ambiente Estabilizado)

🧠 Conceitos Chave
* **Pydantic Schema Guard:** Vinculação imperativa que amarra o decodificador de tokens do LLM a um contrato de dados estrito (`BaseModel`), eliminando falhas de parsing de strings no backend.
* **Field Metadata Injection:** Injeção de metadados nativos via propriedades do `Field(description="")` que atuam diretamente como instruções de prompt contextuais em runtime.
* **Mime-Type Enforcement:** Configuração estrita de `response_mime_type="application/json"` operando sob baixa entropia ($T=0.1$) para garantir saídas de dados determinísticas.

🛠️ Execução Prática (`aula_d5_structured_output.py`)
* Reconstrução limpa do ambiente virtual (`~/dev/.venv`) para expurgar referências absolutas de caminhos antigos do Linux.
* Execução bem-sucedida do motor de extração de metadados SEO. O payload retornou um JSON puro estruturado, contendo arrays de palavras-chave extraídas e scores inteiros calculados diretamente da API do Gemini-2.5-Flash.

---

## 📚 Dia 16 (Módulo 1 - Dia 6): Prompt Defensivo e Tratamento de Exceções
**Data:** 2026-05-27 | **Status:** 🏁 MÓDULO 1 CONCLUÍDO COM SUCESSO

🧠 Conquistas Arquiteturais
* **XML Data Encapsulation:**
Isolamento absoluto de inputs de usuários dentro de delimitadores estruturais, neutralizando ataques de Prompt Injection.
* **Network Exception Guard:**
Implementação de interceptadores estritos (`try/except APIError`) para capturar falhas de timeout, cota e rede sem derrubar o processo local.


## 📊THE FIREWALL ARCHITECTURE

                         [RAW USER INPUT] 
                                │ 
                                ▼
    ┌────────────────────────────────────────────────────────┐ 
    │ 1. DEFENSIVE ENCAPSULATION LAYER                       │ 
    │ - XML Tagging (<user_payload>...</user_payload>)       │ -> (Day 6) Clears instruction bias
	└─────────────────────────┬──────────────────────────────┘ 
	                         │ 
	                         ▼
    ┌────────────────────────────────────────────────────────┐
	│ 2. PROMPT FRAMEWORK BALANCING                          │ 
	│ - System Instructions (Low Entropy: T=0.1)             │ -> (Day 2-4) Limits token randomness                                           
	└─────────────────────────┬──────────────────────────────┘ 
	                         │
	                         ▼ 
	┌────────────────────────────────────────────────────────┐ 
	│ 3. CONSTRAINED DECODING BACKEND                        │ 
	│ - Pydantic BaseModel Validation                        │ -> (Day 5) Blocks non-compliant JSON                                                         
	└─────────────────────────┬──────────────────────────────┘ 
	                         │ 
	                          ▼ 
	    [SECURE STRUCTURED OUTPUT] (100% Valid JSON Object)


## 📂 M1 Index Synchronization

~/dev/
├── .venv/                         <-- The Single, Master Execution Sandbox
├── 01-AI_LLMs/
│     └── 5-Structures_Outputs/
│           └── pipeline_avancado.py   <-- Historical Module 0 Masterwork
└── 02-APIs_Prompt_Engineering/
      └── D_05_06_Pipeline/
            ├── .env                   <-- Secured API Credentials (Hidden)
            ├── aula_d5_structured_output.py  <-- Pydantic Data Contract
            └── aula_d6_defensive_handling.py <-- Defensive System Security
            