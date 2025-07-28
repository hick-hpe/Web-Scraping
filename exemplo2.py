import requests
from bs4 import BeautifulSoup


# função para raspar citações curtas
def get_citacao_curtas(tag):
    return (
        tag.name == 'span' and len(tag.get_text()) < 100
    )

try:
    # URL do site que será raspado
    url = "https://quotes.toscrape.com"

    # Fazendo a requisição HTTP para obter o conteúdo da página
    resposta = requests.get(url)
    resposta.raise_for_status()  # Lança exceção se status != 200

    # Analisando o conteúdo da página com BeautifulSoup
    pagina = BeautifulSoup(resposta.text, 'html.parser')

    # Encontrando todas as citações na página
    citacoes = pagina.find_all('div', class_='quote')

    # Exibindo as citações encontradas que não contenham o texto 'be'
    for citacao in citacoes:
        autor = citacao.find('small', class_='author').get_text()

        # utilizando uma função para filtrar citações curtas
        texto = citacao.find(get_citacao_curtas).get_text()
        
        if not texto:
            continue
        print(f"Citação: {texto}\nAutor: {autor}\n")    

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a página:", e)

