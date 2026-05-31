--- 
# 🛠️ Dicionário Centralizado de Comandos: Ecossistema de IA & Infraestrutura

Este arquivo centraliza todos os snippets práticos, comandos brutos e orientações de troubleshooting acumulados ao longo das aulas. Ele foi desenhado para busca rápida no dia a dia profissional da agência (**Personal Help Desk**), mapeando a ação necessária diretamente com o contexto teórico de origem.

## 🚨 As 3 Regras de Ouro 
1. **Regra do Clique Duplo:** Se você demorar mais de dois cliques para achar um comando no seu Obsidian, a organização faliu. Use títulos diretos com verbos de ação (ex: "Como limpar cache", "Como forçar conexão").
2. **O Código é o Dono, o Comentário é o Guia:** Sempre que guardar um comando, coloque um comentário curto em cima explicando o parâmetro mais difícil. 
3. **Abuse das Tags Transversais:** Em vez de separar por pastas de linguagens, use tags no topo da nota. Exemplo: `#mcp #python #linux`. Assim, se você buscar pela tag `#linux`, o Obsidian traz tudo o que interage com o sistema, seja via Python ou via terminal.


---

## 📦 Ecossistema Node (NPM & NPX)

### ⚡ Execução Efêmera de Ferramentas e Servidores (Sem Instalação Global)
* **Rodar o MCP Inspector local de forma isolada:**
```bash
  npx @modelcontextprotocol/inspector
```

- **Parâmetro Crítico:** O `npx` baixa o pacote diretamente para o cache do usuário e o descarta após o encerramento do processo (`Ctrl + C`), mantendo os binários do sistema limpos e sem poluição global.
- **Origem do Conceito:** [[notas_Extensão_NPM_NPX_Python.md#Dia 23]]


**Ignorar checagem de token de autenticação do Inspector (Modo Dev):**
    
```
    DANGEROUSLY_OMIT_AUTH=true npx @modelcontextprotocol/inspector
```
    
- **Parâmetro Crítico:** Remove a barreira do token randômico (`MCP_PROXY_AUTH_TOKEN`) para acelerar testes locais. **Aviso de Segurança:** Não utilizar em ambientes de rede pública ou corporativa exposta.
    
- **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 22]]

### 🔍 Auditoria, Debug e Gerenciamento de Cache no Linux

- **Verificar o tamanho ocupado pelos servidores MCP no cache do npx:**
    
    ```
    du -sh ~/.npm/_npx/* 2>/dev/null
    ```
    
    - **Parâmetro Crítico:** Lista os hashes SHA-256 das sandboxes temporárias criadas pelo Node para rodar os servidores. Essencial para debugar se o download foi concluído ou se há corrupção local.
        
    - **Origem do Conceito:** [[notas_Extensão_NPM_NPX_Python.md#Dia 23]]

### 🚨 Resolução de Erros Comuns de Infraestrutura (Troubleshooting Node)

- **Falha `ENOENT` no disparo do npx:**
    
    - **Causa:** O Node não encontrou o comando ou o caminho relativo passado no script de configuração.
        
    - **Solução:** Substituir caminhos relativos por caminhos absolutos baseados no sistema operacional (Ex: `/home/lucasrocha/...`).
        
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 22]]
        
- **Falha `EPIPE` (Broken Pipe) no transporte Stdio:**
    
    - **Causa:** O processo filho (servidor Python/Node) morreu em background ou fechou o canal de comunicação inesperadamente antes do envio dos dados.
        
    - **Solução:** Validar se há processos órfãos travando a execução ou erros de sintaxe internos usando comandos de `pkill`.
        
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 22]]

## 🖥️ Infraestrutura e Shell Linux (Ubuntu)

### 🩺 Diagnóstico e Gerenciamento de Processos (Process Clean-up)

- **Matar de forma forçada processos órfãos que travam servidores MCP:**
    
    Bash
    
    ```
    pkill -f mcp
    ```
    
    - **Parâmetro Crítico:** O sinal `-f` faz o `pkill` buscar o padrão "mcp" na linha de comando inteira do processo, e não apenas no nome do binário. Crucial para encerrar servidores Python e instâncias do Node presas na memória RAM após o fechamento abrupto do terminal.
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 22]]
        
### 📂 Auditoria de Armazenamento e Permissões de Disco

- **Verificar o espaço em disco de diretórios ocultos de forma legível (Human-Readable):**
    
    ```
    du -sh ~/.npm/_npx/* 2>/dev/null
    ```
    
    - **Parâmetro Crítico:**
        
        - `du`: _Disk Usage_ (Uso de Disco).
            
        - `-s`: _Summarize_ (exibe apenas o total acumulado de cada argumento, impedindo que o terminal despeje milhares de subpastas na tela).
            
        - `-h`: _Human-Readable_ (converte os bytes brutos em unidades compreensíveis como KB, MB ou GB).
            
        - `2>/dev/null`: Redireciona mensagens de erro de permissão ou pastas inexistentes para o dispositivo nulo do Linux, mantendo o output limpo.
            
    - **Origem do Conceito:** [[notas_Extensão_NPM_NPX_Python.md#Dia 23]]
        

### 🛠️ Resolução de Erros de Escopo do Kernel (Troubleshooting POSIX)

- **Tratamento de Falhas de Caminho com Códigos POSIX Nativos:**
    
    - **Erro `ENOENT` (Error No Entity):** Ocorre quando o Shell tenta invocar um binário ou ler um caminho que não existe no escopo global ou local.
        
    - **Erro `EPIPE` (Broken Pipe / Cano Quebrado):** Ocorre na camada de transporte de I/O quando o Host tenta empurrar um stream de dados para um subprocesso que colapsou e fechou sua entrada padrão (`stdin`).
        
    - **Ação Corretiva:** Abandonar o uso de caminhos relativos (`./`) em arquivos de configuração e injetar caminhos absolutos (`/home/lucasrocha/...`) mapeados em tempo de execução.
        
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 22]]
        

