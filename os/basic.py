import os
import pyautogui
import time
# Exemplo: abrindo o Bloco de Notas
user = os.getlogin() #captura o login do user e guarda em uma váriavel 

print(f"olá {user}") 
input("assim que estiver pronto pode pressionar o ENTER L> ")
os.startfile("opera.exe")
time.sleep(3)
pyautogui.write("Corinthians")
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(1889, 25)
'''
Essa pequena aplicação eu visei estudar uma fusão entre bibliotecas, para criar uma automação de simples clicks, coisa que também é possivel com selenium (e até mais recomendado fazer)
Minha lógica foi:
Abrir o browser com recursos do os, simulando o start opera.exe;
usar a biblioteca time para fazer um sleep no código e mandar ele para "dormir, dar um tempo para carregar a página
Como ao abrir o cursor já está diretamente apontado a barra de pesquisa apenas escrevi com autogui;
'''
#os.system('cls') para limpar o terminal
 
