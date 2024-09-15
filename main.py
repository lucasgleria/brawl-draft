# main.py
from app.controller import Controller
from app.input_window import InputWindow
from app.display_window import DisplayWindow
from api.brawl_stars_api import BrawlStarsAPI  # Simulando que a classe já foi implementada

def main():
    """
    Função principal do programa que inicializa as janelas e o controlador.
    """
    # Inicializa a janela de inputs e a janela de exibição
    input_window = InputWindow()
    display_window = DisplayWindow()

    # Inicializa o cliente da API para buscar as imagens dos personagens
    api_client = BrawlStarsAPI()

    # Inicializa o controlador que liga o input com a exibição
    controller = Controller(input_window, display_window, api_client)

    # Executa a janela de inputs (e consequentemente a aplicação)
    input_window.run()

if __name__ == '__main__':
    main()
