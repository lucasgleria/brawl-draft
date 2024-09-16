# api/brawl_stars_api.py
import requests
from models.character import Character

class BrawlStarsAPI:
    BASE_URL = "https://api.brawlify.com/v1/brawlers" 

    def get_character_image(self, brawler_id):
        """
        Busca os detalhes do personagem e sua imagem pela BrawlAPI.
        :param brawler_id: ID do personagem inserido pelo usuário.
        :return: Instância de Character com o nome e URL da imagem.
        """
        # Faz a requisição para o endpoint específico do brawler
        endpoint = f"{self.BASE_URL}/{brawler_id}"
        response = requests.get(endpoint)

        if response.status_code == 200:
            brawler = response.json()
            # Pega o nome do personagem e a URL da imagem
            name = brawler.get("name")
            image_url = brawler.get("imageUrl2")  # Usa imageUrl2 para a versão sem bordas

            if name and image_url:
                return Character(name, image_url)
            else:
                # Caso a imagem não esteja disponível, retorna uma imagem padrão
                default_image_url = "https://via.placeholder.com/150"
                return Character(name or "Desconhecido", default_image_url)
        else:
            # Trata erros de conexão ou resposta não 200
            raise ConnectionError(f"Erro ao acessar a API BrawlAPI: {response.status_code}")
