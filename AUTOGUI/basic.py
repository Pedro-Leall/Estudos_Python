#Bloco simples para saber o tamanho da tela
import pyautogui 
# Verificar tamanho da tela 
largura, altura = pyautogui.size() 
print(f'Resolução: {largura}x{altura}')


# abre um app que mostra as coordenadas do mouse = pyautogui.mouseInfo()

'''
Esse trecho abaixo não comentado se trata de uma automação bobo, aonde eu tenho uma Resolução: 1920x1200 e atrás do VScode estava aberto uma aba com o gemini aberto.
'''
pyautogui.moveTo(1786, 33)
pyautogui.click()

pyautogui.moveTo(999, 1068)
pyautogui.click()

pyautogui.write("esse é um prompt mandado pelo autogui")
pyautogui.press("enter")

'''
isso ajuda a enteder a possição atual do mouse
x, y = pyautogui.position()
print(f"Posição atual do mouse: X={x}, Y={y}")

# O autogui usa coordenadas, como se fosse latitude e longetude/x e y 
pyautogui.moveTo(1786, 33)   
# Move o mouse para as coordenadas 
pyautogui.click()   
# Clica na posição atual 
pyautogui.click(200, 300)   
# Move e clica 
pyautogui.doubleClick(200, 300)  
# Clique duplo 
pyautogui.rightClick(200, 300)   
# Clique com botão direito 
pyautogui.scroll(10)   
# Rola a tela para cima 
pyautogui.drag(100, 0, duration=1)  
# Arrasta o mouse 100px para a direita

'''

