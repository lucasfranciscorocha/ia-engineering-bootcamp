import os
from google import genai
from google.genai import types

def executar_teste_llm(prompt_text, temperatura_valor):
    # Inicializa o cliente - ele busca automaticamente a variável GEMINI_API_KEY
    client = genai.Client()
    
    print(f"\n" + "="*60)
    print(f"🔥 EXECUTANDO COM TEMPERATURA: {temperatura_valor}")
    print("="*60)
    
    # Configuramos os parâmetros técnicos (Dia 4)
    config = types.GenerateContentConfig(
        temperature=temperatura_valor,
        top_p=0.95,
        max_output_tokens=1000,
    )
    
    # Chamada oficial da API usando o modelo mais recente e rápido (Flash)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_text,
        config=config
    )
    
    print(response.text)

# 🧠 CONSTRUÇÃO DO PROMPT COM CHAIN OF THOUGHT (Dia 3)
# Forçamos o modelo a criar uma secção de raciocínio antes de extrair os dados.
prompt_complexo = """
Atuas como um Analista de Segurança Sénior em ambientes Linux.

Tarefa: Analisa o relatório de incidentes abaixo e diz-me quantos IPs únicos tentaram atacar o servidor e qual o IP mais perigoso (com mais tentativas).

Regra Estrita de Raciocínio (Chain of Thought):
Antes de dares a resposta final, deves criar uma secção chamada '### [RACIOCÍNIO PASSO A PASSO]' onde vais listar cada IP encontrado, contar as suas ocorrências e validar se são únicos. Só depois geras a secção '### [RESPOSTA FINAL]'.

DADOS BRUTOS:
10:00:01 - Failed password for root from 192.168.1.105 port 22
10:01:23 - Failed password for admin from 192.168.1.110 port 22
10:02:15 - Failed password for root from 192.168.1.105 port 22
10:03:00 - Accepted password for lucasrocha from 10.0.0.5 port 22
10:04:12 - Failed password for guest from 192.168.1.105 port 22
10:05:59 - Failed password for invalid user oracle from 172.16.0.45 port 22
"""

# Teste 1: Temperatura Baixa (0.0) -> Totalmente determinístico, focado em análise de dados
executar_teste_llm(prompt_complexo, temperatura_valor=0.0)

# Teste 2: Temperatura Alta (1.0) -> Mais criativo na forma de explicar o raciocínio
# executar_teste_llm(prompt_complexo, temperatura_valor=1.0)