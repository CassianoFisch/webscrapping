from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opts)

url = r'https://www.dell.com/pt-br'
navegador.get(url)
sleep(2)

pesquisa1 = navegador.find_element(By.ID, "mh-search-input")
pesquisa1.send_keys("Notebook Gamer G15")
pesquisa1.send_keys(Keys.RETURN)

sleep(2)

resultado = navegador.find_element(By.ID, "g5530w251124w1")
resultado.click()

sleep(2)

preco_elemento = navegador.find_element(By.CSS_SELECTOR, "div.cf-price.cf-rr-pull-right.cf-disable-tooltip")
preco = preco_elemento.text.strip()

with open("preco_notebook1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Preço do Notebook Gamer G15: {preco}\n")

print(f"Preço do Notebook Gamer G15: {preco} foi salvo em 'preco_notebook.txt'.")

navegador.quit()