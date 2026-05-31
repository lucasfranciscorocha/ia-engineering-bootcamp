import tiktoken

def analisar_contexto():
    # Usando o tokenizer padrão do ecossistema aberto para simular a quebra de strings
    enc = tiktoken.get_encoding("cl100k_base")
    
    # Texto simulando uma injeção de código ou string que o teu sistema vai processar
    prompt_usuario = "Estou a configurar o meu Cockpit de Arquitetura Digital no Ubuntu."
    
    # Codificação: Transforma texto bruto em IDs numéricos que entram no Transformer
    tokens = enc.encode(prompt_usuario)
    
    print("-" * 50)
    print(f"Texto Original: '{prompt_usuario}'")
    print(f"Quantidade de Caracteres: {len(prompt_usuario)}")
    print(f"Quantidade de Tokens Gerados: {len(tokens)}")
    print(f"IDs dos Tokens no Espaço Vetorial: {tokens}")
    print("-" * 50)
    
    # Exibindo a fragmentação real (o que a IA realmente lê)
    print("Fragmentação Semântica:")
    for token_id in tokens:
        fragmento = enc.decode([token_id])
        print(f"ID {token_id} -> '{fragmento}'")

if __name__ == "__main__":
    analisar_contexto()
