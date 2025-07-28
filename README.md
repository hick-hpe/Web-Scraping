# Web-Scraping

Web Scraping é a automatização da coleta de dados de websites, convertendo-os em informações estruturadas para análise posterior. Em vez de copiar e colar manualmente, um programa (chamado de scraper ou crawler) acessa o código HTML da página, extrai os dados desejados e os organiza de forma estruturada, como CSV, JSON ou até em bancos de dados.

## Prática do Web Scraping

Segue o passo a passo:

- Escolha do site:
    Para exemplificar, foi escolhido o site [https://quotes.toscrape.com](https://quotes.toscrape.com), que é o recomendado para essa finalidade.

- Clone o repositório:
    ```
    git clone https://github.com/hick-hpe/Web-Scraping
    ```

- Instale as bbliotecas:
    ```
    pip install requests beautifulsoup4 
    ```
- Executar o arquivo de exemplo:
    ```
    python exemplo1.py
    ```

## Explicação do arquivo

- Importação das bibliotecas:
    ```python
    import requests
    from bs4 import BeautifulSoup
    ```

- Tratamento de erro:
    ```python
    try:
        # código que tentará ser executado
    except requests.exceptions.RequestException as e:
        # caso lance uma exceção (erro)
    ```

- Definimos a url:
    ```python
    url = "https://quotes.toscrape.com"
    ```
