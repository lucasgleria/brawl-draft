# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul, 3 para o time vermelho)
        e um campo para o mapa do jogo.
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens e Mapa - Brawl Stars")

        self.inputs = []  # Lista que armazenará todos os inputs, com seus IDs

        # Inicializando os campos de texto para o time azul
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"blue_{i+1}"  # ID único para cada input do time azul
            input_entry.bind("<Return>", lambda event, team='blue', input_id=input_id, entry=input_entry: self.on_input(team, input_id, entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'blue', 'id': input_id, 'entry': input_entry})

        # Inicializando os campos de texto para o time vermelho
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Vermelho - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"red_{i+1}"  # ID único para cada input do time vermelho
            input_entry.bind("<Return>", lambda event, team='red', input_id=input_id, entry=input_entry: self.on_input(team, input_id, entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'red', 'id': input_id, 'entry': input_entry})

        # Inicializando o campo de texto para o Mapa
        label = tk.Label(self.root, text="Nome do Mapa")
        label.pack()
        self.map_entry = tk.Entry(self.root)
        self.map_entry.bind("<Return>", lambda event: self.on_map_input(self.map_entry.get()))
        self.map_entry.pack()

        self.controller = None

    def set_controller(self, controller):
        """
        Define o controlador que processará os eventos de input.
        :param controller: Instância do Controller que processa os inputs
        """
        self.controller = controller

    def on_input(self, team, input_id, name):
        """
        Chama o controlador para processar o input do usuário quando ele pressiona Enter.
        Cada input é identificado por um ID único e processado de forma independente.
        :param team: Time azul ou vermelho
        :param input_id: ID único do input
        :param name: Nome do personagem inserido no input
        """
        name = name.strip().lower()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", f"O nome do personagem no input {input_id} não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, input_id, name)  # Passa o input ID para o controlador
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def on_map_input(self, map_name):
        """
        Chama o controlador para processar o nome do mapa quando pressionar Enter.
        :param map_name: Nome do mapa inserido pelo usuário
        """
        map_name = map_name.strip().lower()  # Remove espaços em branco antes e depois do nome
        if not map_name:
            messagebox.showerror("Erro", "O nome do mapa não pode estar vazio!")
            return

        try:
            self.controller.process_map_input(map_name)  # Processa o input do mapa
        except ValueError as e:
            # Mostra uma mensagem de erro caso o mapa não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
