# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens - Brawl Stars")

        # Inicializa containers para as imagens dos dois times
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        self.blue_team_images = []
        self.red_team_images = []

    def update_image(self, team, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        :param team: Time azul ou vermelho
        :param image_url: URL da imagem do personagem
        """
        # Faz o download da imagem a partir do URL (você precisa implementar o download)
        # Abre a imagem e a exibe no respectivo frame
        image = self.download_image(image_url)  # Função para baixar a imagem
        img_tk = ImageTk.PhotoImage(image)

        if team == 'blue':
            label = tk.Label(self.team_blue_frame, image=img_tk)
            label.image = img_tk  # Mantém a referência para não ser coletada pelo GC
            label.pack()
            self.blue_team_images.append(label)
        elif team == 'red':
            label = tk.Label(self.team_red_frame, image=img_tk)
            label.image = img_tk
            label.pack()
            self.red_team_images.append(label)

    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        # Implementar a lógica de download de imagem (usando requests ou outra lib)
        pass