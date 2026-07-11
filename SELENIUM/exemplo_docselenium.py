from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
from deep_translator import GoogleTranslator
from selenium.common.exceptions import NoSuchElementException # <-- Importação Nova!

pokemon_name = input("Digite o nome de um Pokémon: ").capitalize()
search = '//*[@id="filter-pkmn-name"]'
ahref = f'//*[@id="pokedex"]//a[text()="{pokemon_name}"]' 
intro_xpath = '//*[@id="main"]/p'

opcoes = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opcoes)

driver.get("https://pokemondb.net/pokedex/all")

# A pesquisa inicial é segura, então deixamos fora
elem = driver.find_element(By.XPATH, search)
elem.clear() 
elem.send_keys(pokemon_name)
time.sleep(0.5) 

# === AQUI COMEÇA A PROTEÇÃO ===
try:
    print(f"Procurando por {pokemon_name} na tabela...")
    
    # Se o Pokémon não existir, esta linha abaixo vai dar erro.
    # O Python vai abortar o "try" IMEDIATAMENTE e pular direto pro "except".
    elem = driver.find_element(By.XPATH, ahref)
    elem.click()

    # Se chegou aqui, é porque achou! Pega o texto e traduz.
    intro_ingles = driver.find_element(By.XPATH, intro_xpath).text
    intro_pt = GoogleTranslator(source='auto', target='pt').translate(intro_ingles)
    
    print(f"\n--- INTRODUÇÃO: {pokemon_name} ---")
    print(intro_pt)

except NoSuchElementException:
    # Este bloco SÓ é executado se o erro acontecer lá em cima.
    print(f"\n❌ ERRO: O Pokémon '{pokemon_name}' não foi encontrado no site.")
    print("Verifique se você digitou o nome corretamente (não use nomes de Digimon!).")
    
# O driver.quit() vai rodar de qualquer jeito no final, fechando o navegador com segurança.
driver.quit()