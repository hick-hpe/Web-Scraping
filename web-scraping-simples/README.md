# Web Scraping Simples

A raspagem de dados simples atua em sites nos quais os conteúdos estão todos no próprio HTML, de forma estática. Para esta abordagem, utilizaremos as bibliotecas `BeatifullSoup`.

## Prática do Web Scraping

Segue o passo a passo:

- **Instale as bibliotecas**:
    ```
    pip install requests beautifulsoup4 
    ```

- **Executar o arquivo de exemplo**:
    ```
    cd web-scraping-simples
    python ws-simples.py
    ```

## Explicação do código

### 1. Importação das bibliotecas:
```python
import requests
from bs4 import BeautifulSoup
```

### 2. Tratamento de erro:
```python
try:
    # código que tentará ser executado
except requests.exceptions.RequestException as e:
    # caso lance uma exceção (erro)
```

### 3. Definimos a url:
```python
url = "https://quotes.toscrape.com"
```

### 4. Fazemos a requisição:
```python
resposta = requests.get(url)
resposta.raise_for_status()
```

### 5. Converte o conteúdo HTML da página em um objeto BeautifulSoup:
```python
pagina = BeautifulSoup(resposta.text, 'html.parser')
```

### 6. Busca todas as divs que contêm citações:
```python
citacoes = pagina.find_all('div', class_='quote')
```

### 7. Exibir as citações:
```python
for citacao in citacoes:
    texto = citacao.find('span', class_='text').get_text()
    autor = citacao.find('small', class_='author').get_text()
    print(f"Citação: {texto}\nAutor: {autor}\n")
```

## Filtrar os elementos

Além de buscar os elementos diretamente pelos atributos, podemos utilizar também funções comuns ou lambdas para filtrar os elementos desejados.

### Exemplo

Para exemplificar, buscaremos apenas por citações curtas, aquelas com até 100 caracteres.

### 1. Criar a função

```python
def get_citacao_curtas(tag):
    return (
        tag.name == 'span'
        and 'text' in tag.get('class', [])
        and len(tag.get_text()) <= 100
    )
```

### 2. Utilizando a função:

Substituir o trecho `citacao.find('span', class_='text').get_text()` por `tag_texto = citacao.find(get_citacao_curtas)`

Ajustes no `for` para exibir apenas as citações curtas:
```python
for citacao in citacoes:
    autor = citacao.find('small', class_='author').get_text()
    
    tag_texto = citacao.find(get_citacao_curtas)
    if not tag_texto:
        continue
    
    texto = tag_texto.get_text()
    print(f"Citação: {texto}\nTamanho: {len(texto)}\nAutor: {autor}\n")
```

### Exemplo com função lambda:
Função `lambda` é uma função anônima (sem nome) que pode ser definida em uma única linha. Ela substitui a função nomeada e é útil quando a lógica é simples e usada uma única vez. Adaptando o exemplo:

```python
tag_texto = citacao.find(
    lambda tag: (
        tag.name == 'span' 
        and 'text' in tag.get('class', []) 
        and len(tag.get_text()) <= 100
    )
)
```

Trecho do `for` atualizado:
```python
for citacao in citacoes:
    autor = citacao.find('small', class_='author').get_text()
    
    tag_texto = citacao.find(
        lambda tag: (
            tag.name == 'span' 
            and 'text' in tag.get('class', []) 
            and len(tag.get_text()) <= 100
        )
    )
    
    if not tag_texto:
        continue
    
    texto = tag_texto.get_text()
    print(f"Citação: {texto}\nTamanho: {len(texto)}\nAutor: {autor}\n")
```
