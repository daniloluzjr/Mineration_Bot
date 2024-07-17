import pyautogui
import time
import threading
import tkinter as tk
import random

# Variável global para controlar o estado do bot
bot_running = False

def press_key(key):
    pyautogui.press(key)

def bot_thread(window_name, start_button, countdown_label, action_time, wait_time):
    global bot_running
    while bot_running:
        # Ativa a janela do jogo pelo nome
        windows = pyautogui.getWindowsWithTitle(window_name)
        if windows:
            windows[0].activate()

        start_time = time.time()
        while time.time() - start_time < action_time:
            if not bot_running:
                break
            press_key('f')
            time.sleep(random.uniform(1, 3))
        
        if bot_running:
            for remaining in range(wait_time, 0, -1):
                if not bot_running:
                    break
                mins, secs = divmod(remaining, 60)
                countdown_label.config(text=f"Restarting in: {mins:02d}:{secs:02d}")
                time.sleep(1)

    # Reativar o botão "Start Bot" quando o bot parar
    start_button.config(state=tk.NORMAL)
    countdown_label.config(text="Bot stopped")

def start_bot(window_name, start_button, countdown_label, action_time_entry, wait_time_entry):
    global bot_running
    if not bot_running:
        bot_running = True
        start_button.config(state=tk.DISABLED)
        countdown_label.config(text="Bot running")

        try:
            action_time = int(action_time_entry.get()) * 60  # Converte minutos para segundos
            wait_time = int(wait_time_entry.get()) * 60      # Converte minutos para segundos
        except ValueError:
            countdown_label.config(text="Invalid input")
            bot_running = False
            start_button.config(state=tk.NORMAL)
            return

        threading.Thread(target=bot_thread, args=(window_name, start_button, countdown_label, action_time, wait_time)).start()

def stop_bot(start_button, countdown_label):
    global bot_running
    bot_running = False
    # Reativar o botão "Start Bot" imediatamente após parar o bot
    start_button.config(state=tk.NORMAL)
    countdown_label.config(text="Bot stopped")

# Configuração da interface gráfica
def create_gui():
    root = tk.Tk()
    root.title("Bot - LUZ")
    
    # Desativa a opção de maximizar a janela
    root.resizable(False, False)

    # Definir margens
    padding_x = 20
    padding_y = 10

    frame = tk.Frame(root, padx=padding_x, pady=padding_y)
    frame.pack()

    tk.Label(frame, text="Game window name:").pack(pady=5)
    window_name_entry = tk.Entry(frame)
    window_name_entry.pack(padx=10, pady=5)  # Adiciona margens horizontais e verticais

    tk.Label(frame, text="Determine tempo de ação (min):").pack(pady=5)
    action_time_entry = tk.Entry(frame)
    action_time_entry.pack(padx=10, pady=5)

    tk.Label(frame, text="Determine o tempo parado (min):").pack(pady=5)
    wait_time_entry = tk.Entry(frame)
    wait_time_entry.pack(padx=10, pady=5)

    button_width = 12  # Define uma largura fixa para os botões

    start_button = tk.Button(frame, text="Start Bot", width=button_width, command=lambda: start_bot(window_name_entry.get(), start_button, countdown_label, action_time_entry, wait_time_entry))
    start_button.pack(pady=5)

    stop_button = tk.Button(frame, text="Stop Bot", width=button_width, command=lambda: stop_bot(start_button, countdown_label))
    stop_button.pack(pady=5)

    countdown_label = tk.Label(frame, text="Bot stopped")
    countdown_label.pack(pady=5)

    # Adiciona o @ do Instagram estilizado
    instagram_label = tk.Label(frame, text="@professor_luz", fg="lightgray", font=("Arial", 10, "italic"))
    instagram_label.pack(side=tk.RIGHT, padx=10, pady=10)

    # Manter a janela sempre à frente
    root.attributes("-topmost", True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


#@professor_luz
