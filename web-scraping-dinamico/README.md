# Web Scraping Dinâmico

A raspagem de dados dinâmica atua em sites nos quais os conteúdos não estão diretamente no HTML, mas sim gerados dinamicamente pelo JavaScript. Para esta abordagem, utilizaremos as bibliotecas `BeatifullSoup`.

## Prática do Web Scraping

Segue o passo a passo:

- **Instale as bibliotecas**:
    ```
    pip install selenium webdriver-manager
    ```

- **Executar o arquivo de exemplo**:
    ```
    python ws-dinamico.py
    ```
## Explicação do código

### 1. Importação das bibliotecas:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
```

Explicação das bibliotecas:
- `webdriver`: controla o navegador (abrir, fechar, navegar para URLs)
- `By`: fornece localizadores para encontrar elementos na página (ex.: By.CLASS_NAME, By.ID)
- `Service`: configura o serviço do navegador (Chrome), como caminho do driver e inicialização
- `ChromeDriverManager`: faz o download e gerencia automaticamente a versão correta do ChromeDriver
- `time`: pausar a execução do código

### 2. Acessanco o site:
```python
try:
    url = "https://quotes.toscrape.com/js"
    driver.get(url)

    # esperar o JS carregar
    time.sleep(2) 
```

### 3. Obtendo as citações:
```python
citacoes = driver.find_elements(By.CLASS_NAME, "quote")
```

### 4. Exibir as citações:
```python
for c in citacoes:
    texto = c.find_element(By.CLASS_NAME, "text").text
    autor = c.find_element(By.CLASS_NAME, "author").text
    print(f"Citação: {texto}\nAutor: {autor}\n")
```

### 5. Garante que o navegador seja fechado mesmo se ocorrer um erro:

```python
finally:
    driver.quit()
```

## Filtrar os elementos

No `selenium`, não é possível utilizar filtros personalizados, como no `BeatifullSoup`.

Em vez disso, usamos os métodos de localização fornecidos pela biblioteca `By`.

### Exemplos de uso do `By`

- Buscar por tag:
    ```python
    driver.find_elements(By.TAG_NAME, "tag")
    ```

- Buscar por ID:
    ```python
    driver.find_elements(By.ID, "id")
    ```

- Buscar por classe:
    ```python
    driver.find_elements(By.CLASS_NAME, "classe")
    ```

- Buscar por XPATH:
    ```python
    # para lista de elementos
    driver.find_element(By.XPATH, "//elemento[@atributo='valor']")

    # obtendo um elemento específico
    driver.find_element(By.XPATH, "//elemento[@atributo='valor'][n]")
    ```
    Nota:
    - `/`: busca o elemento começando pela raiz.
    - `//`: busca o elemento em qualquer parte da página.
    - `@atributo='valor'`: busca o elemento em qualquer parte da página
    - `n`: posição so elemento, com índice começando pelo 1.

    Pode ser usado tanto para HTML quanto XML.

    Alguns opções de filtros com XPATH:

    | Filtro               | Explicação                                                | Exemplo                                                                 |
    |----------------------|------------------------------------------------------------|-------------------------------------------------------------------------|
    | `string-length()`     | Mede o comprimento do texto                              | `//span[@class='text' and string-length(text()) <= 100]`                |
    | `contains()`          | Verifica se o texto ou atributo contém uma substring     | `//span[contains(text(), 'vida')]`                                      |
    | `starts-with()`       | Filtra elementos cujo texto ou atributo começa com prefixo | `//input[starts-with(@name, 'user')]`                                   |
    | `normalize-space()`   | Remove espaços extras do início, fim e múltiplos espaços internos | `//div[normalize-space(text())='Exemplo']`|
    | `substring()`         | Retorna parte da string a partir de uma posição inicial   | `//span[substring(text(), 1, 4)='Cita']`                                |
    | `position()`          | Retorna a posição do nó dentro do conjunto de resultados | `(//li)[position()=1]` (primeiro item da lista)                         |
    | `last()`              | Seleciona o último elemento do conjunto                   | `(//li)[last()]` (último item da lista)                                 |
    | `not()`               | Retorna nós que não atendem à condição especificada       | `//div[not(@class='hidden')]`                                           |
    | `and`, `or`           | Operadores lógicos para combinar múltiplas condições      | `//input[@type='text' and @name='username']`                            |

    
    Nota: use `@atributo` para se referir aos atributos.

### Buscando as citações curtas

Para exemplificar, buscaremos as citações curtas.

```python
citacoes_curtas = driver.find_elements(
    By.XPATH, "//div[@class='quote']/span[@class='text' and string-length(text()) <= 100]"
)

for c in citacoes:
    texto = c.find_element(By.CLASS_NAME, "text").text
    autor = c.find_element(By.CLASS_NAME, "author").text
    print(f"Citação: {texto}\nAutor: {autor}\n")
```


