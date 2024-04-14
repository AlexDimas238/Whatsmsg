import pywhatkit
import pyautogui
import time

def abrir_conversa(numero_telefone):

        # Abrir a conversa no WhatsApp usando o PyWhatKit
        pywhatkit.sendwhatmsg_instantly(numero_telefone, mensagem,)

        # Esperar um momento após maximizar a janela
        time.sleep(2)

        # Encontrar a janela do WhatsApp
        whatsapp_window = pyautogui.getWindowsWithTitle("WhatsApp")[0]

        # Maximizar a janela do WhatsApp
        whatsapp_window.maximize()

        # Esperar um momento após maximizar a janela
        time.sleep(1)

        # Pressiona Enter para enviar a mensagem
        #pyautogui.press('enter')

        for i in range(1, 100):
            # Construir a segunda mensagem com a contagem
            mensagem_com_contagem = f"{mensagem2} {i}"

            # Digitar a mensagem com a contagem
            pyautogui.write(mensagem_com_contagem)

            # Pressiona Enter para enviar a mensagem
            pyautogui.press('enter')

            # Esperar um momento entre cada mensagem
            time.sleep(1)

        print("Mensagem enviada com sucesso!")

# Número de telefone para enviar a mensagem (no formato internacional)
numero_telefone = "xxxxxx"

# Mensagem a ser enviada
mensagem = "Mensagem 1 "
mensagem2 = "Mensagem que fica no loop"

abrir_conversa(numero_telefone)



