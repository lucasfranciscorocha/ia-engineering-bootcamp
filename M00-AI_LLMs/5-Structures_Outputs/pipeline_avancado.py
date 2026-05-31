import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# 1. Definimos o contrato do output usando Pydantic (Garantia de JSON Estruturado)
class RelatorioSeguranca(BaseModel):
    ips_unicos_contados: int = Field(description="O número total de endereços IP únicos que falharam a autenticação.")
    ip_mais_perigoso: str = Field(description="O endereço IP que registou o maior número de tentativas de ataque.")
    nivel_de_risco: str = Field(description="Nível de risco determinado: BAIXO, MÉDIO ou ALTO.")
    justificativa_tecnica: str = Field(description="Breve justificação da análise de segurança.")

def gerar_output_estruturado():
    client = genai.Client()
    
    prompt_dados = """
    Analisa as seguintes linhas de log do Ubuntu e extrai as métricas de segurança exigidas no esquema de saída.
    
    LOGS:
    10:00:01 - Failed password for root from 192.168.1.105 port 22
    10:01:23 - Failed password for admin from 192.168.1.110 port 22
    10:02:15 - Failed password for root from 192.168.1.105 port 22
    10:03:00 - Accepted password for lucasrocha from 10.0.0.5 port 22
    10:04:12 - Failed password for guest from 192.168.1.105 port 22
    10:05:59 - Failed password for invalid user oracle from 172.16.0.45 port 22
    """

    # 2. Configuração Avançada da API forçando o formato JSON baseado no nosso Modelo Pydantic
    config = types.GenerateContentConfig(
        temperature=0.0, # Determinístico para extração de dados brutos
        response_mime_type="application/json",
        response_schema=RelatorioSeguranca,
    )
    
    print("🛰️ Enviando dados para o Gemini com restrição de esquema JSON...")
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_dados,
        config=config
    )
    
    print("\n📦 REQUISIÇÃO CONCLUÍDA! OUTPUT JSON PURO:")
    print("-" * 60)
    print(response.text)
    print("-" * 60)

if __name__ == "__main__":
    gerar_output_estruturado()