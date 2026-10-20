from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

# Recuperar variables
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key:
    print("Clave encontrada")
else:
    print("Clave NO encontrada")
