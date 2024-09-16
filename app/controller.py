# app/controller.py

from models.brawlers import BRAWLER_IDS  # Importa os dados dos Brawlers
from models.maps import MAP_DATA  # Importa os dados dos Mapas

class Controller:
    def __init__(self, input_window, display_window, api_client):
        self.input_window = input_window
        self.display_window = display_window
        self.api_client = api_client
        self.input_window.set_controller(self)

    def process_input(self, team, input_id, name):
        """
        Processa o input de um nome inserido pelo usuário, baseado em seu ID único.
        :param team: Time azul ou vermelho
        :param input_id: ID único do input
        :param name: Nome do personagem inserido no input
        """
        name = name.lower()  # Converter o nome para minúsculas
        if name in BRAWLER_IDS:
            brawler_id = BRAWLER_IDS[name]
            # Obtém o objeto Character
            character = self.api_client.get_character_image(brawler_id)
            # Passa a URL da imagem para o display, com base no ID do input
            self.display_window.update_image(team, input_id, character.get_image_url())
        else:
            raise ValueError(f"Personagem '{name}' não encontrado.")

    def process_map_input(self, map_name):
        """
        Processa o nome do mapa inserido pelo usuário.
        Utiliza a estrutura JSON para buscar as informações corretas sobre o mapa e o modo de jogo.
        :param map_name: Nome do mapa inserido
        """
        map_name = map_name.lower()  # Converter para minúsculas
        if map_name in MAP_DATA:
            map_info = MAP_DATA[map_name]
            map_image_url = map_info["map_image_url"]
            game_mode_name = map_info["game_mode"]["name"]
            game_mode_image_url = map_info["game_mode"]["image_url"]
            game_mode_banner_url = map_info["enviroment"]["banner_url"]

            # Atualiza a exibição com o nome do mapa, a imagem do mapa, o nome do modo de jogo, e a imagem do modo de jogo
            self.display_window.update_map(map_name, map_image_url, game_mode_name, game_mode_image_url, game_mode_banner_url)
        else:
            raise ValueError(f"Mapa '{map_name}' não encontrado.")