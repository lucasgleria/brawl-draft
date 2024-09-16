# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times
        e o mapa com o modo de jogo no centro da tela.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens, Mapa e Modo de Jogo - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Frame central para o mapa e modo de jogo
        self.map_mode_frame = tk.Frame(self.root)
        self.map_mode_frame.pack(side=tk.TOP, pady=20)

        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.TOP, pady=20)

        # Referências para as imagens
        self.blue_team_images = {}
        self.red_team_images = {}
        self.map_label = None
        self.map_name_label = None
        self.game_mode_label = None
        self.game_mode_image_label = None
        self.game_mode_banner_label = None

    def update_image(self, team, input_id, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        Cada input é tratado de forma independente com base no seu ID único.
        :param team: Time azul ou vermelho
        :param input_id: ID único do input
        :param image_url: URL da imagem do personagem
        """
        image = self.download_image(image_url)
        img_tk = ImageTk.PhotoImage(image)

        if team == 'blue':
            if input_id not in self.blue_team_images:
                label = tk.Label(self.team_blue_frame, image=img_tk)
                label.image = img_tk
                label.pack()
                self.blue_team_images[input_id] = label
        elif team == 'red':
            if input_id not in self.red_team_images:
                label = tk.Label(self.team_red_frame, image=img_tk)
                label.image = img_tk
                label.pack()
                self.red_team_images[input_id] = label

    def update_map(self, map_name, map_image_url, game_mode_name, game_mode_image_url, game_mode_banner_url):
        """
        Atualiza a janela com a imagem do mapa, o nome do mapa, o nome do modo de jogo e a imagem do modo de jogo.
        :param map_name: Nome do mapa
        :param map_image_url: URL da imagem do mapa
        :param game_mode_name: Nome do modo de jogo associado ao mapa
        :param game_mode_image_url: URL da imagem do modo de jogo associado ao mapa
        :param game_mode_banner_url: URL da imagem do banner do modo de jogo
        """
        # Limpa o conteúdo do frame central
        for widget in self.map_mode_frame.winfo_children():
            widget.destroy()

        # Cria um Canvas para o game_mode_banner e game_mode_image
        self.map_mode_canvas = tk.Canvas(self.map_mode_frame, width=700, height=200)  # Ajuste o tamanho conforme necessário
        self.map_mode_canvas.pack()

        # Atualiza a imagem do banner do modo de jogo
        game_mode_banner = self.download_image(game_mode_banner_url)
        if game_mode_banner:
            game_mode_banner_img_tk = ImageTk.PhotoImage(game_mode_banner)
            self.map_mode_canvas.create_image(0, 0, anchor=tk.NW, image=game_mode_banner_img_tk)
            self.map_mode_canvas.image_banner = game_mode_banner_img_tk  # Manter uma referência

        # Atualiza a imagem do modo de jogo
        game_mode_image = self.download_image(game_mode_image_url)
        if game_mode_image:
            game_mode_img_tk = ImageTk.PhotoImage(game_mode_image)
            # Posiciona a imagem do modo de jogo sobre o banner, no canto superior esquerdo
            self.map_mode_canvas.create_image(0, 0, anchor=tk.NW, image=game_mode_img_tk)
            self.map_mode_canvas.image_mode = game_mode_img_tk  # Manter uma referência

        # Adiciona o nome do mapa sobre o banner, ao lado direito da imagem do modo de jogo
        if map_name:
            self.map_mode_canvas.create_text(250, 50, anchor=tk.NW, text=map_name, font=("Helvetica", 50), fill="white", tags="map_name")

        # Atualiza a imagem do mapa
        if self.map_label is not None:
            self.map_label.destroy()
        map_image = self.download_image(map_image_url)
        if map_image:
            map_img_tk = ImageTk.PhotoImage(map_image)
            self.map_label = tk.Label(self.map_frame, image=map_img_tk)
            self.map_label.image = map_img_tk
            self.map_label.pack()


    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            return Image.open(image_data)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            return Image.new("RGB", (150, 150), color=(255, 0, 0))
