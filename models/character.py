# models/character.py

class Character:
    def __init__(self, name, image_url):
        """
        Inicializa um personagem com nome e URL da imagem.
        :param name: Nome do personagem
        :param image_url: URL da imagem do personagem
        """
        self.name = name
        self.image_url = image_url

    def get_name(self):
        """
        Retorna o nome do personagem.
        :return: Nome do personagem
        """
        return self.name

    def get_image_url(self):
        """
        Retorna a URL da imagem do personagem.
        :return: URL da imagem do personagem
        """
        return self.image_url
