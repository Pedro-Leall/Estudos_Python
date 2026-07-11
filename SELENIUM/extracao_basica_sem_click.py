# Programa para extrair informações de um site e retornar um valor, transformando a entrada e a saída
from selenium import webdriver #importar o "controlador" do browser
from selenium.webdriver.common.by import By
import time

pokemon = input("Diga o nome de um pokemon que eu lhe retorno qual é seu número de pokedex: ")
'''
Problema envolvendo a entrada de dados, o site funciona apenas com o nome do pokemon em minusculo.
'''
pokemon = pokemon.lower() # .lower() é uma função que tranforma tudo em minusculo, .upper() tranforma em maiusculo
opcoes = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opcoes) #cria nossa janela do driver 

driver.maximize_window()
driver.get(f"https://pokemondb.net/pokedex/{pokemon}") #abrir uma pagina em especial na internet

time.sleep(5)

numero_dex = driver.find_element(By.XPATH, '//*[starts-with(@id, "tab-basic-")]/div[1]/div[2]/table/tbody/tr[1]/td/strong').text
'''
Problema encontrado durante o aprendizado, este XPATH, tem um id que muda conforme o número de pokedex, que é o elemento que desejo capturar.

codigo antes de consultar a IA: 
numero_dex = driver.find_element(By.XPATH, '//*[@id="tab-basic-137"]/div[1]/div[2]/table/tbody/tr[1]/td/strong').text

Como foi proposto pela IA (GEMINI) contornar este poblema:

1. O método "Começa com" (starts-with)
Essa é a função nativa do XPath para procurar algo pelo início da palavra. É a opção mais segura para o seu caso.

A estrutura básica é: //elemento[starts-with(@atributo, "texto_inicial")]

Como fica no seu código:

Python
xpath_dinamico = '//*[starts-with(@id, "tab-basic-")]/div[1]/div[2]/table/tbody/tr[1]/td/strong'

numero_dex = driver.find_element(By.XPATH, xpath_dinamico).text
O que o Selenium lê aqui: "Busque em qualquer lugar da página (//) qualquer elemento (*) que a condição seja ([...]) ter o ID começando com a palavra (starts-with(@id, "tab-basic-")). Depois de achar isso, desça até o strong."
'''

driver.quit()

numero_dex = int(numero_dex) #isso serve para transformar o número vindo via selenium para um inteiro, já que o número vinha com 0 à esquerda
print(f"O pokemon {pokemon} é o {numero_dex}° da pokedex")
