import requests
from bs4 import BeautifulSoup

# URL do site que será raspado
url = "https://quotes.toscrape.com"

# Fazendo a requisição HTTP para obter o conteúdo da página
resposta = requests.get(url)

# Verificando se a requisição foi bem-sucedida
print(resposta.text)

# Exibindo o status da requisição
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro ao acessar a página:", resposta.status_code)

# Analisando o conteúdo da página com BeautifulSoup
pagina = BeautifulSoup(resposta.text, 'html.parser')

# Encontrando todas as citações na página
citacoes = pagina.find_all('div', class_='quote')

# Exibindo as citações encontradas
for citacao in citacoes:
    texto = citacao.find('span', class_='text').get_text()
    autor = citacao.find('small', class_='author').get_text()
    print(f"Citação: {texto}\nAutor: {autor}\n")
    
