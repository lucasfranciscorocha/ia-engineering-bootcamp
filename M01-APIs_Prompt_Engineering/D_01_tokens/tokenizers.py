import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Ensure the system environment variable is being parsed
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("CRITICAL: HF_TOKEN environment variable is missing!")

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

# The library automatically grabs the token from the OS environment
tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
print(f"Successfully loaded tokenizer for {model_id} native space.")