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

pesquisa2 = navegador.find_element(By.ID, "mh-search-input")
pesquisa2.send_keys("Notebook Inspiron 15")
pesquisa2.send_keys(Keys.RETURN)

sleep(2)

resultado = navegador.find_element(By.ID, "i3520wadl1012w")
resultado.click()

sleep(2)

preco_elemento = navegador.find_element(By.CSS_SELECTOR, ".font-weight-bold.mb-1.text-nowrap.sale-price")
preco = preco_elemento.text.strip()

with open("preco_notebook2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Preço do Notebook Inspiron 15: {preco}\n")

print(f"Preço do Notebook Inspiron 15: {preco} foi salvo em 'preco_notebook.txt'.")

navegador.quit()