## 🐍 Ecossistema Python & Ambientes Virtuais

### 📦 Isolamento de Dependências (Sandboxing com venv)

- **Ativar o ambiente virtual isolado do projeto:**
    
    Bash
    
    ```
    source ~/dev/.venv/bin/activate
    ```
    
    - **Parâmetro Crítico:** Redireciona os caminhos de execução do sistema para utilizar o interpretador Python e os pacotes instalados estritamente dentro da pasta local `.venv`, protegendo o escopo global do sistema operacional contra poluição de dependências.
        
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 19]]
        
- **Desativar o ambiente virtual e retornar ao interpretador padrão do sistema:**
    
    Bash
    
    ```
    deactivate
    ```
    
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 19]]
        

### 🚀 Inicialização e Execução do Motor MCP

- **Disparar um servidor customizado baseado no protocolo de baixo nível ou FastMCP:**
    
    Bash
    
    ```
    ~/dev/.venv/bin/python3 aula_d21_custom_server.py
    ```
    
    - **Parâmetro Crítico:** Chamar o binário do Python apontando diretamente para o caminho absoluto dentro da `.venv` garante que o servidor rode com todas as bibliotecas necessárias, mesmo se o comando for disparado por um Host externo (como o Claude Desktop) em background.
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 19]]
        

### ⚡ Primitivos de Código para Escrita de Servidores (FastMCP Blueprint)

- **Estrutura base assíncrona concorrente para tratamento de I/O de mensagens:**
    
    Python
    
    ```
    import asyncio
    # Orquestra as streams de leitura/escrita JSON-RPC sem bloquear o terminal Ubuntu
    asyncio.run(seu_metodo_principal())
    ```
    
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 19]]
        
- **Evitar corrupção de pacotes JSON-RPC via Stdio:**
    
    - **Regra de Ouro:** Nunca utilizar o comando nativo `print()` no escopo global de execução do servidor MCP. O `print()` joga strings brutas no `stdout`, corrompendo a stream de mensageria estruturada que o cliente espera ler, resultando em falhas instantâneas de conexão.
        
    - **Origem do Conceito:** [[notas_Vector Mathematics_MCP.md#Dia 19]]


### 🚀 Injeção e Inicialização de Servidores Públicos via MCP Inspector
* **Disparar o MCP Inspector acoplado ao servidor oficial de Filesystem:**
  ```bash
  DANGEROUSLY_OMIT_AUTH=true npx @modelcontextprotocol/inspector npx -y @modelcontextprotocol/server-filesystem /home/lucasrocha/dev
  ```
  - **Parâmetro Crítico:** * `npx -y`: O sinal `-y` (yes) força o Node a aceitar automaticamente a instalação e o download do pacote do servidor de arquivos em background, impedindo que o terminal trave aguardando uma confirmação manual do usuário.
    
    - `/home/lucasrocha/dev`: Delimita o escopo de atuação da IA. O servidor de filesystem restringe as permissões de leitura e escrita (`read_text_file`, `write_file`, `edit_file`) estritamente a este path absoluto, aplicando o princípio do privilégio mínimo.
        
- **Origem do Conceito:** [[notas_Extensão_NPM_NPX_Python.md]]

### 📂 Gerenciamento de Escopo e Persistência de Ambiente
* **Injetar e persistir variáveis de ambiente no escopo do usuário:**
  ```bash
  echo 'export GEMINI_API_KEY="sua_chave_aqui"' >> ~/.bashrc && source ~/.bashrc
  ```

#### ***Log do Inspector: `No valid root directories provided by client`:**
  * **Causa:** O servidor de Filesystem inicializou corretamente via Stdio, mas a interface web do Inspector ainda não enviou uma requisição contendo o caminho absoluto permitido.
  * **Status:** Normal/Esperado. O aviso desaparece assim que uma ferramenta (Ex: `list_directory`) é invocada passando o path mapeado no terminal, ou quando o servidor é rodado diretamente por um Host nativo (Claude Desktop) que já injeta os diretórios nos argumentos de boot.
  * **Origem do Conceito:** [[sandboxing_seguranca.md]]


### 🛡️ Auditoria de Escopo e Simulação de Path Absoluto (Sanity Check)
* **Validar a existência real e o escopo de caminhos antes da injeção no JSON do Host:**
  ```bash
  ls -la /home/lucasrocha/dev && file /home/lucasrocha/dev/aula_d21_custom_server.py
  ```
  - **Parâmetro Crítico:** O operador `&&` garante a execução sequencial segura (o segundo comando só roda se o primeiro for bem-sucedido). O utilitário `file` analisa o cabeçalho do arquivo para confirmar se ele é um script de texto legível pelo interpretador Python, evitando que o Host Nativo levante um subprocesso quebrado ou corrompido em background.
- **Origem do Conceito:** [[sandboxing_seguranca.md]]