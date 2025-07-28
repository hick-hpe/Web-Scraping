# Web Scraping Simples

A raspagem de dados simples atua em sites nos quais os conteúdos estão todos no próprio HTML, de forma estática. Para esta abordagem, utilizaremos as bibliotecas `requests` e `BeatifullSoup`.

## Prática do Web Scraping

Segue o passo a passo:

- **Instale as bibliotecas**:
    ```
    pip install requests beautifulsoup4 
    ```

- **Executar o arquivo de exemplo**:
    ```
    python ws-simples.py
    ```

## Explicação do código

### 1. Importação das bibliotecas:
```python
import requests
from bs4 import BeautifulSoup
```

### 2. Acessanco o site:
```python
try:
    url = "https://quotes.toscrape.com"
    resposta = requests.get(url)

    # lançar uma exeção se status_code != 200
    resposta.raise_for_status()
```

### 3. Converte o conteúdo HTML da página em um objeto BeautifulSoup:
```python
pagina = BeautifulSoup(resposta.text, 'html.parser')
```

### 4. Busca todas as divs que contêm citações:
```python
citacoes = pagina.find_all('div', class_='quote')
```

### 5. Exibir as citações:
```python
for citacao in citacoes:
    texto = citacao.find('span', class_='text').get_text()
    autor = citacao.find('small', class_='author').get_text()
    print(f"Citação: {texto}\nAutor: {autor}\n")
```

### 6. Explcação:
Esse bloco captura possíveis erros durante a requisição HTTP, como:
- Problemas de conexão
- URL inválida
- Resposta com status de erro (4xx ou 5xx)

```python
except requests.exceptions.RequestException as e:
    # Captura exceções de rede ou HTTP e exibe a mensagem de erro
    print("Erro ao acessar a página:", e)
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
