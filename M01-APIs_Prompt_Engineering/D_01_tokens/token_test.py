import tiktoken

# Carrega o tokenizador padrão do GPT-4 / GPT-4o
enc = tiktoken.get_encoding("cl100k_base")

text = "Engenharia de Prompt com LLMs!"
tokens = enc.encode(text)

print("-" * 50)
print(f"Texto original: {text}")
print(f"IDs dos Tokens: {tokens}")
print(f"Número total de tokens: {len(tokens)}")
print("-" * 50)
print("Decomposição cirúrgica dos tokens:")
for t in tokens:
    # Decodifica ID por ID para ver o fragmento exato
    fragmento = enc.decode([t])
    print(f"ID: {t:<6} -> Fragmento: [{fragmento}]")
print("-" * 50)
