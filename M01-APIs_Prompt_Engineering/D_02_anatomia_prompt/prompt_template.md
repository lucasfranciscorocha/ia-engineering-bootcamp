# ROLE
Atuas como um Engenheiro DevOps especialista em parsing e segurança no Ubuntu Linux.

# TASK
Analisa o log brutos de autenticação fornecido abaixo e extrai as tentativas de login falhadas.

# CONSTRAINTS
- Extrai apenas eventos que contenham "*Failed* password" ou "*Authentication failure*".
- Ignora conexões bem-sucedidas.
- A saída deve ser exclusivamente a tabela Markdown, sem texto introdutório ou conclusivo.

# FEW-SHOT EXAMPLES

[EXEMPLO 1]
INPUT:
May 19 12:01:02 server1 sshd[12345]: *Failed* password for invalid user admin from 192.168.1.50 port 54321 ssh2
OUTPUT:
| Data | Utilizador | IP de Origem | Serviço |
| :--- | :--- | :--- | :--- |
| May 19 12:01:02 | admin (inválido) | 192.168.1.50 | sshd |

[EXEMPLO 2]
INPUT:
May 19 12:05:00 server1 sshd[12346]: **Accepted** password for lucasrocha from 10.0.0.5 port 54322 ssh2
OUTPUT:
(Nenhum output gerado - log de sucesso ignorado)

# ACTUAL DATA TO PROCESS
INPUT:
May 19 13:45:10 server1 sshd[19992]: *Failed* password for root from 203.0.113.5 port 39221 ssh2
May 19 13:46:02 server1 sshd[19995]: **Accepted** password for andreia from 10.0.0.8 port 39222 ssh2
May 19 13:47:15 server1 sshd[20001]: *Failed* password for invalid user guest from 198.51.100.12 port 41123 ssh2

# @"Resposta do exercício"
**OUTPUT:**
| Data | Utilizador | IP de Origem | Serviço |
| :--- | :--- | :--- | :--- |
| May 19 13:45:10 | root (inválido) | 203.0.113.5 | sshd | - *%% Seguir a risca os dados de INPUT - ERRO no Usuário%%*
| May 19 13:47:15 | guest (inválido) | 198.51.100.12 | sshd | - *%% Seguir a risca os dados de INPUT - ERRO no Usuário%%*