#Instalar biblotecas
#pip install requests

#segundo passo: adicionar/importar ao codigo
import requests

url = "https://viacep.com.br/ws/13468390/json/"

dados = requests.get(url).json()

print(dados)
