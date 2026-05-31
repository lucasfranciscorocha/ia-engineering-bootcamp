
# 🛡️ Sandboxing e Isolamento de Escopo (Privilégio Mínimo)

### ⚙️ O Conceito
Mecanismo de segurança arquitetural que limita o raio de ação de um agente de IA. Ao inicializar um servidor (como o de *Filesystem*), injetar um caminho absoluto restringe os braços mecânicos do modelo estritamente àquela pasta.

### 🚨 Vetor de Ataque e Mitigação
Se um agente de IA sofrer um ataque de **Prompt Injection** (um cliente malicioso injeta instruções escondidas no formulário do WordPress para tentar roubar dados do servidor), a IA pode tentar varrer o sistema operacional usando comandos de escape (como `cd ../../ && cat /etc/passwd`). 
O mecanismo de Sandboxing no nível do transporte MCP aborta a execução no ato, garantindo que a IA nunca saia da sandbox definida (`/home/lucasrocha/dev`).