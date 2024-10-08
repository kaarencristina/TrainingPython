# entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pi install pyautogui

import pyautogui
import time

pyautogui.PAUSE=0.8 #pausa para cada comando

#abrindo navegadorCAHA000252    1dsad
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")


#acessar site empresa

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#dar uma pausa de 3seg, pois depende da velocidade da internet etc
time.sleep(4)

# fazer login

pyautogui.click(x=688, y=468)
pyautogui.write("blablabla@gmail.com")
pyautogui.click(x=702, y=600) #ou usar a tecla tab
pyautogui.write("password")

#login-button

pyautogui.click(x=944, y=658)

time.sleep(2)



# importar a base de dados (instalar o pandas, pip install pandas)
import pandas

import pandas as pd
import pyexcel_ods

# Lendo o arquivo 
table = pandas.read_csv("produtos.csv")

print(table)

time.sleep(3)
#para cada linha da tabela
linha=0
for linha in table.index:
    
    # cadastrar produtos
    pyautogui.click(x=743, y=317)
    time.sleep(0.5) 

    #cod
    cod=table.loc[linha,"codigo"]
    pyautogui.write(str(cod))
    pyautogui.press("tab")


    #marca

    marca=table.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo=table.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria=table.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #precoun
    precoun=table.loc[linha,"preco_unitario"]
    pyautogui.write(str(precoun))
    pyautogui.press("tab")

    #custo
    custo=table.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs=table.loc[linha,"obs"]
    if not pandas.isna(obs):  #verificar se esta vazio
        pyautogui.write(str(obs))
    pyautogui.press("tab")
   

    #clicar no enviar
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(4000)
    