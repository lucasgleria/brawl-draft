# api/brawl_stars_api.py
import requests
from models.character import Character

class BrawlStarsAPI:
    BASE_URL = "https://api.brawlstars.com/v1"
    API_TOKEN = "SEU_TOKEN_AQUI"  # Insira o token da API aqui

    def __init__(self):
        """
        Inicializa o cliente da API Brawl Stars com o cabeçalho de autenticação.
        """
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}"
        }

    def get_character_image(self, name):
        """
        Busca os detalhes do personagem e sua imagem pela API do Brawl Stars.
        :param name: Nome do personagem inserido pelo usuário.
        :return: Instância de Character com o nome e URL da imagem.
        """
        endpoint = f"{self.BASE_URL}/brawlers"
        response = requests.get(endpoint, headers=self.headers)

        if response.status_code == 200:
            brawlers = response.json().get("items", [])
            # Procura o personagem pelo nome na lista de brawlers
            for brawler in brawlers:
                if brawler["name"].lower() == name.lower():
                    # Cria uma instância de Character com o nome e a URL da imagem
                    return Character(brawler["name"], brawler["imageUrl2"])
            # Se o personagem não for encontrado, pode-se retornar uma imagem padrão ou erro
            raise ValueError(f"Personagem '{name}' não encontrado.")
        else:
            # Trata erros de conexão ou resposta não 200
            raise ConnectionError(f"Erro ao acessar a API do Brawl Stars: {response.status_code}")

