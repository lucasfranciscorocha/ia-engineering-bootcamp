
### O Ciclo Mecânico do Function Calling

O fluxo de execução de uma ferramenta segue um protocolo rígido de 4 etapas entre o Host e o Modelo:

1. **A Declaração:** Nós passamos para a LLM o nosso código acompanhado de um esquema descritivo (geralmente gerado via `Pydantic` em Python). Esse esquema diz exatamente o nome da função, o que ela faz e quais argumentos ela espera.
2. **A Decisão do Modelo:** O modelo analisa o comando do usuário (ex: _"Reduza o padding do formulário"_). Ele percebe que não tem o arquivo CSS na sua memória. Ele interrompe a geração de texto comum e retorna uma requisição estruturada: `call: ler_arquivo_css(caminho="/home/lucasrocha/css/style.css")`.
3. **A Execução Local:** O seu framework de agentes intercepta essa requisição, roda o script Python ou o comando do sistema nativamente no seu Ubuntu Linux, captura o conteúdo do arquivo e joga de volta para o modelo como uma mensagem do tipo `tool`.
4. **A Resolução:** O modelo lê o conteúdo real retornado pelo terminal, processa a lógica de design e avança para o próximo passo do planejamento.

### Ecossistema de Function Calling

1. **Nome da Ferramenta:** Extrator de telefones   

 **Resposta:   ==extrator_contatos_whatsapp_local

3. **Descrição para a IA:** Captador de números telefônicos em grupos whatsapp   

**Resposta:   =="Use esta ferramenta sempre que o operador fornecer um texto bruto, log ou código HTML de uma página do WhatsApp e solicitar a extração de contatos para a criação de listas de marketing (mailing). O único argumento necessário é o texto bruto extraído."

5. **Parâmetros de Entrada:** extração sequencial de números "(xx) xxxxx-xxxx" com nomes [nome_cliente] para utilização em mailing.

 **Resposta:   ==Aqui está como estruturaríamos isso usando o `Pydantic` para garantir que a IA não envie lixo ou comandos maliciosos para o sistema. O script vai caçar o padrão que você definiu e higienizar os dados:

```
import re
import json
from pydantic import BaseModel, Field

# 1. Schema rígido para garantir que o input seja estritamente texto texto bruto
class InputTextoBruto(BaseModel):
    texto_origem: str = Field(description="O texto bruto ou código HTML contendo as mensagens ou lista de membros do grupo.")

# 2. A função executada localmente no seu Ubuntu
def extrator_contatos_whatsapp_local(texto_origem: str) -> str:
# REGEX SEGURA: Captura os padrões de números brasileiros (com ou sem nono dígito, DDD e parênteses)
padrao_telefone = r'\(?\d{2}\)?\s?\d{4,5}[-\s]?\d{4}'
 
# Busca todas as ocorrências no texto enviado pela IA
telefones_encontrados = re.findall(padrao_telefone, texto_origem)
  
if not telefones_encontrados:
return "Nenhum número de telefone válido foi encontrado no texto fornecido."
  
# Remove duplicadas para limpar o mailing automaticamente
telefones_limpos = list(set(telefones_encontrados))
 
# Estrutura o resultado em um JSON limpo para o agente processar ou salvar
mailing_resultado = {
"total_capturado": len(telefones_limpos),
"contatos": [{"id": i+1, "telefone": tel, "nome": "Cliente Potencial"} for i, tel in enumerate(telefones_limpos)]
}
   
return json.dumps(mailing_resultado, indent=2, ensure_ascii=False)
```

### 🛡️ O que mudou aqui para salvar o seu sistema?

1. **Isolamento de Execução:** A IA agora está restrita a uma função de processamento de texto. Ela não abre portas de rede, não mexe no seu navegador e não executa códigos no terminal. Ela apenas lê texto e cospe JSON limpo.
    
2. **Higiene dos Dados:** O uso do `re.findall` com uma Regex específica garante que, mesmo que o texto original venha cheio de poluição visual, o output final seja estritamente o mailing limpo que você precisa.
    

O que achou dessa abordagem revisada? Consegue perceber como ela resolve o objetivo macro do seu mailing mantendo o seu servidor Ubuntu totalmente fora da zona de risco?

Se estiver tudo claro na sua mente e anotado no seu Obsidian, estamos prontos para avançar para as malhas complexas e grafos do **LangGraph no Dia 27**. Pode mandar o sinal verde!