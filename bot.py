import pyautogui
import time
import threading
import tkinter as tk
import random

# Variável global para controlar o estado do bot
bot_running = False

def press_key(key):
    pyautogui.press(key)

def bot_thread(window_name, start_button, countdown_label):
    global bot_running
    while bot_running:
        # Ativa a janela do jogo pelo nome
        windows = pyautogui.getWindowsWithTitle(window_name)
        if windows:
            windows[0].activate()

        start_time = time.time()
        while time.time() - start_time < 60:
            if not bot_running:
                break
            press_key('f')
            time.sleep(random.uniform(3, 7))
        
        if bot_running:
            for remaining in range(10 * 60, 0, -1):  # Ajustado para 10 minutos
                if not bot_running:
                    break
                mins, secs = divmod(remaining, 60)
                countdown_label.config(text=f"Reiniciando em: {mins:02d}:{secs:02d}")
                time.sleep(1)

    # Reativar o botão "Iniciar Bot" quando o bot parar
    start_button.config(state=tk.NORMAL)
    countdown_label.config(text="Bot parado")

def start_bot(window_name, start_button, countdown_label):
    global bot_running
    if not bot_running:
        bot_running = True
        start_button.config(state=tk.DISABLED)
        countdown_label.config(text="Bot em execução")
        threading.Thread(target=bot_thread, args=(window_name, start_button, countdown_label)).start()

def stop_bot(start_button, countdown_label):
    global bot_running
    bot_running = False
    # Reativar o botão "Iniciar Bot" imediatamente após parar o bot
    start_button.config(state=tk.NORMAL)
    countdown_label.config(text="Bot parado")

# Configuração da interface gráfica
def create_gui():
    root = tk.Tk()
    root.title("Ravendawn Bot")

    tk.Label(root, text="Nome da janela do jogo:").pack(pady=5)
    window_name_entry = tk.Entry(root)
    window_name_entry.pack(pady=5)

    start_button = tk.Button(root, text="Iniciar Bot", command=lambda: start_bot(window_name_entry.get(), start_button, countdown_label))
    start_button.pack(pady=5)

    stop_button = tk.Button(root, text="Parar Bot", command=lambda: stop_bot(start_button, countdown_label))
    stop_button.pack(pady=5)

    countdown_label = tk.Label(root, text="Bot parado")
    countdown_label.pack(pady=5)

    # Manter a janela sempre à frente
    root.attributes("-topmost", True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


# Criado por Danilo Luz Jr @professor_luz
# abra no VS e execute: python bot.py (no terminal)
# preencha o nome da sua janela (exemplo: Ravendal - NickName)
# click Iniciar para o bot iniciar a mineração
