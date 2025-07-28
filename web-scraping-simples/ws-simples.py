"""
Web Scraping com Python usando a biblioteca BeautifulSoup.
Exemplo 1: Obter as citações de um site de exemplo.
"""
import requests
from bs4 import BeautifulSoup

try:
    # URL da página que será raspada
    url = "https://quotes.toscrape.com/"

    # Envia uma requisição HTTP GET para a URL
    resposta = requests.get(url)
    resposta.raise_for_status()  # Gera exceção se a resposta não for bem-sucedida (status ≠ 200)

    # Converte o conteúdo HTML da página em um objeto BeautifulSoup
    pagina = BeautifulSoup(resposta.text, 'html.parser')

    # Busca todas as divs que contêm citações
    citacoes = pagina.find_all('div', class_='quote')

    # Itera sobre cada citação encontrada e exibe o texto e o autor
    for citacao in citacoes:
        texto = citacao.find('span', class_='text').get_text()
        autor = citacao.find('small', class_='author').get_text()
        print(f"Citação: {texto}\nAutor: {autor}\n")

except requests.exceptions.RequestException as e:
    # Captura erros de conexão, timeout ou HTTP
    print("Erro ao acessar a página:", e)

