import pyautogui
import pyperclip
import webbrowser
import yfinance
import time

ticker = input("Digite o código da ação: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")

fechamento = dados.Close

maxima = round(fechamento.max(),2)
minimo = round(fechamento.min(), 2)
preco_medio = round(fechamento.mean(), 2)

destinatario = "pimpao775@gmail.com"
assunto = f"Dados do Relatório da Ação {ticker}"

mensagem = f"""Rafael 
Seguem as análises solicitadas da ação {ticker}:

Cotação Máxima: R$ {maxima}
Cotação Mínima: R$ {minimo}
Preço Médio: R$ {preco_medio}
Atenciosamente"""

# abrir o navegador e ir para o Gmail

webbrowser.open("www.gmail.com")
time.sleep(10)

# configurando uma pausa para carregar os itens
pyautogui.PAUSE = 5 

# clicar no botão escrever

pyautogui.click(x=98, y=219)

# digitar o e-mail o destinatário e clicar TAB

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar o assunto do e-mail e clicar tab

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")              

# digitar a mensagem do e-mail 

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

#clicar no botão enviar 

pyautogui.click(x=215, y=978)

# fechando o Gmail

pyautogui.click(x=732, y=18)

print("E-mail Enviado com Sucesso")

