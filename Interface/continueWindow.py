import tkinter as tk
import os
def continue_message(error):
    
    # Criar a janela principal para iniciar o Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    # Criar a janela de erro
    window = tk.Toplevel()
    window.title("Mensagem de sucesso!")
    window.geometry("400x250")
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'check.ico')
    window.iconbitmap(icon_path)  # Define o ícone (.ico)
    window.configure(bg="#C8E6C9")  # Cor de fundo vermelha clara
    window.resizable(False, False)

    # Centralizar a janela corretamente
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 400
    window_height = 250
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Frame para organizar layout
    frame = tk.Frame(window, bg="#C8E6C9", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Label para exibir a mensagem de erro
    continue_label = tk.Label(frame, text=error, font=("Arial", 12, "bold"), fg="black", bg="#C8E6C9",
                           wraplength=360, justify="center")  # Quebra de linha automática
    continue_label.pack(pady=10)

    # Botão de fechar e encerrar o Tkinter
    def close_and_exit():
        window.quit()
        window.destroy()
        root.quit()
        root.destroy()

    ok_button = tk.Button(frame, text="OK", font=("Arial", 12, "bold"), fg="white",
                             bg="#81C784", relief="flat", padx=10, pady=5, command=close_and_exit)
    ok_button.pack(pady=10)

    # Bloqueia interação com outras janelas até que a mensagem seja fechada
    window.transient()
    window.grab_set()
    window.wait_window()



