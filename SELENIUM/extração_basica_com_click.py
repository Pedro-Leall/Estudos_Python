from selenium import webdriver #controlar o browser
from selenium.webdriver.common.by import By #passar parametros de buscar para o find
from selenium.webdriver.common.keys import Keys
import time

from deep_translator import GoogleTranslator

from selenium.common.exceptions import NoSuchElementException # isso serve para fazer o tratamento de erro, quando o pokemon digitado não existir ou não estiver no banco de emojis

'''
Entrar no site e via search achar algo, tendo pelo menos 1 click
'''

search = '//*[@id="filter-pkmn-name"]'
intro = '//*[@id="main"]/p'

pokemon_name = input("Digite um pokemon que lhe devolvo uma introdução dele: ").title() #Para formatarmos a entrada para uma formatação esperada, ex: LUCARIO para Lucario podemos usar '.capitalize()' Para palavras únicas ou '.title()' para palavras compostas como Mr. Mine
ahref = f'//*[@id="pokedex"]//a[text()="{pokemon_name}"]'  # //*[contains indica que contem, neste caso refere a tr, pois cada pokemon tem a sua table row

opcoes = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opcoes)

driver.get("https://pokemondb.net/pokedex/all")

try:
    elem = driver.find_element(By.XPATH, search)

    elem.clear() #limpar a caixa de texto por precaução
    elem.send_keys(pokemon_name)
    time.sleep(0.3)

    elem = driver.find_element(By.XPATH, ahref)
    elem.click()

    intro = driver.find_element(By.XPATH, intro).text

    intro = GoogleTranslator(source='auto', target='pt').translate(intro)

    #parte 2
    '''
    Explicação deste TRY:

    Para mitigar o possivel erro ao buscar um pokemon que não tenha um emojis usamos 'NoSuchElementException'.

    NoSuchElementException: ocorre quando o Selenium tenta interagir com um elemento que não existe ou ainda não carregou na página.
    '''
    try:
        driver.get(f"https://emojicombos.com/{pokemon_name.lower()}-text-art")
        emoji = driver.find_element(By.XPATH, '//*[@id="comboListEl"]/div[1]/div/div[2]/div[1]/div').text
        driver.quit()
        print(intro)
        print(emoji)
    except NoSuchElementException:
        driver.quit()
        print(intro)

except NoSuchElementException:
    driver.quit()
    print("+","-" * 38,"+")
    print("|Pokemon não existe ou não foi encontrado|")
    print("+","-" * 38,"+")