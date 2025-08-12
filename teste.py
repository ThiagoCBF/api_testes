import requests

indicadores = 77819

url = f'https://servicodados.ibge.gov.br/api/v1/rmpg/maregrafos'
resposta = requests.get(url)

print(resposta.json())