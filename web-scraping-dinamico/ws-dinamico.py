"""
Exemplo 3: Obter citações de um site com conteúdo dinâmico.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o Chrome
options = webdriver.ChromeOptions()

# Executa o chrome em segundo plano(sem abrir janela)
options.add_argument("--headless")

# abrir o Chrome, baixar e configura automaticamente o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    url = "https://quotes.toscrape.com/js"
    driver.get(url)
    time.sleep(2)  # Aguarda JS carregar

    # Pega todas as citações renderizadas
    citacoes = driver.find_elements(By.CLASS_NAME, "quote")

    for c in citacoes:
        texto = c.find_element(By.CLASS_NAME, "text").text
        autor = c.find_element(By.CLASS_NAME, "author").text
        print(f"Citação: {texto}\nAutor: {autor}\n")

finally:
    driver.quit()
