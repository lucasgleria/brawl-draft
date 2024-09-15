# app/controller.py

class Controller:
    def __init__(self, input_window, display_window, api_client):
        """
        Inicializa o controlador, conectando a janela de inputs e a janela de exibição.
        :param input_window: Instância da janela de input (InputWindow)
        :param display_window: Instância da janela de exibição de imagens (DisplayWindow)
        :param api_client: Cliente da API para buscar as imagens dos personagens
        """
        self.input_window = input_window
        self.display_window = display_window
        self.api_client = api_client

        # Conectar eventos da janela de input ao controlador
        self.input_window.set_controller(self)

    def process_input(self, team, name):
        """
        Processa o input de um nome inserido pelo usuário.
        :param team: Time azul ou vermelho
        :param name: Nome do personagem inserido no input
        """
        # Busca a imagem do personagem usando a API
        image_url = self.api_client.get_character_image(name)

        # Atualiza a janela de exibição com a imagem retornada pela API
        self.display_window.update_image(team, image_url)