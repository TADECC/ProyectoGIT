import os

from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Recuperar variables
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key:
    print("Clave encontrada")
else:
    print("Clave NO encontrada")
