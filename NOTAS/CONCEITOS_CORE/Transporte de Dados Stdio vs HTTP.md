# 🔄 Transporte de Dados: Stdio vs HTTP (Arquitetura de Mensageria)

### ⚙️ O Conceito
Modelos de Contexto Protocolar (MCP) locais não dependem de requisições de rede (HTTP/REST) para conversar com a sua máquina; eles usam os canais nativos do Kernel do Linux: **Stdio (Standard Input/Output)**.
* **Standard Input (stdin):** O canal por onde o cliente (ex: Claude) envia comandos JSON para o servidor.
* **Standard Output (stdout):** O canal por onde o servidor devolve o resultado para o cliente.

### 🚨 A Regra de Ouro do Engenheiro (Anti-Crash)
Em sistemas baseados em Stdio, **o fluxo de dados é sagrado**. O uso de um comando de output simples como `print()` no escopo global do seu código joga caracteres puros no canal `stdout`. Isso corrompe o pacote estruturado JSON-RPC, quebrando a comunicação instantaneamente e resultando em erros de *Broken Pipe* (`EPIPE`).