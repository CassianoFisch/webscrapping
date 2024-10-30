from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# Se estiver usando o Pycharm para desenvolver,
# Adicione estas linhas.
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options=opts)
url = r'C:\Users\08087\Documents\webscrap\contato.html'
navegador.get(url)
campo_nome = navegador.find_element(By.ID, "nome")
campo_nome.send_keys("Xbox Player")
sleep(3)
campo_mensagem = navegador.find_element(By.ID, "mensagem")
campo_mensagem.send_keys("Existir cabo sem fio pra xbox 360?")
sleep(2)

botao = navegador.find_element(By.XPATH, "/html/body/div/div/form/button")
botao.click()


# titulo = navegador.find_element(By.ID, "titulo2")
#precos = navegador.find_elements(By.CLASS_NAME, "price")
#for preco in precos:
#    print(preco.text)
#produtos = navegador.find_elements(By.CLASS_NAME, 'product_name')

#for p in produtos:
#    print(p.text)

# print(navegador.title) # pega uma informação do site