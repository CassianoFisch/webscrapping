from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opts)

url = r'https://www.dell.com/pt-br'
navegador.get(url)

try:
    pesquisa2 = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "mh-search-input"))
    )
    pesquisa2.send_keys("Notebook gamer Alienware m16 R2")
    pesquisa2.send_keys(Keys.RETURN)

    preco_elemento = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ps-dell-price.ps-simplified"))
    )
    preco = preco_elemento.text.strip()

    with open("preco_notebook3.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Preço do Notebook Alienware m16 R2: {preco}\n")

    print(f"Preço do Notebook Alienware m16 R2: {preco} foi salvo em 'preco_notebook3.txt'.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    navegador.quit()