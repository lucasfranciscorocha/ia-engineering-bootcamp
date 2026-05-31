
# 📖 Glossário Global: Engenharia de IA & Arquitetura de Sistemas

Este ficheiro constitui o repositório central atemporal de jargões industriais, conceitos computacionais e mecânicas de baixo nível adotados na infraestrutura da **Personal Help Desk**.

---

### 🅰️ A
* **Análise Estatística de I/O (Input/Output):** A medição, auditoria e rastreio de como o sistema operacional lê (Input) e escreve (Output) pacotes físicos de dados no disco rígido (SSD/HD).
* **Aquecimento do Cache (Cache Warming):** Prática de pré-instalar, descarregar ou executar componentes de software antes da sua utilização principal, garantindo que o sistema encontre os ficheiros prontos no disco local, reduzindo a latência ao mínimo (< 10ms).
* **Árvores de Dependência (`node_modules`):** A estrutura de pastas aninhadas e encadeadas onde o ecossistema Node guarda todas as sub-bibliotecas e pacotes de terceiros que um determinado projeto precisa para ser executado.

### 🅲 C
* **Cache Efêmero:** Área de armazenamento temporário no disco que retém ficheiros descarregados da internet para acelerar execuções subsequentes, podendo ser limpa sem corromper o núcleo do sistema operacional.
* **Caminho Absoluto (Absolute Path):** O endereço completo e inequívoco de um ficheiro ou diretório a partir da raiz do sistema operacional (ex: `/home/lucasrocha/...`), garantindo que um comando ou processo funcione em qualquer escopo de execução em background.
* **Ciclo de Vida (Lifecycle):** O fluxo completo de fases operacionais de um software, abrangendo a sua instalação, carregamento em memória RAM, execução ativa, até ao seu encerramento seguro e limpeza de resíduos no sistema.
* **Cold Start (Arranque a Frio):** O atraso ou latência que ocorre quando um sistema precisa de descarregar, compilar ou ler ficheiros do zero na primeiríssima vez que é executado na máquina.

### 🅳 D
* **Dependências:** Bibliotecas, frameworks ou blocos de código desenvolvidos por terceiros que o teu programa principal necessita obrigatoriamente para compilar ou funcionar.
* **Diretórios de Escopo do Sistema:** Pastas globais e protegidas pelo Kernel do Linux (como `/usr/bin` ou `/usr/lib`), onde residem os executáveis principais acessíveis a todos os utilizadores do sistema operacional.
* **du -sh (Disk Usage):** Comando nativo do Linux utilizado para auditar o armazenamento, onde `-s` resume o tamanho total de uma pasta e `-h` formata o output em escala legível para humanos (ex: Megabytes em vez de bytes puros).

### 🅷 H
* **Hashes SHA-256:** Um identificador criptográfico único de comprimento fixo (uma string hexadecimal de letras e números) que funciona como a "impressão digital" digital e imutável de um ficheiro, bloco de código ou diretório de cache.
* **Host Nativo:** O aplicativo cliente principal e definitivo (ex: Claude Desktop) instalado no sistema operacional que consome e orquestra servidores MCP em background.

### 🅻 L
* **Latência de Download:** O tempo de atraso e espera despendido enquanto a ligação de rede comunica com servidores remotos para descarregar pacotes ou atualizações.

### 🅼 M
* **Mapeamento Físico de Execução:** O ato de engenharia de rastrear o endereço de memória ou a pasta física real no disco onde o sistema operacional armazenou e está a rodar os ficheiros de um programa ativo.
* **Multiplexação:** Técnica de arquitetura de redes e sistemas que permite que múltiplos canais ou fluxos de dados independentes (como os canais Stdio de servidores diferentes) trafeguem de forma concorrente e paralela através do mesmo meio lógico de comunicação sem que ocorra colisão de pacotes.

### 🆂 S
* **Sandboxing de Binários:** Técnica de segurança avançada que isola ficheiros executáveis dentro de perímetros lógicos fechados ("caixas de areia"), impedindo que um script corrompa, leia ou polua o resto do sistema operacional do utilizador.
* **stderr (Standard Error):** O canal de saída padrão do Linux reservado nativamente para o direcionamento de mensagens de erro, diagnósticos de falhas e logs críticos gerados por processos de background.
* **Stdio (Standard Input/Output):** O canal bidirecional padrão do Kernel do Linux de entrada (`stdin`) e saída (`stdout`) de dados, utilizado para estabelecer comunicação de latência zero entre dois programas em background.

### 🆃 T
* **tail -f (Follow):** Utilitário nativo do Ubuntu utilizado para ler as linhas finais de um ficheiro de texto de forma viva e assíncrona, imprimindo no terminal novas atualizações no exato milissegundo em que são gravadas no disco.