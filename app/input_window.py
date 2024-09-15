# app/input_window.py
import tkinter as tk

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul e 3 para o time vermelho).
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens - Brawl Stars")

        self.team_blue_inputs = []
        self.team_red_inputs = []

        # Inicializando os campos de texto
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_entry.bind("<Return>", lambda event, team='blue', idx=i: self.on_input(team, input_entry.get()))
            input_entry.pack()
            self.team_blue_inputs.append(input_entry)

        for i in range(3):
            label = tk.Label(self.root, text=f"Time Vermelho - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_entry.bind("<Return>", lambda event, team='red', idx=i: self.on_input(team, input_entry.get()))
            input_entry.pack()
            self.team_red_inputs.append(input_entry)

        self.controller = None

    def set_controller(self, controller):
        """
        Define o controlador que processará os eventos de input.
        :param controller: Instância do Controller que processa os inputs
        """
        self.controller = controller

    def on_input(self, team, name):
        """
        Chama o controlador para processar o input do usuário quando ele pressiona Enter.
        :param team: Time azul ou vermelho
        :param name: Nome do personagem inserido no input
        """
        if self.controller:
            self.controller.process_input(team, name)

    def run(self):
        """
        Executa o loop principal da janela de inputs.
        """
        self.root.mainloop()