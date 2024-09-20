import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
# Verificando se a API_KEY foi carregada com sucesso
if api_key:
    print("Chave de API carregada com sucesso:", api_key)
else:
    print("Chave de API não encontrada no arquivo .env.")