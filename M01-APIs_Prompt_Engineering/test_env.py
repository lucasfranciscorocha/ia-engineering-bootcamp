import os
from dotenv import load_dotenv

# Force python to read variables ONLY from the local .env file
load_dotenv()

print("Checking Environmental Isolation Layer...")
print(f"➔ GEMINI_API_KEY Found: {bool(os.getenv('GEMINI_API_KEY'))}")
print(f"➔ WP_USERNAME Found: {os.getenv('WP_USERNAME')}")
