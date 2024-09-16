Fui contratado para desenvolver um software inteligente e rápido, a linguagem escolhida para o desenvolvimento no projeto foi o python e seguiremos os princpios de design pattern SOLID.

O Projeto é o seguinte:
Preciso que haja 6 inputs, 3 inputs que serão destinados ao time azul, 3 inputs que serão destinados para o time vermelho.

Ao Escrever um nome específico e dar enter em cada um dos inputs, Uma imagem deve ser dinamicamente gerada, ao inserir o nome no input e dar enter, a imagem correspondente ao nome escrito deve aparecer na nossa janela principal dinamicamente, sendo atualizada a cada input.

Os 3 inputs do time azul farão aparecer 3 imagens no lado esquerdo da janela principal após serem atualizados

Os 3 inputs do time vermelho farão aparecer 3 imagens no lado direito da janela principal após serem atualizados

Para que isso seja possivel, além de utilizarmos o python e uma interface gráfica para que os inputs apareçam de forma familiar ao usuário, vamos utilizar a API do jogo BRAWL STARS. 

A Janela Principal que será gerada dinamicamente, não deve ser na mesma janela que os inputs ficarão, devem ser janelas distintas.

Por exemplo, ao iniciar o programa, uma primeira janela deve ser exibida com 6 inputs, como já descritos anteriormente, ao escrever o nome "Colt" no primeiro input e pressionar enter, uma nova janela será criada com a imagem do colt à esquerda como já indicado anteriormente, e ao adicionar os outros nomes aos inputs a Janela principal deve ir sendo atualizada da mesma forma.

---------


Este projeto parece ser bem interessante! Vamos começar por entender os principais requisitos e abordá-los passo a passo, utilizando os princípios SOLID e Python.

### 1. Requisitos Chave:
- **Linguagem de programação**: Python.
- **Interface gráfica**: Uma biblioteca gráfica como `Tkinter` ou `PyQt` pode ser usada para gerenciar as janelas e os inputs.
- **Entrada de dados**: 6 inputs no total, divididos entre dois times (azul e vermelho).
- **Geração dinâmica de imagens**: A API do Brawl Stars deve fornecer as imagens correspondentes aos personagens inseridos nos inputs.
- **Janela dinâmica**: As imagens devem ser exibidas em uma janela separada da dos inputs, atualizando conforme os inputs são inseridos.

### 2. Design Patterns (com base em SOLID):
Aqui estão alguns princípios SOLID que podemos aplicar ao projeto:
- **S**: **Single Responsibility Principle (SRP)** — Cada classe deve ter uma única responsabilidade. Teremos classes separadas para gerenciar os inputs, as janelas e a manipulação da API.
- **O**: **Open/Closed Principle (OCP)** — O software deve ser aberto para extensões, mas fechado para modificações. Por exemplo, se quisermos adicionar mais times no futuro, não devemos modificar muito código.
- **L**: **Liskov Substitution Principle (LSP)** — Devemos garantir que as subclasses possam substituir suas superclasses sem quebrar a funcionalidade. Isso pode não ser muito relevante se não formos trabalhar com hierarquias de classes complexas.
- **I**: **Interface Segregation Principle (ISP)** — Interface menor, mais específica. Podemos separar a funcionalidade em classes menores, como uma classe para manipular a API e outra para a interface gráfica.
- **D**: **Dependency Inversion Principle (DIP)** — Dependências devem ser abstrações e não classes concretas. Podemos definir interfaces para a API e para a janela de exibição das imagens, facilitando futuras mudanças.

### 3. Estrutura de Solução (em alto nível)
Vamos pensar em como organizar o código:

#### 1. **Classe de Interface Gráfica**:
Esta classe será responsável por exibir os inputs para os times e capturar os eventos quando o usuário pressiona "enter" nos inputs. Ela irá se comunicar com outra classe responsável por exibir a janela principal com as imagens.

#### 2. **Classe da Janela Principal**:
Será responsável por exibir e atualizar as imagens correspondentes aos personagens dos dois times em uma janela separada.

#### 3. **Classe para a API do Brawl Stars**:
Esta classe irá lidar com a comunicação com a API do Brawl Stars, buscando as imagens dos personagens com base nos nomes inseridos.

### 4. Exemplo de Pseudo Código:

```python
# Classe responsável pela janela de inputs
class InputWindow:
    def __init__(self):
        # Inicializa a janela de inputs com 6 campos de texto
        # 3 para o time azul e 3 para o time vermelho
        self.team_blue_inputs = []
        self.team_red_inputs = []
        # Referência para a janela de exibição
        self.display_window = DisplayWindow()

    def on_input(self, team, name):
        # Função chamada quando o usuário insere um nome e pressiona Enter
        # Atualiza a janela de exibição com a imagem do personagem
        image = BrawlStarsAPI.get_character_image(name)
        self.display_window.update_image(team, image)


# Classe responsável pela janela de exibição
class DisplayWindow:
    def __init__(self):
        # Inicializa a janela principal onde as imagens serão exibidas
        self.blue_team_images = []
        self.red_team_images = []

    def update_image(self, team, image):
        # Atualiza a imagem na janela de acordo com o time (azul ou vermelho)
        if team == 'blue':
            self.blue_team_images.append(image)
        elif team == 'red':
            self.red_team_images.append(image)
        # Atualiza a exibição da janela


# Classe responsável pela comunicação com a API do Brawl Stars
class BrawlStarsAPI:
    @staticmethod
    def get_character_image(name):
        # Comunica-se com a API e retorna a imagem do personagem
        # Vamos assumir que a API retorna uma URL da imagem
        pass
```

### 5. Próximos Passos:
- **Escolha da biblioteca gráfica**: A decisão de usar `Tkinter`, `PyQt` ou outra biblioteca para a interface é importante.
- **API do Brawl Stars**: Precisamos entender o funcionamento da API para buscar as imagens dos personagens. A API fornece uma URL ou imagem que pode ser carregada dinamicamente.
- **Estrutura das Janelas**: As janelas devem ser gerenciadas de forma eficiente, com inputs em uma janela e as imagens sendo exibidas em outra.

Como você pensa em começar? Quer discutir mais sobre a estrutura do código ou a implementação da interface gráfica?

-------

Voce parece ter entendido corretamente o nosso projeto, antes de darmos segmento na programação em si, me mostre como ficaria a estrutura de pastas e pacotes desse projeto para que possamos cumprir os principios SOLID. Leve em consideração que utilizaremos o TKinter

-----------

Ótima ideia! Antes de começar a programação, vamos organizar a estrutura de pastas e pacotes do projeto para garantir que seguimos os princípios SOLID e que o código ficará modular, organizado e de fácil manutenção. A escolha do `Tkinter` é perfeita para o tipo de interface gráfica que você descreveu.

### Estrutura de Pastas e Pacotes

Aqui está uma estrutura de pastas sugerida para o seu projeto, levando em conta a separação de responsabilidades e os princípios SOLID:

```
brawl_stars_app/
│
├── main.py                       # Ponto de entrada do projeto
├── README.md                     # Documentação do projeto
├── requirements.txt              # Dependências do projeto
│
├── app/                          # Pacote principal da aplicação
│   ├── __init__.py               # Inicializador do pacote principal
│   ├── input_window.py           # Classe responsável pela janela de inputs
│   ├── display_window.py         # Classe responsável pela janela de exibição de imagens
│   ├── controller.py             # Controlador que liga input e exibição de imagens
│
├── api/                          # Pacote responsável por comunicação com a API do Brawl Stars
│   ├── __init__.py               # Inicializador do pacote API
│   ├── brawl_stars_api.py        # Classe que lida com a API do Brawl Stars
│
├── models/                       # Pacote responsável por classes de dados e lógica de negócio
│   ├── __init__.py               # Inicializador do pacote models
│   ├── character.py              # Classe do modelo de personagem (ex: nome, imagem)
│
└── assets/                       # Pasta para armazenar arquivos estáticos (ex: imagens baixadas, etc.)
    └── images/                   # Pasta para armazenar as imagens dos personagens temporariamente
```

### Explicação da Estrutura:

1. **`main.py`**: O arquivo principal que serve como ponto de entrada da aplicação. Ele inicializa a interface e orquestra as janelas. 
   - **Responsabilidade única**: iniciar a aplicação e configurar as janelas iniciais.

2. **`app/`**: Este pacote contém toda a lógica da interface gráfica com o `Tkinter`, separando as responsabilidades em janelas distintas e o controlador que faz a comunicação entre as entradas e as exibições.
   - **`input_window.py`**: Contém a classe `InputWindow` que gerencia a janela de inputs.
   - **`display_window.py`**: Contém a classe `DisplayWindow` que gerencia a exibição das imagens.
   - **`controller.py`**: Classe `Controller`, responsável por orquestrar a comunicação entre o input e a atualização da janela de exibição (seguindo o princípio SRP).

3. **`api/`**: O pacote para lidar com a comunicação com a API do Brawl Stars.
   - **`brawl_stars_api.py`**: Implementa a classe `BrawlStarsAPI` para realizar as requisições e obter as informações sobre os personagens (incluindo a URL das imagens).

4. **`models/`**: Contém as classes que modelam os dados principais do projeto, como o `Character`.
   - **`character.py`**: Classe `Character` que encapsula as propriedades de um personagem, como nome e imagem, seguindo o princípio de responsabilidade única (SRP).

5. **`assets/`**: Esta pasta é responsável por armazenar qualquer conteúdo estático necessário, como imagens baixadas da API do Brawl Stars. Isso ajuda a manter o código separado de outros arquivos.
   - **`images/`**: Armazena temporariamente as imagens baixadas da API para exibição.

### Como os Princípios SOLID são aplicados:

1. **Single Responsibility Principle (SRP)**:
   - Cada arquivo e classe tem uma responsabilidade única. Por exemplo, `input_window.py` só lida com os inputs e não se preocupa com a exibição das imagens.

2. **Open/Closed Principle (OCP)**:
   - Se precisarmos adicionar novas funcionalidades, como um terceiro time, podemos fazer isso estendendo o controlador ou criando novas classes, sem modificar a lógica existente.

3. **Liskov Substitution Principle (LSP)**:
   - Todas as classes são projetadas para que possam ser substituídas sem afetar o comportamento do sistema. Por exemplo, o `DisplayWindow` pode ser substituído por outra classe que renderize de forma diferente, sem alterar o resto do código.

4. **Interface Segregation Principle (ISP)**:
   - O código é modular e separado em classes específicas com interfaces claras (como API, interface gráfica e lógica de controle).

5. **Dependency Inversion Principle (DIP)**:
   - O controlador (`Controller`) depende de abstrações e não de implementações concretas. Ele apenas interage com o que precisa (as janelas e a API), facilitando testes e manutenções futuras.

### Próximos Passos:

1. **Implementação Inicial**: Começar a implementação das classes descritas no pseudo-código.
2. **Configurar a API**: Fazer a conexão com a API do Brawl Stars e baixar as imagens correspondentes.
3. **Testes**: Adicionar testes unitários para garantir que a lógica de cada componente funcione corretamente.
4. **Interface e Funcionalidade**: Garantir que as janelas interajam corretamente e que as imagens apareçam conforme os inputs.

O que acha desta estrutura? Podemos começar a discutir os detalhes de cada módulo?

-------

Vamos começar pelo desenvolvimento do pacote app, desenvolva os script de __init__.py, controller.py, display_window.py e input_window.py conforme o solicitado anteriormente

------

Ótimo! Vamos iniciar pelo desenvolvimento dos scripts dentro do pacote `app`, mantendo a organização modular e seguindo os princípios SOLID que discutimos.

Aqui está a estrutura dos arquivos solicitados, que implementam a lógica de controle, interface de input e exibição de imagens. Esses scripts não contêm o código Python completo (para evitar fornecer o código diretamente), mas fornecem uma estrutura clara com explicações em forma de comentários e pseudo-código.

### 1. **Arquivo `__init__.py`**

O arquivo `__init__.py` é necessário para definir que o diretório `app/` é um pacote Python. Neste caso, não há necessidade de adicionar muita lógica, exceto garantir que os módulos sejam importáveis.

```python
# app/__init__.py
# Inicializa o pacote `app`
# Aqui, apenas fazemos a importação das classes do pacote para facilitar o acesso.

from .controller import Controller
from .input_window import InputWindow
from .display_window import DisplayWindow
```

### 2. **Arquivo `controller.py`**

A classe `Controller` é responsável por conectar a lógica entre a interface de input e a janela de exibição de imagens. Ela recebe o input do usuário, faz a requisição da API e atualiza a janela de exibição.

```python
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
```

### 3. **Arquivo `input_window.py`**

A classe `InputWindow` gerencia a interface de input onde o usuário insere os nomes dos personagens. Quando o usuário pressiona "Enter", ela aciona um evento para que o controlador processe o nome e atualize a janela de exibição.

```python
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
```

### 4. **Arquivo `display_window.py`**

A classe `DisplayWindow` é responsável por exibir as imagens correspondentes aos personagens dos dois times (azul e vermelho). Essa janela é separada da janela de inputs.

```python
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
```

### Explicação dos Arquivos:

1. **`controller.py`**: O controlador centraliza a lógica de comunicação entre os inputs e a janela de exibição. Ele recebe o input, processa e pede para a API buscar a imagem.
   
2. **`input_window.py`**: Gerencia a janela de input dos nomes, capturando a interação do usuário e delegando para o controlador processar as entradas.

3. **`display_window.py`**: É responsável por exibir as imagens dos personagens inseridos no input. Usa o `Pillow (PIL)` para lidar com imagens e o `Tkinter` para exibir a janela e as imagens.

4. **`__init__.py`**: Inicializa o pacote `app` e facilita o acesso às classes `Controller`, `InputWindow` e `DisplayWindow`.

---

Com essa estrutura, você tem uma base sólida para implementar as funcionalidades do projeto enquanto segue os princípios SOLID. Agora, podemos passar para a conexão com a API ou discutir mais detalhes da implementação!

-----

Agora faça o desenvolvimento do pacote models, desenvolva os script de __init__.py e character.py conforme o solicitado anteriormente, também desenvolva o script da main.py

-----

Perfeito! Vamos agora desenvolver o pacote **`models`** e também o arquivo **`main.py`** para estruturar e integrar a aplicação.

### Estrutura do Pacote `models`

#### 1. **Arquivo `__init__.py`**

Este arquivo apenas inicializa o pacote **`models`**, garantindo que os modelos possam ser importados facilmente. Ele pode exportar a classe `Character` para facilitar o acesso.

```python
# models/__init__.py
from .character import Character
```

#### 2. **Arquivo `character.py`**

A classe `Character` será o modelo que representa os personagens no sistema, encapsulando as informações necessárias, como o nome e a imagem. Isso segue o princípio de responsabilidade única (SRP), pois a classe lida exclusivamente com os dados de personagens.

```python
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
```

A classe **`Character`** encapsula:
- O nome do personagem (`name`).
- O URL da imagem do personagem (`image_url`).
  
Esses métodos ajudam a garantir que as informações sejam acessíveis de maneira controlada.

---

### Desenvolvimento do Arquivo `main.py`

O **`main.py`** será o ponto de entrada da aplicação. Ele inicializa o controlador e as janelas, e gerencia o fluxo principal. A estrutura segue os princípios SOLID, permitindo que cada parte do sistema seja bem isolada e mantenha uma única responsabilidade.

```python
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
```

### Explicação do `main.py`:

1. **Importação de Dependências**:
   - Importa o `Controller`, `InputWindow`, `DisplayWindow` e `BrawlStarsAPI`.
   
2. **Função `main()`**:
   - Inicializa as janelas de input e exibição (`InputWindow` e `DisplayWindow`).
   - Cria uma instância da classe `BrawlStarsAPI`, que será responsável por buscar as imagens dos personagens.
   - Constrói o `Controller` para conectar as janelas e a lógica de negócio.
   - Executa o loop principal da janela de inputs usando o método `run()` da classe `InputWindow`.

3. **Execução do Programa**:
   - O programa só começa a ser executado quando chamado diretamente via `__main__`. Isso garante que o código seja executado corretamente se o arquivo for rodado como script.

---

### Fluxo Geral:

- **`main.py`** inicia a aplicação, conectando o controlador com as janelas.
- **`Controller`** lida com a lógica entre as janelas de input e exibição.
- **`InputWindow`** recebe os inputs do usuário.
- **`DisplayWindow`** atualiza dinamicamente as imagens.
- **`BrawlStarsAPI`** busca as imagens dos personagens da API, usando o modelo **`Character`** para encapsular os dados.

### Próximos Passos:

Agora, com essa estrutura pronta, o próximo passo seria implementar a classe `BrawlStarsAPI` no pacote **`api/`**, que fará a comunicação real com a API do Brawl Stars para buscar as imagens dos personagens. Quer discutir a implementação dessa API ou partir para essa etapa?

-----

Agora faça o desenvolvimento do pacote api, desenvolva os script de __init__.py e brawl_stars_api.py conforme o solicitado anteriormente, também desenvolva o script da requirements.txt

Estaremos utilizando a API oficial do jogo Brawl Stars

----

Perfeito! Vamos agora desenvolver o pacote **`api`** para lidar com a comunicação com a API oficial do Brawl Stars, além de definir as dependências no arquivo **`requirements.txt`**.

### Desenvolvimento do Pacote `api`

#### 1. **Arquivo `__init__.py`**

Esse arquivo simplesmente inicializa o pacote **`api`** e garante que a classe **`BrawlStarsAPI`** esteja disponível para ser importada diretamente.

```python
# api/__init__.py
from .brawl_stars_api import BrawlStarsAPI
```

#### 2. **Arquivo `brawl_stars_api.py`**

A classe **`BrawlStarsAPI`** será responsável por fazer as requisições HTTP para a API oficial do Brawl Stars, obtendo as informações dos personagens, como o nome e a URL da imagem.

Para se comunicar com a API do Brawl Stars, utilizaremos a biblioteca `requests` para realizar as chamadas HTTP.

**Importante**: A API oficial do Brawl Stars requer um token de autenticação, que pode ser obtido ao se registrar para usar a API. Vamos usar este token para autenticar nossas requisições.

Aqui está o código para a classe **`BrawlStarsAPI`**:

```python
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

```

### Explicação do Código:

1. **URL Base da API**: A constante `BASE_URL` armazena a URL base da API oficial do Brawl Stars.
   - O endpoint **`/brawlers`** é utilizado para obter a lista de todos os personagens do jogo.
   
2. **Autenticação**: A API requer um **token de API** (que pode ser obtido ao registrar o aplicativo na API do Brawl Stars). O token é enviado no cabeçalho HTTP como **Bearer Token**.
   
3. **Método `get_character_image(name)`**:
   - **Requisição**: Faz uma requisição HTTP GET para o endpoint `/brawlers` e recebe uma lista com todos os personagens.
   - **Processamento**: Procura o personagem pelo nome (insensível a maiúsculas/minúsculas) e retorna uma instância da classe `Character` com o nome do personagem e a URL da imagem (`imageUrl2`).
   - **Tratamento de Erros**: Lança exceções adequadas se a requisição falhar ou se o personagem não for encontrado.

4. **Manipulação de Exceções**:
   - **`ValueError`**: Lança um erro se o nome do personagem não for encontrado na lista de brawlers.
   - **`ConnectionError`**: Lança um erro se houver um problema de conexão ou se a API retornar um status de erro (diferente de 200).

---

### Arquivo `requirements.txt`

O **`requirements.txt`** especifica as bibliotecas externas que o projeto necessita. Usaremos o **`requests`** para fazer as requisições HTTP e o **`Pillow`** (PIL) para manipular imagens no Tkinter.

Aqui está o conteúdo do **`requirements.txt`**:

```
requests==2.28.1  # Para fazer requisições HTTP
Pillow==9.1.1     # Para lidar com imagens no Tkinter
```

### Dependências Explicadas:

- **`requests`**: Biblioteca popular para fazer requisições HTTP em Python. Usada para se comunicar com a API do Brawl Stars.
- **`Pillow`**: Um fork do PIL (Python Imaging Library), necessário para carregar e exibir imagens no `Tkinter`.

---

### Como Obter o Token da API:

1. **Registrar na API do Brawl Stars**: Para usar a API, você precisará registrar uma conta e criar um aplicativo na página oficial da [Supercell Developer](https://developer.brawlstars.com/).
   
2. **Gerar o Token**: Após registrar o aplicativo, você receberá um token de autenticação. Esse token deve ser adicionado ao código na variável **`API_TOKEN`** no arquivo `brawl_stars_api.py`.

---

### Próximos Passos:

- **Obtenha o Token da API** e teste a integração com a API oficial do Brawl Stars.
- **Execute o projeto**: Agora que todas as partes estão integradas, você pode rodar o arquivo `main.py` para testar a aplicação.

Se precisar de ajustes ou mais detalhes sobre a implementação da API, fique à vontade para perguntar!

-------

Após executar o programa pela primeira vez, me deparei com o seguinte output ao inserir o nome de um personagem chamado "colt" no pirmeiro input:

Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 20, in <lambda>
    input_entry.bind("<Return>", lambda event, team='blue', idx=i: self.on_input(team, input_entry.get()))    
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 48, in on_input
    self.controller.process_input(team, name)
  File "c:\Users\Lucas\Desktop\Jhon\app\controller.py", line 25, in process_input
    image_url = self.api_client.get_character_image(name)
  File "c:\Users\Lucas\Desktop\Jhon\api\brawl_stars_api.py", line 34, in get_character_image
    raise ValueError(f"Personagem '{name}' não encontrado.")
ValueError: Personagem '' não encontrado.

----------------

Esse erro indica que o nome do personagem inserido no campo de input está sendo passado como uma string vazia (`''`) para o método `get_character_image()`. A exceção ocorre porque o nome do personagem não foi encontrado na API, provavelmente porque o campo de input estava vazio quando você pressionou "Enter".

Vamos revisar algumas possíveis causas e como podemos corrigir isso:

### Problema:
1. **O campo de input estava vazio**: Parece que o usuário pressionou "Enter" antes de inserir o nome do personagem, ou o nome não foi capturado corretamente no evento de entrada.
   
2. **Verificação do valor do input**: Não houve verificação se o valor do input está vazio antes de tentar fazer a chamada para a API.

### Solução:

Precisamos garantir que o nome do personagem não seja uma string vazia antes de prosseguir com a chamada da API. Podemos adicionar uma validação no método `on_input` dentro de `InputWindow` para verificar se o nome inserido não está vazio.

Aqui está a correção para o arquivo **`input_window.py`**:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", "O nome do personagem não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, name)
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))
```

### O que foi corrigido:

1. **Validação do Input**:
   - O método `name.strip()` remove qualquer espaço em branco ao redor do nome. Isso evita que um nome inserido como `"  colt "` seja processado incorretamente.
   - O bloco `if not name:` verifica se o nome está vazio ou contém apenas espaços. Se for o caso, uma mensagem de erro é exibida e a execução é interrompida (não prossegue para a API).
   
2. **Tratamento de Exceção**:
   - O método `process_input` foi envolvido em um bloco `try/except`. Se a exceção `ValueError` for lançada (por exemplo, quando o personagem não é encontrado), uma mensagem de erro será exibida ao usuário através de um popup.

### Ajustes Recomendados:

1. **Interface com Feedback**: Agora, o usuário receberá um feedback claro quando tentar submeter um nome vazio ou um nome de personagem que não existe na API.
   
2. **Evitar Inputs Vazios**: Essa validação de campo vazio é essencial para evitar chamadas desnecessárias à API e melhorar a experiência do usuário.

### Teste:

Agora, ao rodar o programa e tentar pressionar "Enter" com um campo de input vazio, uma mensagem de erro será exibida e o programa não tentará fazer a chamada à API. Se o nome do personagem for inválido (não encontrado na API), outra mensagem de erro será mostrada.

Tente rodar o programa novamente com essa correção e veja se o problema foi resolvido. Se encontrar outros problemas, me avise!

----------

Fui tentar executar o código e tivemos o seguinte resultado:

Traceback (most recent call last):
  File "c:\Users\Lucas\Desktop\Jhon\main.py", line 25, in <module>
    main()
  File "c:\Users\Lucas\Desktop\Jhon\main.py", line 22, in main
    input_window.run()
AttributeError: 'InputWindow' object has no attribute 'run'

-------------

O erro mencionado indica que o método `run()` não foi implementado ou não existe na classe `InputWindow`. A classe `InputWindow` deveria ter um método responsável por iniciar o loop principal do `Tkinter`, que é o que faz com que a interface gráfica fique "ativa" e responsiva.

No `Tkinter`, o loop principal da interface gráfica é iniciado com o método `mainloop()` da janela principal (normalmente, `root`). No código que forneci anteriormente, esquecemos de definir o método `run()` para chamar esse `mainloop()`.

### Solução

Vamos adicionar o método `run()` na classe `InputWindow`, que simplesmente chama `self.root.mainloop()`, garantindo que a interface gráfica seja exibida e funcione corretamente.

Aqui está a correção:

#### Arquivo **`input_window.py`**:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", "O nome do personagem não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, name)
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

### O que foi adicionado:

- **Método `run()`**: Esse método agora chama `self.root.mainloop()`, que é o loop principal do `Tkinter`. Ele mantém a interface gráfica aberta e em funcionamento até que o usuário feche a janela.

Agora, o método `run()` está presente e correto. No **`main.py`**, ele pode ser chamado para iniciar a janela de inputs.

### Teste

Tente rodar o programa novamente e veja se o problema foi resolvido. A janela de inputs deve ser exibida e funcionar corretamente, permitindo que você insira os nomes dos personagens.

--------

Após as implementações, obtivemos o seguinte output:

Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 29, in <lambda>
    input_entry.bind("<Return>", lambda event, team='red', idx=i: self.on_input(team, input_entry.get()))     
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 54, in on_input
    self.controller.process_input(team, name)
  File "c:\Users\Lucas\Desktop\Jhon\app\controller.py", line 25, in process_input
    image_url = self.api_client.get_character_image(name)
  File "c:\Users\Lucas\Desktop\Jhon\api\brawl_stars_api.py", line 32, in get_character_image
    return Character(brawler["name"], brawler["imageUrl2"])
KeyError: 'imageUrl2'

-------

O erro que você está recebendo ocorre porque o dicionário que representa os dados do **personagem (brawler)** retornado pela API do Brawl Stars não contém a chave `"imageUrl2"`. Isso significa que a API pode estar retornando os dados do personagem com uma chave diferente, ou talvez o dado da imagem esteja estruturado de forma diferente no JSON.

### Solução:

1. **Verificar a Estrutura da Resposta da API**: Primeiramente, precisamos verificar quais chaves estão presentes na resposta da API. Uma maneira simples de fazer isso é inspecionar a resposta e ver quais dados estão disponíveis.

2. **Alterar a Chave da Imagem**: Vamos ajustar o código para usar a chave correta para a imagem, que pode ser `"imageUrl"` ou outra chave relacionada a imagens.

### Como Ajustar:

#### Passo 1: Imprimir a Resposta da API

Adicione um `print()` no método `get_character_image()` da classe `BrawlStarsAPI` para ver exatamente como a resposta da API está estruturada.

#### Arquivo **`brawl_stars_api.py`** (com o `print` para depuração):

```python
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
                    # Imprime o dicionário brawler para inspecionar suas chaves
                    print(f"Brawler encontrado: {brawler}")
                    
                    # Verifica as chaves disponíveis
                    if "imageUrl" in brawler:
                        return Character(brawler["name"], brawler["imageUrl"])
                    else:
                        raise KeyError(f"A imagem para '{name}' não foi encontrada.")
            # Se o personagem não for encontrado, pode-se retornar uma imagem padrão ou erro
            raise ValueError(f"Personagem '{name}' não encontrado.")
        else:
            # Trata erros de conexão ou resposta não 200
            raise ConnectionError(f"Erro ao acessar a API do Brawl Stars: {response.status_code}")
```

#### Passo 2: Rodar o Código e Verificar a Estrutura

Execute o código novamente e, ao inserir o nome de um personagem, a saída deve incluir um dicionário que representa o personagem encontrado. Este dicionário conterá as chaves corretas.

Você verá algo como:

```json
Brawler encontrado: {
    "id": 16000000,
    "name": "Colt",
    "starPowers": [...],
    "gadgets": [...],
    "imageUrl": "https://url-to-image",
    ...
}
```

#### Passo 3: Usar a Chave Correta

Se a chave correta for `"imageUrl"`, podemos ajustar o código para usar essa chave. Com base na inspeção, podemos alterar o código da seguinte maneira:

```python
# api/brawl_stars_api.py
def get_character_image(self, name):
    # Código existente...

    for brawler in brawlers:
        if brawler["name"].lower() == name.lower():
            # Use a chave correta para a URL da imagem
            return Character(brawler["name"], brawler["imageUrl"])
```

### Conclusão

O erro **`KeyError: 'imageUrl2'`** ocorre porque a chave `"imageUrl2"` não existe no objeto retornado pela API. Após inspecionar a resposta da API, você poderá usar a chave correta (provavelmente `"imageUrl"`).

Rode o código com o `print` para depurar e me avise se precisar de mais ajuda para ajustar o código!

-----

O output foi o seguinte:

Brawler encontrado: {'id': 16000001, 'name': 'COLT', 'starPowers': [{'id': 23000077, 'name': 'SLICK BOOTS'}, {'id': 23000138, 'name': 'MAGNUM SPECIAL'}], 'gadgets': [{'id': 23000273, 'name': 'SPEEDLOADER'}, {'id': 23000319, 'name': 'SILVER BULLET'}]}
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 29, in <lambda>
    input_entry.bind("<Return>", lambda event, team='red', idx=i: self.on_input(team, input_entry.get()))     
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 54, in on_input
    self.controller.process_input(team, name)
  File "c:\Users\Lucas\Desktop\Jhon\app\controller.py", line 25, in process_input
    image_url = self.api_client.get_character_image(name)
  File "c:\Users\Lucas\Desktop\Jhon\api\brawl_stars_api.py", line 38, in get_character_image
    raise KeyError(f"A imagem para '{name}' não foi encontrada.")
KeyError: "A imagem para 'Colt' não foi encontrada."

-------

Parece que o dicionário retornado pela API para o personagem **Colt** não contém a chave que armazena a URL da imagem do personagem. A estrutura de dados retornada para **Colt** inclui `id`, `name`, `starPowers` e `gadgets`, mas não há informações de imagem.

### Solução:

1. **Verificar a Documentação da API**: É possível que as informações de imagem estejam localizadas em outro endpoint da API ou em outro nível da resposta JSON.
2. **Adicionar uma Imagem Padrão Temporária**: Enquanto não encontramos a imagem correta, podemos adicionar uma imagem padrão para evitar que o programa quebre.

### Solução Temporária - Imagem Padrão

Até encontrarmos a fonte correta da imagem na API, podemos usar uma imagem genérica temporária quando a chave não estiver presente.

Aqui está como podemos implementar isso:

#### Modifique o código da classe `BrawlStarsAPI` para usar uma imagem padrão:

```python
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
                    # Verifica as chaves disponíveis e retorna uma imagem padrão se não houver URL de imagem
                    if "imageUrl" in brawler:
                        return Character(brawler["name"], brawler["imageUrl"])
                    else:
                        # Imagem padrão caso a API não retorne uma imagem
                        default_image_url = "https://via.placeholder.com/150"
                        return Character(brawler["name"], default_image_url)
            # Se o personagem não for encontrado, pode-se retornar uma imagem padrão ou erro
            raise ValueError(f"Personagem '{name}' não encontrado.")
        else:
            # Trata erros de conexão ou resposta não 200
            raise ConnectionError(f"Erro ao acessar a API do Brawl Stars: {response.status_code}")
```

### Explicação:

1. **Imagem Padrão**:
   - Se a chave `"imageUrl"` não estiver presente no dicionário do personagem (como ocorreu no caso do **Colt**), a função retorna uma **URL de imagem padrão** (`https://via.placeholder.com/150`). Isso evita que o programa quebre enquanto continuamos a buscar a solução adequada.
   
2. **URL de Placeholder**:
   - O URL `"https://via.placeholder.com/150"` é uma imagem genérica que pode ser usada como placeholder enquanto a imagem real não está disponível.

### Próximos Passos:

- **Teste novamente o código**: Veja se, ao inserir o nome **Colt**, a imagem padrão é carregada.
- **Revisar a documentação da API**: Verifique se há outro endpoint ou formato de resposta que forneça as imagens dos personagens.

Esse ajuste deve permitir que o programa continue funcionando corretamente, mesmo sem a URL da imagem real. Se preferir, podemos tentar investigar mais a fundo o motivo pelo qual a imagem não está sendo retornada pela API.

----------

Okay, nós estamos com muitos problemas utilizando a API oficial do jogo Brawl Stars, então vamos migrar para a utilização da API BrawlAPI , faça as modificações adequadas para que utilizemos a API deles

---------
Entendido! Vamos migrar para a **API BrawlAPI**, que oferece uma alternativa para acessar os dados do jogo **Brawl Stars**. A principal diferença aqui será o uso de novos endpoints e, possivelmente, uma estrutura de resposta diferente.

### Passos para Migrar para a BrawlAPI:

1. **Obter um Token da BrawlAPI**: A BrawlAPI também requer autenticação via token. Certifique-se de obter um token acessando o site da [BrawlAPI](https://brawlapi.com/).

2. **Modificar o Endereço Base da API**: A BrawlAPI tem uma URL base diferente, e seus endpoints podem ser ligeiramente distintos.

3. **Adaptar a Estrutura da Resposta**: Precisamos ajustar o código para lidar com o formato de resposta que a BrawlAPI fornece.

### Documentação da BrawlAPI:
- Endpoint: `https://api.brawlapi.com/v1/brawlers`
- A API BrawlAPI pode fornecer informações detalhadas dos brawlers, incluindo URLs de imagens.

### Modificações na Classe `BrawlStarsAPI` para BrawlAPI

#### 1. Atualize o arquivo `brawl_stars_api.py` para usar a BrawlAPI

```python
# api/brawl_stars_api.py
import requests
from models.character import Character

class BrawlStarsAPI:
    BASE_URL = "https://api.brawlapi.com/v1"  # URL base da BrawlAPI
    API_TOKEN = "SEU_TOKEN_AQUI"  # Insira o token da BrawlAPI aqui

    def __init__(self):
        """
        Inicializa o cliente da API BrawlAPI com o cabeçalho de autenticação.
        """
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}"
        }

    def get_character_image(self, name):
        """
        Busca os detalhes do personagem e sua imagem pela API do BrawlAPI.
        :param name: Nome do personagem inserido pelo usuário.
        :return: Instância de Character com o nome e URL da imagem.
        """
        endpoint = f"{self.BASE_URL}/brawlers"
        response = requests.get(endpoint, headers=self.headers)

        if response.status_code == 200:
            brawlers = response.json().get("list", [])  # "list" é onde os brawlers são armazenados
            # Procura o personagem pelo nome na lista de brawlers
            for brawler in brawlers:
                if brawler["name"].lower() == name.lower():
                    # Verifica as chaves disponíveis e retorna a URL da imagem
                    if "imageUrl" in brawler:
                        return Character(brawler["name"], brawler["imageUrl"])
                    else:
                        # Imagem padrão caso a API não retorne uma imagem
                        default_image_url = "https://via.placeholder.com/150"
                        return Character(brawler["name"], default_image_url)
            # Se o personagem não for encontrado, pode-se retornar uma imagem padrão ou erro
            raise ValueError(f"Personagem '{name}' não encontrado.")
        else:
            # Trata erros de conexão ou resposta não 200
            raise ConnectionError(f"Erro ao acessar a API BrawlAPI: {response.status_code}")
```

### Explicações:

1. **URL Base**:
   - A URL base foi alterada para `"https://api.brawlapi.com/v1"` da **BrawlAPI**.

2. **Endpoint**:
   - O endpoint para acessar os brawlers agora é **`/brawlers`**.

3. **Estrutura de Resposta**:
   - A resposta JSON da BrawlAPI lista os brawlers sob a chave `"list"`. Portanto, agora usamos `brawlers = response.json().get("list", [])`.

4. **Tratamento de Imagens**:
   - Se a chave `"imageUrl"` estiver disponível no brawler, a imagem é usada diretamente. Caso contrário, uma imagem padrão será utilizada.

### Token da BrawlAPI

Certifique-se de obter o token de autenticação da BrawlAPI e substitua a string `"SEU_TOKEN_AQUI"` no código.

### Modificações Concluídas

Agora, você pode rodar o programa utilizando a **BrawlAPI**. Faça os seguintes ajustes:

1. **Atualize o arquivo `brawl_stars_api.py`** com o código acima.
2. **Insira o token da BrawlAPI** para garantir a autenticação correta.
3. **Teste novamente o fluxo** para garantir que os dados e as imagens dos personagens sejam carregados corretamente.

Se tudo estiver funcionando conforme esperado, o fluxo do programa deve ser o mesmo, porém agora com o suporte à nova API.

-----------
Acredito que na verdade eles funcionam com https requests, como por exemplo:

https://api.brawlify.com/v1/brawlers/16000038

retorna:

{
    "id": 16000038,
    "avatarId": 28000053,
    "name": "Surge",
    "hash": "Surge",
    "path": "Surge",
    "fankit": "surge",
    "released": true,
    "version": 1,
    "link": "https://brawlify.com/brawlers/detail/Surge",
    "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000038.png",
    "imageUrl2": "https://cdn.brawlify.com/brawlers/borderless/16000038.png",
    "imageUrl3": "https://cdn-fankit.brawlify.com/surge_pin.png",
    "class": {
        "id": 1,
        "name": "Damage Dealer"
    },
    "rarity": {
        "id": 6,
        "name": "Legendary",
        "color": "#fff11e"
    },
    "unlock": null,
    "description": "Surge is a souped-up soda fountain, always ready to get the party started! He's got the beats, the moves, and an endless supply of energy drinks.",
    "descriptionHtml": "Surge is a souped-up soda fountain, always ready to get the party started! He's got the beats, the moves, and an endless supply of energy drinks.",
    "starPowers": [
        {
            "id": 23000283,
            "name": "To The Max",
            "path": "To-The-Max",
            "version": 1,
            "description": "Surge's main attack now splits when hitting walls.",
            "descriptionHtml": "Surge's main attack now splits when hitting walls.",
            "imageUrl": "https://cdn.brawlify.com/star-powers/borderless/23000283.png",
            "released": true
        },
        {
            "id": 23000284,
            "name": "Serve Ice Cold",
            "path": "Serve-Ice-Cold",
            "version": 1,
            "description": "Surge keeps his STAGE 1 Super upgrade for the full match duration.",
            "descriptionHtml": "Surge keeps his STAGE 1 Super upgrade for the full match duration.",
            "imageUrl": "https://cdn.brawlify.com/star-powers/borderless/23000284.png",
            "released": true
        }
    ],
    "gadgets": [
        {
            "id": 23000285,
            "name": "Power Surge",
            "path": "Power-Surge",
            "version": 1,
            "description": "Surge overloads his circuits and increases his upgrade level by x for x seconds.",
            "descriptionHtml": "Surge overloads his circuits and increases his upgrade level by <span style=\"color:#00cc00;\">x</span> for <span style=\"color:#00cc00;\">x</span> seconds.",
            "imageUrl": "https://cdn.brawlify.com/gadgets/borderless/23000285.png",
            "released": true
        },
        {
            "id": 23000485,
            "name": "Power Shield",
            "path": "Power-Shield",
            "version": 1,
            "description": "Within the next x seconds, Surge consumes x% of the damage of the next incoming hit and uses the energy to reload x ammo.",
            "descriptionHtml": "Within the next <span style=\"color:#00cc00;\">x</span> seconds, Surge consumes <span style=\"color:#00cc00;\">x%</span> of the damage of the next incoming hit and uses the energy to reload <span style=\"color:#00cc00;\">x</span> ammo.",
            "imageUrl": "https://cdn.brawlify.com/gadgets/borderless/23000485.png",
            "released": true
        }
    ],
    "videos": []
}

--------

Obrigado pelo esclarecimento! A API **BrawlAPI** funciona via requisições HTTPS diretas para endpoints específicos de cada personagem, como o exemplo que você mostrou. Agora, precisamos ajustar o código para fazer uma requisição diretamente ao endpoint específico do brawler com o ID, em vez de obter todos os brawlers de uma vez.

### Como Modificar a Classe `BrawlStarsAPI` para Funcionar com a BrawlAPI:

Sabendo que podemos acessar os detalhes de um brawler específico via um URL como `https://api.brawlify.com/v1/brawlers/{id}`, podemos alterar a implementação da API no nosso código para:
- Fazer uma requisição para o endpoint de um brawler específico.
- Usar o **ID do brawler** para compor a URL da requisição.
- Extrair a URL da imagem e outras informações desejadas da resposta JSON retornada.

### Modificações no Código da API

Aqui está a nova implementação da classe **`BrawlStarsAPI`** para utilizar a BrawlAPI com requisições HTTPS diretas para cada brawler.

#### Modifique o arquivo `brawl_stars_api.py`:

```python
# api/brawl_stars_api.py
import requests
from models.character import Character

class BrawlStarsAPI:
    BASE_URL = "https://api.brawlify.com/v1/brawlers"  # Base URL para buscar brawlers por ID

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
```

### Explicações:

1. **URL Base**:
   - O endpoint da API foi ajustado para `https://api.brawlify.com/v1/brawlers`, e faremos a requisição com base no ID do brawler.

2. **Requisição com ID Específico**:
   - Em vez de listar todos os brawlers de uma vez, agora fazemos a requisição para um endpoint específico, passando o **ID do brawler** diretamente na URL, como `https://api.brawlify.com/v1/brawlers/{id}`.

3. **Estrutura de Resposta**:
   - Após a requisição, a resposta JSON contém informações detalhadas do brawler, incluindo o nome (`name`) e a URL da imagem (`imageUrl2`).
   - A imagem é retornada a partir da chave `"imageUrl2"`, que contém a imagem sem bordas, mas você pode escolher `"imageUrl"`, `"imageUrl3"` ou outra, conforme suas preferências.

4. **Imagem Padrão**:
   - Caso a imagem não seja encontrada, uma imagem padrão (`https://via.placeholder.com/150`) é usada.

### Modificação na Interface do Programa (Input dos IDs)

Agora que precisamos do **ID do brawler**, você pode alterar a lógica para que o usuário insira o ID do brawler diretamente ou manter um mapeamento de IDs a partir dos nomes. Aqui está uma sugestão para mapear nomes para IDs:

#### Exemplo de Mapeamento de Nomes para IDs:

```python
# Exemplo simples de dicionário para mapear nomes de brawlers para seus IDs
BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers aqui
}
```

#### Adapte a Chamada no Controlador:

No seu **controller.py**, ao invés de buscar pelo nome diretamente, podemos buscar o ID do brawler com base no nome inserido:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

class Controller:
    def __init__(self, input_window, display_window, api_client):
        self.input_window = input_window
        self.display_window = display_window
        self.api_client = api_client
        self.input_window.set_controller(self)

    def process_input(self, team, name):
        """
        Processa o input de um nome inserido pelo usuário.
        :param team: Time azul ou vermelho
        :param name: Nome do personagem inserido no input
        """
        name = name.lower()  # Converter o nome para minúsculas
        if name in BRAWLER_IDS:
            brawler_id = BRAWLER_IDS[name]
            image_url = self.api_client.get_character_image(brawler_id)
            self.display_window.update_image(team, image_url)
        else:
            raise ValueError(f"Personagem '{name}' não encontrado.")
```

### Testando a Nova Implementação

1. **Obtenha os IDs dos brawlers**: Você pode pegar mais IDs diretamente do site da [Brawlify](https://brawlify.com/).
2. **Teste a Interface**: Execute o programa, insira o nome do brawler (como **Colt** ou **Surge**) e veja se a imagem correspondente aparece corretamente na janela de exibição.

Se precisar de mais ajustes ou quiser adicionar novos brawlers ao mapeamento, é só adaptar o dicionário `BRAWLER_IDS`. 

Agora sua aplicação está ajustada para utilizar a BrawlAPI com requisições HTTPS diretas!

------------

Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 29, in <lambda>
    input_entry.bind("<Return>", lambda event, team='red', idx=i: self.on_input(team, input_entry.get()))
  File "c:\Users\Lucas\Desktop\Jhon\app\input_window.py", line 54, in on_input
    self.controller.process_input(team, name)
  File "c:\Users\Lucas\Desktop\Jhon\app\controller.py", line 26, in process_input
    self.display_window.update_image(team, image_url)
  File "c:\Users\Lucas\Desktop\Jhon\app\display_window.py", line 32, in update_image
    img_tk = ImageTk.PhotoImage(image)
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageTk.py", line 121, in __init__ 
    mode = Image.getmodebase(mode)
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\Image.py", line 253, in getmodebase
    return ImageMode.getmode(mode).basemode
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageMode.py", line 90, in getmode 
    return _modes[mode]
KeyError: None
Exception ignored in: <function PhotoImage.__del__ at 0x000002A0C771DD30>
Traceback (most recent call last):
  File "C:\Users\Lucas\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageTk.py", line 131, in __del__
    name = self.__photo.name
AttributeError: 'PhotoImage' object has no attribute '_PhotoImage__photo'

tentei pesquisar por colt e não consegui novamente o output foi esse

--------

O erro que você está recebendo está relacionado à maneira como estamos manipulando a imagem retornada pela API e como a biblioteca **Pillow** (PIL) e **Tkinter** lidam com a exibição dessas imagens. O problema ocorre quando o código tenta criar um objeto **`PhotoImage`** a partir de uma imagem baixada ou quando a imagem retornada não é manipulada corretamente.

Vamos resolver isso em algumas etapas.

### 1. **Baixar a Imagem Corretamente**

Atualmente, a URL da imagem está sendo retornada diretamente pela API, mas precisamos de um passo adicional: baixar a imagem da internet e convertê-la em um formato que o `Pillow` (PIL) entenda para que ela possa ser exibida no **Tkinter**.

Para baixar a imagem a partir da URL, podemos usar a biblioteca `requests` para obter a imagem e, em seguida, convertê-la em um objeto **PIL.Image**. Depois disso, podemos convertê-la em um formato compatível com o **Tkinter** usando **`ImageTk.PhotoImage`**.

### Modificações no Código

#### Passo 1: Baixar a Imagem com `requests` e Carregar com PIL

Vamos modificar o arquivo **`display_window.py`** para baixar a imagem e garantir que seja carregada corretamente no formato que o **Tkinter** espera.

#### Modifique o Arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

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
        # Faz o download da imagem a partir do URL (usando requests)
        image = self.download_image(image_url)
        
        # Converte a imagem para um formato compatível com Tkinter
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
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que a requisição foi bem-sucedida
            image_data = BytesIO(response.content)  # Lê os dados da imagem
            return Image.open(image_data)  # Abre a imagem com o PIL
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            # Retorna uma imagem padrão em caso de erro
            return Image.new("RGB", (150, 150), color=(255, 0, 0))
```

### Explicação do que foi Alterado:

1. **Função `download_image`**:
   - Faz uma requisição HTTP para baixar a imagem a partir da URL usando `requests.get`.
   - Converte os dados da resposta em um objeto `BytesIO`, que pode ser tratado como um arquivo em memória.
   - Usa `PIL.Image.open()` para carregar a imagem em um formato que a biblioteca Pillow entenda.

2. **Manuseio de Erros**:
   - Caso ocorra um erro durante o download da imagem (ex.: URL inválida ou problemas de rede), uma imagem padrão é retornada.

3. **Conversão para `ImageTk.PhotoImage`**:
   - Depois que a imagem é baixada e carregada pelo `PIL`, ela é convertida para um formato que o **Tkinter** entende usando `ImageTk.PhotoImage(image)`.

### Passo 2: Verifique o Controlador

Certifique-se de que o controlador (`controller.py`) está passando uma URL válida para a função `update_image`. Como estamos lidando com URLs da API, o endpoint de imagem precisa estar correto.

### Teste a Aplicação Novamente

1. Tente executar o programa e inserir o nome de um personagem (por exemplo, "Colt").
2. Verifique se a imagem correspondente ao personagem é baixada corretamente e exibida na janela.

### Possíveis Ajustes Finais

Se a imagem ainda não aparecer corretamente:
- Certifique-se de que a URL da imagem retornada pela API está correta (você pode testar a URL diretamente no navegador).
- Verifique se a biblioteca **Pillow** e o **Tkinter** estão funcionando corretamente em sua instalação.

Com essa solução, o programa deve ser capaz de baixar a imagem e exibi-la corretamente na interface gráfica!


-------------

Tivemos um avanço, porém o output foi o seguinte:

Erro ao baixar a imagem: Invalid URL '<models.character.Character object at 0x000001CC844D3850>': No scheme supplied. Perhaps you meant https://<models.character.Character object at 0x000001CC844D3850>?

--------------

Esse erro está acontecendo porque o **`image_url`** que está sendo passado para a função **`update_image`** não é uma URL, mas sim um objeto da classe `Character`. No código, estamos passando o **objeto `Character`** inteiro para o método **`update_image`**, enquanto deveríamos passar apenas o **atributo da URL da imagem** desse objeto.

### Correção

Precisamos garantir que, no controlador **`controller.py`**, ao chamarmos **`update_image`**, estejamos passando a **URL da imagem** que está armazenada no atributo `image_url` do objeto `Character`.

Aqui está a correção para o arquivo **`controller.py`**:

### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

class Controller:
    def __init__(self, input_window, display_window, api_client):
        self.input_window = input_window
        self.display_window = display_window
        self.api_client = api_client
        self.input_window.set_controller(self)

    def process_input(self, team, name):
        """
        Processa o input de um nome inserido pelo usuário.
        :param team: Time azul ou vermelho
        :param name: Nome do personagem inserido no input
        """
        name = name.lower()  # Converter o nome para minúsculas
        if name in BRAWLER_IDS:
            brawler_id = BRAWLER_IDS[name]
            # Obtém o objeto Character
            character = self.api_client.get_character_image(brawler_id)
            # Passa apenas a URL da imagem, não o objeto inteiro
            self.display_window.update_image(team, character.get_image_url())
        else:
            raise ValueError(f"Personagem '{name}' não encontrado.")
```

### Explicação:

- No método `process_input`, agora estamos **pegando a URL da imagem diretamente** do objeto `Character` retornado por `self.api_client.get_character_image(brawler_id)`.
- O método `get_image_url()` da classe `Character` retorna a URL da imagem, que é então passada para o método **`update_image`**.

### Verifique a Classe `Character` para Garantir o Método `get_image_url`

O objeto `Character` deve ter o método **`get_image_url()`** para retornar a URL correta. Aqui está como sua classe `Character` deve estar definida:

#### Verifique o Arquivo `character.py`:

```python
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
```

### Teste Novamente

Agora, com a URL da imagem sendo passada corretamente para o método `update_image`, o programa deve baixar e exibir a imagem correta do personagem.

Rode o programa e insira o nome de um personagem, como **"Colt"**, e veja se a imagem aparece corretamente na interface.

Se ainda houver algum erro, me avise!

-----------

Perfeito, etamos conseguindo exibir a imagem corretamente na tela agora, porém por algum motivo, ao invés de cada input gerar uma imagem de cada lado da tela, apenas um input do time vermelho está aparecendo, faça com que cada input exiba uma imagem diferente na janela, eles não dependem um dos outros, e as imagens devem ser geradas uma embaixo da outra, as azuis do lado esquerdo da tela e as vermelhas do lado direito 

----------------

Ótimo! Agora que as imagens estão sendo exibidas corretamente, precisamos ajustar a exibição para que as imagens de cada **input** apareçam de forma independente e corretamente alinhadas nas suas respectivas posições: as imagens dos inputs do **time azul** à esquerda, e as do **time vermelho** à direita, uma abaixo da outra.

### Problema Atual:
Aparentemente, apenas uma imagem do **time vermelho** está aparecendo, e as outras imagens não estão sendo exibidas corretamente. Isso provavelmente está acontecendo porque não estamos garantindo que as novas imagens sejam exibidas em posições diferentes, e também precisamos garantir que múltiplas imagens possam ser geradas, uma abaixo da outra, em suas respectivas colunas.

### Solução:
Precisamos ajustar o método `update_image()` para que ele adicione as imagens uma abaixo da outra, garantindo que cada time tenha sua própria coluna na tela (time azul à esquerda, time vermelho à direita). Além disso, vamos garantir que a lógica permita adicionar múltiplas imagens sem que uma substitua a outra.

### Modificação no `display_window.py`:

#### Atualize o arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Manteremos as imagens referenciadas para não serem coletadas pelo garbage collector
        self.blue_team_images = []
        self.red_team_images = []

    def update_image(self, team, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        :param team: Time azul ou vermelho
        :param image_url: URL da imagem do personagem
        """
        # Faz o download da imagem a partir do URL (usando requests)
        image = self.download_image(image_url)
        
        # Converte a imagem para um formato compatível com Tkinter
        img_tk = ImageTk.PhotoImage(image)

        # Adiciona a imagem na coluna correta (esquerda para azul, direita para vermelho)
        if team == 'blue':
            label = tk.Label(self.team_blue_frame, image=img_tk)
            label.image = img_tk  # Mantém a referência para não ser coletada pelo GC
            label.pack()  # Adiciona a imagem na próxima posição vertical no frame
            self.blue_team_images.append(label)  # Armazena para manter referência
        elif team == 'red':
            label = tk.Label(self.team_red_frame, image=img_tk)
            label.image = img_tk  # Mantém a referência
            label.pack()  # Adiciona a imagem na próxima posição vertical no frame
            self.red_team_images.append(label)

    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que a requisição foi bem-sucedida
            image_data = BytesIO(response.content)  # Lê os dados da imagem
            return Image.open(image_data)  # Abre a imagem com o PIL
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            # Retorna uma imagem padrão em caso de erro
            return Image.new("RGB", (150, 150), color=(255, 0, 0))
```

### Explicações do que foi Alterado:

1. **Layout das Imagens**:
   - Cada imagem é adicionada verticalmente com o uso de `label.pack()`. O `pack()` adiciona o próximo item na sequência vertical do frame, garantindo que as imagens sejam exibidas uma abaixo da outra.

2. **Manutenção de Referências das Imagens**:
   - As listas `self.blue_team_images` e `self.red_team_images` armazenam as referências dos labels criados para cada imagem. Isso garante que o **garbage collector** do Python não remova a imagem da memória.

3. **Frames para Time Azul e Vermelho**:
   - Cada time tem um `Frame` separado para organizar suas imagens: `team_blue_frame` para o **time azul** (esquerda) e `team_red_frame` para o **time vermelho** (direita). Isso mantém as imagens em colunas separadas.

4. **Posicionamento Vertical**:
   - O `pack()` é utilizado sem argumentos adicionais, o que faz com que as imagens sejam adicionadas uma abaixo da outra.

### Teste Novamente

Agora, ao inserir nomes de personagens nos **inputs** dos times azul e vermelho:
- As imagens do time azul aparecerão à esquerda, uma abaixo da outra.
- As imagens do time vermelho aparecerão à direita, uma abaixo da outra.

### Próximos Passos

1. **Verifique se as imagens de ambos os times são exibidas corretamente em colunas separadas**.
2. **Teste com múltiplos personagens** para garantir que as imagens aparecem de forma independente, sem substituir as anteriores.

Se precisar de mais ajustes ou encontrar qualquer outro problema, é só avisar!

-----------

Apenas uma imagem está sendo gerada, uma imagem no time vermelho do lado direito da tela, quero que apareçam 3 imagens de CADA um dos times em ambos os lados

------------

Entendido! O problema parece estar no fato de que as imagens não estão sendo atualizadas corretamente para os dois times. Precisamos garantir que, ao inserir os nomes de personagens, **cada input** está sendo tratado de maneira independente e que as imagens são exibidas corretamente em ambos os lados da tela, ou seja, 3 imagens para o **time azul** (à esquerda) e 3 imagens para o **time vermelho** (à direita).

### Ajuste no Código

O código precisa ser corrigido para garantir que:
- Cada input gere uma imagem nova, seja para o time azul ou para o time vermelho.
- As imagens apareçam de forma independente, sem substituir as anteriores.
- As imagens sejam exibidas uma abaixo da outra, tanto à esquerda quanto à direita da tela.

### Solução:
Vamos ajustar o fluxo para que os inputs de ambos os times sejam processados corretamente e suas respectivas imagens sejam exibidas em colunas separadas, uma abaixo da outra.

### Arquivo `input_window.py`:
Precisamos garantir que cada input está sendo tratado corretamente e, ao pressionar "Enter", a imagem correspondente é exibida no time certo.

#### Verifique o Código `input_window.py`:
A função `on_input()` está correta? Vamos garantir que ela funcione para cada time de forma independente. No arquivo `input_window.py`, o código deve chamar o controlador corretamente para ambos os times.

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul e 3 para o time vermelho).
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens - Brawl Stars")

        self.team_blue_inputs = []
        self.team_red_inputs = []

        # Inicializando os campos de texto para o time azul
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_entry.bind("<Return>", lambda event, team='blue', idx=i: self.on_input(team, input_entry.get()))
            input_entry.pack()
            self.team_blue_inputs.append(input_entry)

        # Inicializando os campos de texto para o time vermelho
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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", "O nome do personagem não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, name)
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

Agora, vamos ajustar o `controller.py` para garantir que estamos processando corretamente cada time.

### Arquivo `controller.py`:

Aqui, garantimos que o controlador esteja processando corretamente tanto o **time azul** quanto o **time vermelho**, exibindo as imagens conforme o input.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

class Controller:
    def __init__(self, input_window, display_window, api_client):
        self.input_window = input_window
        self.display_window = display_window
        self.api_client = api_client
        self.input_window.set_controller(self)

    def process_input(self, team, name):
        """
        Processa o input de um nome inserido pelo usuário.
        :param team: Time azul ou vermelho
        :param name: Nome do personagem inserido no input
        """
        name = name.lower()  # Converter o nome para minúsculas
        if name in BRAWLER_IDS:
            brawler_id = BRAWLER_IDS[name]
            # Obtém o objeto Character
            character = self.api_client.get_character_image(brawler_id)
            # Passa apenas a URL da imagem para a janela correta
            self.display_window.update_image(team, character.get_image_url())
        else:
            raise ValueError(f"Personagem '{name}' não encontrado.")
```

### Arquivo `display_window.py`:
Agora precisamos garantir que a exibição das imagens está correta para ambos os times.

#### Atualize o Arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Manteremos as imagens referenciadas para não serem coletadas pelo garbage collector
        self.blue_team_images = []
        self.red_team_images = []

    def update_image(self, team, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        :param team: Time azul ou vermelho
        :param image_url: URL da imagem do personagem
        """
        # Faz o download da imagem a partir do URL (usando requests)
        image = self.download_image(image_url)
        
        # Converte a imagem para um formato compatível com Tkinter
        img_tk = ImageTk.PhotoImage(image)

        # Adiciona a imagem na coluna correta (esquerda para azul, direita para vermelho)
        if team == 'blue':
            label = tk.Label(self.team_blue_frame, image=img_tk)
            label.image = img_tk  # Mantém a referência para não ser coletada pelo GC
            label.pack()  # Adiciona a imagem na próxima posição vertical no frame
            self.blue_team_images.append(label)  # Armazena para manter referência
        elif team == 'red':
            label = tk.Label(self.team_red_frame, image=img_tk)
            label.image = img_tk  # Mantém a referência
            label.pack()  # Adiciona a imagem na próxima posição vertical no frame
            self.red_team_images.append(label)

    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que a requisição foi bem-sucedida
            image_data = BytesIO(response.content)  # Lê os dados da imagem
            return Image.open(image_data)  # Abre a imagem com o PIL
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            # Retorna uma imagem padrão em caso de erro
            return Image.new("RGB", (150, 150), color=(255, 0, 0))
```

### Teste:

Agora, ao inserir os nomes dos personagens nos campos de texto, o seguinte deve acontecer:
- **Time Azul**: 3 imagens devem aparecer no lado esquerdo, uma abaixo da outra.
- **Time Vermelho**: 3 imagens devem aparecer no lado direito, uma abaixo da outra.

Tente novamente e veja se agora o comportamento é o esperado.

------------


Acredito que o problema que estamos enfrentando seja porque os inputs estão sendo relacionados uns com os outros, cada um dos inputs deve ser uma entidade diferente e não relacionada, apesar de existirem os times azuis e vermelhos, cada um dos inputs deve ser um input separadamente, que correpsonderá a uma imagem independente das outras, vamos adotar um sistema de id nos inputs para que funcione de acordo com o solicitado. Não se esqueça de manter o padrão SOLID no projeto

-------------

Entendido! A questão é que, embora os inputs sejam divididos entre **time azul** e **time vermelho**, cada um desses inputs deve ser tratado como uma entidade **independente**, sem que o comportamento de um input afete os outros. Para resolver isso, vamos:
- **Atribuir IDs únicos para cada input** (mesmo dentro de cada time) para garantir que cada input seja tratado de maneira independente.
- Garantir que cada input gere uma imagem **independente** ao ser processado, sem depender de outros inputs do mesmo time.

### Abordagem

1. **Entidades Independentes para Inputs**: Cada input será tratado como uma entidade separada com seu próprio ID, permitindo que os eventos sejam processados individualmente.
2. **Sistema de IDs para Inputs**: Atribuíremos um ID único para cada input (mesmo para inputs do mesmo time) para garantir que eles sejam processados de maneira independente.
3. **Princípios SOLID**: Manteremos a separação de responsabilidades de maneira clara (cada input lida com sua própria lógica), garantindo que o código seja modular e fácil de manter.

### Implementação

### Passo 1: Modificar `InputWindow` para Adicionar IDs Únicos

Cada input terá um ID único, o que permitirá que cada evento seja processado de forma independente.

#### Modifique o Arquivo `input_window.py`:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul e 3 para o time vermelho).
        Cada input é tratado de forma independente, com IDs únicos para identificar cada input.
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens - Brawl Stars")

        self.inputs = []  # Lista que armazenará todos os inputs, com seus IDs

        # Inicializando os campos de texto para o time azul
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"blue_{i+1}"  # ID único para cada input do time azul
            input_entry.bind("<Return>", lambda event, team='blue', input_id=input_id: self.on_input(team, input_id, input_entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'blue', 'id': input_id, 'entry': input_entry})

        # Inicializando os campos de texto para o time vermelho
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Vermelho - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"red_{i+1}"  # ID único para cada input do time vermelho
            input_entry.bind("<Return>", lambda event, team='red', input_id=input_id: self.on_input(team, input_id, input_entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'red', 'id': input_id, 'entry': input_entry})

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", "O nome do personagem não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, input_id, name)  # Passa o input ID para o controlador
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

### Passo 2: Modificar o Controlador para Usar IDs Únicos

No controlador, vamos garantir que os inputs sejam processados com base nos IDs únicos.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

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
```

### Passo 3: Ajustar `DisplayWindow` para Usar IDs Únicos e Exibir as Imagens Corretamente

No `DisplayWindow`, garantimos que as imagens de cada input sejam exibidas separadamente e corretamente organizadas por time e por ID.

#### Modifique o Arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Manteremos as imagens referenciadas para não serem coletadas pelo garbage collector
        self.blue_team_images = {}
        self.red_team_images = {}

    def update_image(self, team, input_id, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        Cada input é tratado de forma independente com base no seu ID único.
        :param team: Time azul ou vermelho
        :param input_id: ID único do input
        :param image_url: URL da imagem do personagem
        """
        # Faz o download da imagem a partir do URL (usando requests)
        image = self.download_image(image_url)
        
        # Converte a imagem para um formato compatível com Tkinter
        img_tk = ImageTk.PhotoImage(image)

        # Adiciona a imagem na coluna correta (esquerda para azul, direita para vermelho), usando o ID único
        if team == 'blue':
            if input_id not in self.blue_team_images:
                label = tk.Label(self.team_blue_frame, image=img_tk)
                label.image = img_tk  # Mantém a referência para não ser coletada pelo GC
                label.pack()  # Adiciona a imagem na próxima posição vertical no frame
                self.blue_team_images[input_id] = label  # Armazena para manter referência
        elif team == 'red':
            if input_id not in self.red_team_images:
                label = tk.Label(self.team_red_frame, image=img_tk)
                label.image = img_tk  # Mantém a referência
                label.pack()  # Adiciona a imagem na próxima posição vertical no frame
                self.red_team_images[input_id] = label

    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que a requisição foi bem-sucedida
            image_data = BytesIO(response.content)  # Lê os dados da imagem
            return Image.open(image_data)  # Abre a imagem com o PIL
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            # Ret

orna uma imagem padrão em caso de erro
            return Image.new("RGB", (150, 150), color=(255, 0, 0))
```

### Explicações:
1. **IDs Únicos**: Cada input agora tem um ID único (por exemplo, `"blue_1"`, `"red_2"`) e é tratado de maneira independente no controlador e na janela de exibição.
2. **Imagens Independentes**: Cada imagem é gerada de forma independente, e o uso de IDs únicos garante que a exibição de uma imagem não afete as outras.
3. **Estrutura Modular**: O código foi organizado de acordo com o padrão **SOLID**, com responsabilidades bem definidas entre a janela de input, o controlador e a janela de exibição.

### Teste Final:
Agora, ao inserir nomes nos inputs, as imagens devem aparecer de forma independente, uma abaixo da outra em cada time (esquerda para azul, direita para vermelho). Teste para garantir que cada input gera uma imagem independente.

--------------------

Certo, antes de consertarmos isso, vamos consertar um outro conceito que não está funcionando corretamente ainda, eu preciso que se por exemplo eu escrever apenas o valor no input 1 destinado ao time azul, a janela principal seja atualizada, mesmo se eu não preencher os outros inputs, quando eu faço isso atualmente, eu recebo a mensagem de Erro como se nao tivesse escrito nenhum nome 

-------------

Ótimo! Entendo que você quer que a janela principal seja atualizada sempre que um **input** for preenchido e a tecla "Enter" for pressionada, independentemente de outros inputs. Isso significa que não devemos forçar a dependência entre os inputs.

### Problema:
Atualmente, o erro ocorre porque o sistema espera que todos os campos sejam preenchidos, mas você quer que a janela seja atualizada sempre que um único campo é preenchido, sem esperar pelos outros.

### Solução:
Precisamos garantir que cada **input** funcione de forma independente e que, ao preencher e enviar um nome em qualquer input, a janela principal seja atualizada imediatamente. A mensagem de erro só deve aparecer se o campo preenchido estiver vazio ao pressionar "Enter".

### Etapas para Corrigir:

1. **Remover Dependência entre Inputs**: Cada input deve ser processado imediatamente, sem que os outros inputs dependam dele.
2. **Corrigir Lógica de Validação**: Exibir a mensagem de erro apenas quando o **campo individual** estiver vazio e a tecla "Enter" for pressionada.

### Modificação do `InputWindow`

Vamos garantir que a mensagem de erro só apareça se o **input específico** estiver vazio. Se ele for preenchido, o controlador será chamado para processar e atualizar a janela principal, sem verificar outros inputs.

#### Modifique o Arquivo `input_window.py`:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul e 3 para o time vermelho).
        Cada input é tratado de forma independente, com IDs únicos para identificar cada input.
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens - Brawl Stars")

        self.inputs = []  # Lista que armazenará todos os inputs, com seus IDs

        # Inicializando os campos de texto para o time azul
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"blue_{i+1}"  # ID único para cada input do time azul
            input_entry.bind("<Return>", lambda event, team='blue', input_id=input_id: self.on_input(team, input_id, input_entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'blue', 'id': input_id, 'entry': input_entry})

        # Inicializando os campos de texto para o time vermelho
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Vermelho - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"red_{i+1}"  # ID único para cada input do time vermelho
            input_entry.bind("<Return>", lambda event, team='red', input_id=input_id: self.on_input(team, input_id, input_entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'red', 'id': input_id, 'entry': input_entry})

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", f"O nome do personagem no input {input_id} não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, input_id, name)  # Passa o input ID para o controlador
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

### Explicação:
1. **Verificação de Campo Vazio**:
   - Agora, o sistema **só mostra a mensagem de erro** se o campo preenchido estiver vazio ao pressionar "Enter", mas isso **não impede que outros inputs funcionem**.
   
2. **Atualização Independente**:
   - Cada campo é processado e atualizado de forma **independente**. Se você preencher apenas o primeiro campo do time azul e pressionar "Enter", a janela principal será atualizada imediatamente.

### Ajuste no Controlador (`controller.py`)

Vamos garantir que o controlador continue funcionando corretamente e processe apenas o campo preenchido.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

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
```

### Explicação:
- O controlador agora processa o **input único** com base no `input_id` e no nome do personagem. Não depende de outros inputs.

### Teste Novamente

1. **Preencha apenas um campo** (por exemplo, o campo 1 do time azul) e pressione "Enter". A janela principal deverá ser atualizada com a imagem correspondente ao personagem inserido.
2. **Verifique se outros inputs continuam funcionando independentemente**. Por exemplo, se preencher apenas o campo do time vermelho, sua imagem deverá ser exibida corretamente na janela.

Com essa abordagem, garantimos que cada input funciona de forma independente e que a janela principal é atualizada imediatamente ao preencher qualquer campo, sem exigir o preenchimento de todos os campos.

Se tudo estiver funcionando como esperado, agora podemos prosseguir com a correção final da lógica dos IDs independentes para garantir que as imagens sejam exibidas de forma correta e ordenada.

------------------

Eu debbuguei o código e percebi que o problema é que temos a variavel chamada name, ela fica relacionada apenas com o último input, por isso que apenas o input red_3 é exibido na tela, faça com que exista uma variavel name para cada um dos inputs para que ele seja exibido corretamente, ou implemente de uma forma diferente, utilizando um for na exibição

-------------------

O problema que você identificou está relacionado ao **uso de closures** no loop que atribui os bindings para cada campo de input. A variável `name` acaba compartilhada entre todas as funções criadas no loop, e é por isso que, ao final, todos os inputs ficam associados ao último campo, no caso, o **input `red_3`**.

### Solução:
Precisamos garantir que cada **input** tenha uma referência **independente** ao seu valor. Para fazer isso, podemos resolver o problema de closures usando um **argumento padrão** na função `lambda`, ou então reestruturar o código de forma que cada campo mantenha sua própria instância de nome.

### Abordagem 1: Corrigir a Referência com Lambda

Ao criar o binding com o evento `<Return>`, precisamos capturar corretamente o valor do **input específico** para evitar que todos os bindings usem a mesma referência.

#### Modifique o Arquivo `input_window.py`:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com 6 campos de texto (3 para o time azul e 3 para o time vermelho).
        Cada input é tratado de forma independente, com IDs únicos para identificar cada input.
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens - Brawl Stars")

        self.inputs = []  # Lista que armazenará todos os inputs, com seus IDs

        # Inicializando os campos de texto para o time azul
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Azul - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"blue_{i+1}"  # ID único para cada input do time azul
            # Usamos um argumento padrão na lambda para capturar o input_entry corretamente
            input_entry.bind("<Return>", lambda event, team='blue', input_id=input_id, entry=input_entry: self.on_input(team, input_id, entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'blue', 'id': input_id, 'entry': input_entry})

        # Inicializando os campos de texto para o time vermelho
        for i in range(3):
            label = tk.Label(self.root, text=f"Time Vermelho - Jogador {i + 1}")
            label.pack()
            input_entry = tk.Entry(self.root)
            input_id = f"red_{i+1}"  # ID único para cada input do time vermelho
            # Usamos um argumento padrão na lambda para capturar o input_entry corretamente
            input_entry.bind("<Return>", lambda event, team='red', input_id=input_id, entry=input_entry: self.on_input(team, input_id, entry.get()))
            input_entry.pack()
            self.inputs.append({'team': 'red', 'id': input_id, 'entry': input_entry})

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
        if not name:  # Verifica se o nome está vazio
            messagebox.showerror("Erro", f"O nome do personagem no input {input_id} não pode estar vazio!")
            return

        try:
            self.controller.process_input(team, input_id, name)  # Passa o input ID para o controlador
        except ValueError as e:
            # Mostra uma mensagem de erro caso o personagem não seja encontrado
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

### O que foi corrigido:
1. **Problema de Closure**: A função `lambda` agora captura corretamente o valor de `input_entry` ao usar o argumento padrão `entry=input_entry`. Isso garante que cada input terá sua própria referência e não compartilhará a variável `name` com outros inputs.
   
2. **Referências Independentes**: Agora, ao pressionar "Enter" em qualquer input, ele usará o valor correto inserido naquele campo, e a janela será atualizada de forma independente para cada campo.

### Abordagem 2: Usar um Loop Separado

Se preferir, outra abordagem seria reestruturar o código para usar um loop separado para cada input, o que também resolveria o problema de closures. No entanto, a abordagem com **argumentos padrão no `lambda`** é mais simples e eficaz para o problema que você está enfrentando.

### Teste:
1. **Preencha qualquer campo** (por exemplo, o campo azul 1 ou o campo vermelho 2) e pressione "Enter". A imagem correspondente deverá aparecer na janela principal.
2. **Verifique se as imagens de outros inputs também aparecem corretamente** quando pressionar "Enter" em seus respectivos campos.

Isso deve resolver o problema de closure e garantir que cada input tenha seu comportamento independente. Se houver mais problemas ou algo não estiver funcionando como esperado, avise!

--------------

Perfeito! Agora vamos adicionar uma nova feature ao nosso programa, preciso de um novo input onde o usuário escreverá o nome do Mapa do jogo e a imagem do mapa deve aparecer no centro da tela, entre as imagens do time azul e do time vermelho, e acima do mapa deve aparecer o nome correspondente do mapa, tudo isso centralizado na tela

--------------

Ótimo! Agora vamos adicionar a funcionalidade de exibir a imagem do **mapa do jogo** no centro da tela, entre as imagens dos times azul e vermelho. Vamos também exibir o **nome do mapa** centralizado acima da imagem.

### Estrutura do Novo Input:
- Um novo **input** será adicionado para que o usuário possa inserir o nome do mapa.
- Quando o nome for inserido e o usuário pressionar "Enter", o programa buscará a imagem do mapa e a exibirá no **centro da janela**, com o nome do mapa **centralizado** acima da imagem.

### Passos:
1. Adicionar um **input** para o nome do mapa.
2. Exibir o **nome** e a **imagem** do mapa no centro da tela, entre as colunas dos times azul e vermelho.
3. Centralizar a exibição do nome e da imagem do mapa.

### Modificações no Código:

#### Passo 1: Modificar o `InputWindow` para Adicionar o Novo Input do Mapa

Vamos adicionar um campo de input para que o usuário insira o nome do mapa.

#### Modifique o Arquivo `input_window.py`:

```python
# app/input_window.py
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro

class InputWindow:
    def __init__(self):
        """
        Inicializa a janela de inputs com campos de texto para os dois times e o nome do mapa.
        Cada input é tratado de forma independente, com IDs únicos para identificar cada input.
        """
        self.root = tk.Tk()
        self.root.title("Seleção de Personagens e Mapa - Brawl Stars")

        self.inputs = []  # Lista que armazenará todos os inputs, com seus IDs

        # Input para o nome do mapa
        label = tk.Label(self.root, text="Nome do Mapa")
        label.pack()
        self.map_entry = tk.Entry(self.root)
        self.map_entry.bind("<Return>", lambda event: self.on_map_input(self.map_entry.get()))  # Lida com o input do mapa
        self.map_entry.pack()

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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
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
        Chama o controlador para processar o input do nome do mapa.
        :param map_name: Nome do mapa inserido no input
        """
        map_name = map_name.strip()  # Remove espaços em branco
        if not map_name:  # Verifica se o nome do mapa está vazio
            messagebox.showerror("Erro", "O nome do mapa não pode estar vazio!")
            return

        try:
            self.controller.process_map_input(map_name)  # Passa o nome do mapa para o controlador
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def run(self):
        """
        Inicia o loop principal da janela de inputs.
        """
        self.root.mainloop()
```

### Passo 2: Modificar o `Controller` para Processar o Nome do Mapa

Vamos garantir que o controlador consiga lidar com o input do mapa, buscar a imagem correta e passar para o **DisplayWindow**.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

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
        Processa o input do nome do mapa inserido pelo usuário.
        :param map_name: Nome do mapa inserido no input
        """
        # Busca o objeto Mapa através da API
        map_data = self.api_client.get_map_data(map_name)
        # Passa a URL da imagem do mapa e o nome do mapa para o display
        self.display_window.update_map(map_data.get_name(), map_data.get_image_url())
```

### Passo 3: Atualizar o `DisplayWindow` para Exibir o Nome e Imagem do Mapa

Agora, no `DisplayWindow`, precisamos exibir o nome e a imagem do mapa no centro da tela.

#### Modifique o Arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens e Mapa - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Manteremos as imagens referenciadas para não serem coletadas pelo garbage collector
        self.blue_team_images = {}
        self.red_team_images = {}

        # Adiciona elementos para o mapa
        self.map_label = None
        self.map_image_label = None

    def update_image(self, team, input_id, image_url):
        """
        Atualiza a janela com a imagem do personagem.
        Cada input é tratado de forma independente com base no seu ID único.
        :param team: Time azul ou vermelho
        :param input_id: ID único do input
        :param image_url: URL da imagem do personagem
        """
        # Faz o download da imagem a partir do URL (usando requests)
        image = self.download_image(image_url)
        
        # Converte a imagem para um formato compatível com Tkinter
        img_tk = ImageTk.PhotoImage(image)

        # Adiciona

 a imagem na coluna correta (esquerda para azul, direita para vermelho), usando o ID único
        if team == 'blue':
            if input_id not in self.blue_team_images:
                label = tk.Label(self.team_blue_frame, image=img_tk)
                label.image = img_tk  # Mantém a referência para não ser coletada pelo GC
                label.pack()  # Adiciona a imagem na próxima posição vertical no frame
                self.blue_team_images[input_id] = label  # Armazena para manter referência
        elif team == 'red':
            if input_id not in self.red_team_images:
                label = tk.Label(self.team_red_frame, image=img_tk)
                label.image = img_tk  # Mantém a referência
                label.pack()  # Adiciona a imagem na próxima posição vertical no frame
                self.red_team_images[input_id] = label

    def update_map(self, map_name, image_url):
        """
        Atualiza o mapa no centro da tela com o nome do mapa.
        :param map_name: Nome do mapa
        :param image_url: URL da imagem do mapa
        """
        # Se já existe um mapa exibido, removemos o anterior
        if self.map_label:
            self.map_label.destroy()
        if self.map_image_label:
            self.map_image_label.destroy()

        # Exibe o nome do mapa
        self.map_label = tk.Label(self.map_frame, text=map_name, font=("Arial", 16, "bold"))
        self.map_label.pack(pady=10)

        # Faz o download da imagem do mapa
        map_image = self.download_image(image_url)
        img_tk = ImageTk.PhotoImage(map_image)

        # Exibe a imagem do mapa
        self.map_image_label = tk.Label(self.map_frame, image=img_tk)
        self.map_image_label.image = img_tk  # Mantém a referência
        self.map_image_label.pack()

    def download_image(self, url):
        """
        Faz o download da imagem a partir de uma URL e retorna uma instância de PIL.Image.
        :param url: URL da imagem
        :return: Instância de PIL.Image
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que a requisição foi bem-sucedida
            image_data = BytesIO(response.content)  # Lê os dados da imagem
            return Image.open(image_data)  # Abre a imagem com o PIL
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar a imagem: {e}")
            # Retorna uma imagem padrão em caso de erro
            return Image.new("RGB", (300, 300), color=(255, 0, 0))
```

### Explicações:
1. **Input do Mapa**: Agora temos um input separado para o nome do mapa. Ao pressionar "Enter", o controlador processa o nome do mapa, busca a imagem e exibe no centro.
2. **Exibição do Nome e Imagem do Mapa**: O nome do mapa é exibido acima da imagem, ambos centralizados entre as colunas dos times azul e vermelho.
3. **Manutenção de Estado**: As referências para o mapa são mantidas e substituídas corretamente ao buscar novos mapas.

### Teste:
1. **Insira o nome de um mapa** no campo de texto para mapas e pressione "Enter". O nome e a imagem do mapa devem aparecer no centro da tela.
2. **Verifique se os times azul e vermelho continuam funcionando corretamente**.

Se houver mais alguma questão ou ajuste, fique à vontade para me avisar!

/////////////// 

Ótima ideia! Vamos adicionar a funcionalidade de exibir a imagem do **Mapa** ao centro da tela, entre os times azul e vermelho, e incluir o nome do mapa acima da imagem, tudo centralizado. Isso trará um elemento visual importante ao seu programa e tornará a interface mais interativa.

### Como Adicionar a Nova Feature:

- **Novo Input para o Mapa**: Adicionaremos um campo de texto onde o usuário pode escrever o nome do mapa.
- **Exibição do Mapa**: Quando o nome do mapa for submetido, o mapa correspondente será exibido ao centro da tela, entre as colunas de imagens dos times azul e vermelho.
- **Nome do Mapa Centralizado**: O nome do mapa será exibido logo acima da imagem, também centralizado.

### Passo 1: Modificar o `InputWindow` para Adicionar o Campo de Mapa

Vamos adicionar um novo input para o **Mapa** e garantir que, quando o nome do mapa for submetido, o controlador e a janela de exibição lidem com ele corretamente.

#### Modifique o Arquivo `input_window.py`:

```python
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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
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
        map_name = map_name.strip()  # Remove espaços em branco antes e depois do nome
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
```

### Explicações:
- **Novo Input para o Mapa**: Adicionamos um campo de texto para que o usuário insira o nome do mapa, além dos campos dos times. Quando o usuário pressionar "Enter", o controlador será chamado para processar o mapa.
- **on_map_input**: Esta função trata o evento quando o mapa é submetido, garantindo que o nome do mapa seja processado de forma independente dos inputs dos personagens.

### Passo 2: Modificar o Controlador para Processar o Mapa

Agora precisamos garantir que o controlador processe o nome do mapa corretamente e repasse a exibição para a janela principal.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

MAPS = {
    "gem grab": "https://cdn.brawlify.com/maps/gem-grab.png",  # Exemplo de URL para um mapa
    "brawl ball": "https://cdn.brawlify.com/maps/brawl-ball.png"
    # Adicione mais mapas conforme necessário
}

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
        :param map_name: Nome do mapa inserido
        """
        map_name = map_name.lower()  # Converter para minúsculas
        if map_name in MAPS:
            map_image_url = MAPS[map_name]
            # Atualiza a exibição com o mapa e o nome do mapa
            self.display_window.update_map(map_name, map_image_url)
        else:
            raise ValueError(f"Mapa '{map_name}' não encontrado.")
```

### Explicações:
- **Novo Dicionário de Mapas**: O dicionário `MAPS` armazena os nomes dos mapas e suas URLs de imagens.
- **Novo Método `process_map_input`**: Este método processa o input do mapa e passa as informações para a janela de exibição para serem exibidas.

### Passo 3: Atualizar a Exibição do Mapa na `DisplayWindow`

Agora, vamos modificar a janela de exibição para incluir a imagem do mapa e seu nome no centro da tela.

#### Modifique o Arquivo `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL

class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times
        e o mapa no centro da tela.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens e Mapa - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk

.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Frame central para o mapa
        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.TOP, pady=20)

        # Referências para as imagens
        self.blue_team_images = {}
        self.red_team_images = {}
        self.map_label = None
        self.map_name_label = None

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

    def update_map(self, map_name, map_image_url):
        """
        Atualiza a janela com a imagem do mapa e o nome do mapa.
        :param map_name: Nome do mapa
        :param map_image_url: URL da imagem do mapa
        """
        # Atualiza o nome do mapa
        if self.map_name_label is not None:
            self.map_name_label.destroy()
        self.map_name_label = tk.Label(self.map_frame, text=map_name, font=("Helvetica", 16))
        self.map_name_label.pack()

        # Atualiza a imagem do mapa
        if self.map_label is not None:
            self.map_label.destroy()

        map_image = self.download_image(map_image_url)
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
```

### Explicações:
- **Exibição Central do Mapa**: O mapa é exibido ao centro, com o nome do mapa acima da imagem.
- **Atualização do Mapa**: O método `update_map()` destrói o mapa e o nome anteriores (se houver) e exibe o novo mapa e nome.

### Teste Final

1. **Escreva o nome de um personagem em qualquer campo** e pressione "Enter". A imagem do personagem deverá aparecer na coluna correta.
2. **Escreva o nome de um mapa** (por exemplo, "gem grab") e pressione "Enter". O nome e a imagem do mapa deverão aparecer centralizados entre as colunas dos times.

Agora, sua aplicação está pronta para exibir tanto os personagens quanto o mapa de forma interativa e organizada!

--------------

Acredito que a melhor abordagem será utilizar o ID dos mapas, assim como fizemos com os Brawlers


------------

Ótima ideia! Seguir o mesmo padrão dos **Brawlers** usando os **IDs dos Mapas** vai manter a consistência e modularidade no seu projeto, além de facilitar a adição de novos mapas no futuro.

Vamos ajustar o código para que, ao invés de usar o nome do mapa, utilizemos os **IDs dos Mapas**, assim como foi feito para os personagens (Brawlers). Faremos as seguintes modificações:

### Passo 1: Criar um Dicionário de IDs para os Mapas

Assim como o dicionário `BRAWLER_IDS`, criaremos um dicionário `MAP_IDS` que mapeia o nome dos mapas para os seus IDs. O controlador então usará o ID para buscar as informações e a imagem do mapa.

### Passo 2: Modificar o Controlador para Usar IDs dos Mapas

O controlador processará o nome do mapa, buscará o ID correspondente, e usará esse ID para obter a imagem do mapa, assim como fizemos com os brawlers.

### Passo 3: Adicionar a Função de Exibição no `DisplayWindow`

Exibiremos o nome e a imagem do mapa no centro da tela, utilizando o ID para buscar a imagem correta.

### Implementação

#### Passo 1: Atualizar o `controller.py` com IDs dos Mapas

Vamos criar um dicionário `MAP_IDS` que armazena os IDs e URLs correspondentes aos mapas, e modificar o método `process_map_input` para lidar com isso.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

MAP_IDS = {
    "gem grab": 1,
    "brawl ball": 2,
    # Adicione mais mapas conforme necessário
}

MAP_IMAGES = {
    1: {
        "name": "Gem Grab",
        "image_url": "https://cdn.brawlify.com/maps/gem-grab.png"
    },
    2: {
        "name": "Brawl Ball",
        "image_url": "https://cdn.brawlify.com/maps/brawl-ball.png"
    },
    # Adicione mais mapas com seus IDs e URLs
}

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
        Processa o nome do mapa inserido pelo usuário, usa o ID para buscar a imagem do mapa.
        :param map_name: Nome do mapa inserido
        """
        map_name = map_name.lower()  # Converter para minúsculas
        if map_name in MAP_IDS:
            map_id = MAP_IDS[map_name]
            # Obter o nome e a URL da imagem a partir do ID
            map_data = MAP_IMAGES.get(map_id)
            if map_data:
                self.display_window.update_map(map_data["name"], map_data["image_url"])
            else:
                raise ValueError(f"Imagem do mapa '{map_name}' não encontrada.")
        else:
            raise ValueError(f"Mapa '{map_name}' não encontrado.")
```

### Explicações:
- **`MAP_IDS`**: Mapeia o nome do mapa para o ID correspondente.
- **`MAP_IMAGES`**: Mapeia o ID do mapa para os dados do mapa (nome e URL da imagem).
- **`process_map_input`**: Ao receber o nome do mapa, ele converte para o ID e, a partir desse ID, obtém a imagem e o nome para exibição.

#### Passo 2: Modificar o `InputWindow` para Submeter o Nome do Mapa

No arquivo `input_window.py`, garantimos que o input do mapa envie o nome para o controlador, que usará o ID correspondente.

#### Verifique o Código `input_window.py`:

```python
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
        name = name.strip()  # Remove espaços em branco antes e depois do nome
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
        map_name = map_name.strip()  # Remove espaços em branco antes e depois do nome
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
```

#### Passo 3: Atualizar a Exibição do Mapa em `DisplayWindow`

Agora, vamos garantir que o mapa e o nome sejam exibidos corretamente no centro da tela.

#### Verifique o Código `display_window.py`:

```python
# app/display_window.py
import tkinter as tk
from PIL import Image, ImageTk  # Para lidar com imagens
import requests
from io import BytesIO  # Para manipular a imagem baixada diretamente da URL



class DisplayWindow:
    def __init__(self):
        """
        Inicializa a janela de exibição que exibirá as imagens dos personagens dos dois times
        e o mapa no centro da tela.
        """
        self.root = tk.Toplevel()  # Cria uma nova janela separada
        self.root.title("Imagens dos Personagens e Mapa - Brawl Stars")

        # Inicializa containers para as imagens dos dois times, lado a lado
        self.team_blue_frame = tk.Frame(self.root)
        self.team_blue_frame.pack(side=tk.LEFT, padx=20)

        self.team_red_frame = tk.Frame(self.root)
        self.team_red_frame.pack(side=tk.RIGHT, padx=20)

        # Frame central para o mapa
        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.TOP, pady=20)

        # Referências para as imagens
        self.blue_team_images = {}
        self.red_team_images = {}
        self.map_label = None
        self.map_name_label = None

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

    def update_map(self, map_name, map_image_url):
        """
        Atualiza a janela com a imagem do mapa e o nome do mapa.
        :param map_name: Nome do mapa
        :param map_image_url: URL da imagem do mapa
        """
        # Atualiza o nome do mapa
        if self.map_name_label is not None:
            self.map_name_label.destroy()
        self.map_name_label = tk.Label(self.map_frame, text=map_name, font=("Helvetica", 16))
        self.map_name_label.pack()

        # Atualiza a imagem do mapa
        if self.map_label is not None:
            self.map_label.destroy()

        map_image = self.download_image(map_image_url)
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
```

### Explicações:
- **Nome e Imagem do Mapa**: O nome do mapa é exibido acima da imagem, que é centralizada na tela entre os times.
- **IDs dos Mapas**: Usamos o ID dos mapas para buscar as informações do nome e URL, garantindo consistência com a abordagem dos Brawlers.

### Teste Final:
1. **Escreva o nome de um personagem** e pressione "Enter" para ver se a imagem do personagem aparece corretamente.
2. **Escreva o nome de um mapa** (por exemplo, "gem grab") e veja se a imagem e o nome do mapa aparecem centralizados na tela.

Essa abordagem usando IDs dos mapas mantém o projeto consistente e modular!

---------

Erro ao baixar a imagem: 404 Client Error: Not Found for url: https://cdn.brawlify.com/maps/gem-grab.png

Acredito que o erro esteja sendo gerado por conta da falta de conhecimento da estrutura json que estamos utilziando, a estrutura disponibilizada na documentação da api é a seguinte:

De Mapas:

{
    "list": [
        {
            "id": 15000000,
            "new": false,
            "disabled": true,
            "name": "Temple Ruins",
            "hash": "Temple-Ruins",
            "version": 6,
            "link": "https://brawlify.com/maps/detail/Temple-Ruins",
            "imageUrl": "https://cdn-old.brawlify.com/map/Temple-Ruins.png?v=6",
            "credit": null,
            "environment": {
                "id": 42,
                "name": "DarrylsShip",
                "hash": "event_pirates_banner",
                "path": "Pirates",
                "version": 1,
                "imageUrl": "https://cdn-old.brawlify.com/environment/Pirates.png?v=1"
            },
            "gameMode": {
                "id": 1,
                "name": "Bounty",
                "hash": "Bounty",
                "version": 1,
                "color": "#10b2b7",
                "link": "https://brawlify.com/gamemodes/detail/Bounty",
                "imageUrl": "https://cdn-old.brawlify.com/gamemode/Bounty.png?v=1"
            },
            "lastActive": 1566180000,
            "dataUpdated": null
        }
    ]
}

De modos de jogo:

{
    "list": [
        {
            "id": 15,
            "name": "Hot Zone",
            "hash": "Hot-Zone",
            "disabled": false,
            "color": "#e33752",
            "version": 1,
            "title": "Control the Zones!",
            "tutorial": "Control the Hot Zones to win! Establish control and earn points by being inside a zone while keeping opponents out. When the time runs out, the team with the most points wins! Watch out for the double points in the final moments.",
            "description": "Control the Hot Zones!",
            "shortDescription": "Control the Zones!",
            "sort1": 16,
            "sort2": 16,
            "link": "https://brawlify.com/gamemodes/detail/Hot-Zone",
            "imageUrl": "https://cdn-old.brawlify.com/gamemode/Hot-Zone.png?v=1",
            "imageUrl2": "https://cdn-old.brawlify.com/gamemode/header/Hot-Zone.png?v=1"
        }
    ]
}

Nós precisamos exibir uma imagem pequena do modo de jogo com o nome do mapa escolhido acima da imagem retangular no centro da janela do mapa da partida selecionado, como por exemplo modo de jogo: brawl ball no mapa triple dribble, porém apenas escrevendo no input o nome do mapa, o software deve compreender que o modo de jogo é brawl ball.

-------

Entendi! Para resolver o problema, precisaremos modificar o código para lidar corretamente com a estrutura **JSON** que você forneceu. Além disso, quando o usuário insere o nome de um **mapa**, o software deve ser capaz de identificar o **modo de jogo** associado a esse mapa e exibir tanto a imagem do mapa quanto uma pequena imagem representando o **modo de jogo**.

### Estrutura Geral:
1. **Mapas**: Quando o nome de um mapa é inserido, precisamos buscar o mapa correspondente e obter a URL da imagem do mapa, assim como a do **modo de jogo** associado a esse mapa.
2. **Modos de Jogo**: Cada mapa possui um **modo de jogo** associado. Precisamos obter a imagem do modo de jogo para exibi-la acima da imagem do mapa.
3. **Inputs**: O usuário só precisa inserir o nome do mapa no input, e o software automaticamente entenderá o modo de jogo associado a esse mapa.

### Ajuste na Estrutura:
- Quando o nome de um mapa for submetido, a aplicação irá buscar o **ID do mapa**, sua **imagem**, e também o **modo de jogo** correspondente, exibindo ambos na janela.
- Utilizaremos as URLs **`imageUrl`** tanto do mapa quanto do **modo de jogo**.

### Passo 1: Modificar o Controlador para Processar Mapas e Modos de Jogo

Vamos começar modificando o **controlador** para lidar com a estrutura de **mapas** e **modos de jogo**. Utilizaremos os dados JSON para buscar as informações corretas.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

MAP_DATA = {
    # Exemplo de estrutura de mapas com ID e modo de jogo
    "temple ruins": {
        "id": 15000000,
        "map_image_url": "https://cdn-old.brawlify.com/map/Temple-Ruins.png?v=6",
        "game_mode": {
            "name": "Bounty",
            "image_url": "https://cdn-old.brawlify.com/gamemode/Bounty.png?v=1"
        }
    },
    # Adicione mais mapas conforme necessário
}

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

            # Atualiza a exibição com o nome do mapa, a imagem do mapa, o nome do modo de jogo, e a imagem do modo de jogo
            self.display_window.update_map(map_name, map_image_url, game_mode_name, game_mode_image_url)
        else:
            raise ValueError(f"Mapa '{map_name}' não encontrado.")
```

### Explicações:
1. **`MAP_DATA`**: Contém as informações sobre o mapa, como o ID do mapa, a URL da imagem do mapa, e os detalhes sobre o **modo de jogo** associado, incluindo o nome e a URL da imagem do modo de jogo.
2. **`process_map_input`**: Quando o nome do mapa é submetido, ele obtém o mapa e o **modo de jogo** associados, passando as informações para a janela de exibição.

### Passo 2: Atualizar o `DisplayWindow` para Exibir o Mapa e o Modo de Jogo

Agora, no arquivo **`display_window.py`**, vamos modificar a função `update_map` para exibir não apenas o nome e a imagem do mapa, mas também o nome e a imagem do **modo de jogo** associado.

#### Modifique o Arquivo `display_window.py`:

```python
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
        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.TOP, pady=20)

        # Referências para as imagens
        self.blue_team_images = {}
        self.red_team_images = {}
        self.map_label = None
        self.map_name_label = None
        self.game_mode_label = None
        self.game_mode_image_label = None

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

    def update_map(self, map_name, map_image_url, game_mode_name, game_mode_image_url):
        """
        Atualiza a janela com a imagem do mapa, o nome do mapa, o nome do modo de jogo e a imagem do modo de jogo.
        :param map_name: Nome do mapa
        :param map_image_url: URL da imagem do mapa
        :param game_mode_name: Nome do modo de jogo associado ao mapa
        :param game_mode_image_url: URL da imagem do modo de jogo associado ao mapa
        """
        # Atualiza o nome do mapa
        if self.map_name_label is not None:
            self.map_name_label.destroy()
        self.map_name_label = tk.Label(self.map_frame, text=map_name, font=("Helvetica", 16))
        self.map_name_label.pack()

        # Atualiza a imagem do mapa
        if self.map_label is not None:
            self.map_label.destroy()

        map_image = self.download_image(map_image_url)
        map_img_tk = ImageTk.PhotoImage(map_image)
        self.map_label = tk.Label(self.map_frame, image=map_img_tk)
        self.map_label.image = map_img_tk
        self.map_label.pack()

        # Atualiza o nome e a imagem do modo de jogo
        if self.game_mode_label is not None:
            self.game_mode_label.destroy()
        self.game_mode_label = tk.Label(self.map_frame, text=game_mode_name, font=("Helvetica", 12))
        self.game_mode_label.pack()

        if self.game_mode_image_label is not None:
            self.game_mode_image_label.destroy()

        game_mode_image = self.download_image(game_mode_image_url)
        game_mode_img_tk = ImageTk.PhotoImage(game_mode_image)
        self.game_mode_image_label = tk.Label(self.map_frame, image=game_mode_img_tk)
        self.game_mode_image_label.image = game_mode_img_tk
        self.game_mode_image_label.pack()

    def

 download_image(self, url):
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
```

### Explicações:
- **Exibição Central do Modo de Jogo e Mapa**: Agora, exibimos tanto o nome e a imagem do **modo de jogo** quanto o **nome e a imagem do mapa**. Ambos são centralizados na tela.
- **`update_map`**: Atualiza a janela com as informações do mapa e do modo de jogo, destrói os elementos anteriores, se houver, e exibe as novas informações.

### Teste Final:
1. **Escreva o nome de um mapa** (como "temple ruins") e pressione "Enter". O nome e a imagem do **mapa** devem aparecer, junto com o nome e a imagem do **modo de jogo** associado.
2. Verifique se as imagens são exibidas corretamente e de forma centralizada na tela.

Isso deve corrigir os problemas de busca de mapas e modos de jogo, garantindo que tudo seja exibido corretamente com base nos dados JSON fornecidos!

------------

Substitua a lógica utilziando url para utilizar apenas id's, assim como estamos fazendo com os brawlers, o erro de requisição persiste por não encontrar a url


-----------

Entendido! Vamos substituir o uso de URLs diretamente por **IDs**, da mesma forma como fizos para os **Brawlers**. Ao invés de usar URLs fixas, utilizaremos os **IDs dos Mapas** e **IDs dos Modos de Jogo** para buscar as informações corretas de forma mais flexível e confiável, sem depender de URLs externas que possam mudar.

### Estrutura a ser Implementada:
1. **Mapa**: Quando o usuário inserir o nome do mapa, o sistema identificará o **ID do Mapa** e o **ID do Modo de Jogo** correspondente.
2. **Modo de Jogo**: Utilizaremos o **ID do Modo de Jogo** associado ao mapa para buscar sua respectiva imagem e nome.
3. **Exibição**: A exibição será atualizada com base nos **IDs** e **imagens** recuperadas a partir das respostas da API.

### Atualizando o Sistema para Usar IDs

#### Passo 1: Atualizar o Controlador para Usar IDs de Mapas e Modos de Jogo

Vamos modificar o **controlador** para buscar as informações com base nos **IDs** dos mapas e modos de jogo, conforme a estrutura JSON que você forneceu. Os dados do mapa serão mapeados a partir dos seus **IDs** e suas imagens serão processadas a partir desses IDs.

#### Modifique o Arquivo `controller.py`:

```python
# app/controller.py

BRAWLER_IDS = {
    "colt": 16000001,
    "surge": 16000038,
    # Adicione mais brawlers conforme necessário
}

MAP_DATA = {
    "temple ruins": {
        "id": 15000000,
        "game_mode_id": 1  # ID do modo de jogo associado
    },
    "triple dribble": {
        "id": 15000001,
        "game_mode_id": 2  # Exemplo de um modo de jogo para "Triple Dribble"
    },
    # Adicione mais mapas conforme necessário
}

GAME_MODES = {
    1: {
        "name": "Bounty",
        "image_id": 1  # ID da imagem correspondente ao modo de jogo
    },
    2: {
        "name": "Brawl Ball",
        "image_id": 2  # ID da imagem correspondente ao modo de jogo
    },
    # Adicione mais modos de jogo conforme necessário
}

MAP_IMAGES = {
    15000000: "https://cdn-old.brawlify.com/map/Temple-Ruins.png?v=6",  # Exemplo de URL de imagem para um mapa
    15000001: "https://cdn-old.brawlify.com/map/Triple-Dribble.png?v=6",
    # Adicione mais URLs de imagem para mapas conforme necessário
}

GAME_MODE_IMAGES = {
    1: "https://cdn-old.brawlify.com/gamemode/Bounty.png?v=1",  # Exemplo de URL de imagem para o modo de jogo Bounty
    2: "https://cdn-old.brawlify.com/gamemode/Brawl-Ball.png?v=1",
    # Adicione mais URLs de imagem para modos de jogo conforme necessário
}

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
        Utiliza os IDs do mapa e do modo de jogo para buscar as imagens corretas.
        :param map_name: Nome do mapa inserido
        """
        map_name = map_name.lower()  # Converter para minúsculas
        if map_name in MAP_DATA:
            # Obter o ID do mapa e do modo de jogo
            map_id = MAP_DATA[map_name]["id"]
            game_mode_id = MAP_DATA[map_name]["game_mode_id"]

            # Buscar as URLs das imagens com base nos IDs
            map_image_url = MAP_IMAGES.get(map_id)
            game_mode_data = GAME_MODES.get(game_mode_id)
            game_mode_name = game_mode_data["name"]
            game_mode_image_url = GAME_MODE_IMAGES.get(game_mode_data["image_id"])

            if map_image_url and game_mode_image_url:
                # Atualizar a exibição com os dados do mapa e do modo de jogo
                self.display_window.update_map(map_name, map_image_url, game_mode_name, game_mode_image_url)
            else:
                raise ValueError(f"Imagens para o mapa ou modo de jogo '{map_name}' não foram encontradas.")
        else:
            raise ValueError(f"Mapa '{map_name}' não encontrado.")
```

### Explicações:
1. **`MAP_DATA`**: Cada mapa agora está associado a um **ID de Mapa** e um **ID de Modo de Jogo**. Utilizamos esses IDs para buscar as informações corretas sobre o mapa e o modo de jogo.
2. **`MAP_IMAGES`**: Mapeia os **IDs dos Mapas** para suas respectivas URLs de imagem.
3. **`GAME_MODES`**: Armazena as informações dos modos de jogo, associando os IDs com os nomes e IDs das imagens.
4. **`GAME_MODE_IMAGES`**: Mapeia os **IDs dos Modos de Jogo** para suas respectivas URLs de imagem.
5. **`process_map_input`**: Quando o usuário insere o nome do mapa, buscamos os IDs do mapa e do modo de jogo e utilizamos esses IDs para buscar as imagens e informações corretas.

### Passo 2: Modificar a `DisplayWindow` para Exibir as Imagens com Base nos IDs

Agora, o arquivo `display_window.py` precisa exibir as imagens do mapa e do modo de jogo com base nos **IDs** processados.

#### Verifique o Arquivo `display_window.py`:

```python
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
        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.TOP, pady=20)

        # Referências para as imagens
        self.blue_team_images = {}
        self.red_team_images = {}
        self.map_label = None
        self.map_name_label = None
        self.game_mode_label = None
        self.game_mode_image_label = None

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

    def update_map(self, map_name, map_image_url, game_mode_name, game_mode_image_url):
        """
        Atualiza a janela com a imagem do mapa, o nome do mapa, o nome do modo de jogo e a imagem do modo de jogo.
        :param map_name: Nome do mapa
        :param map_image_url: URL da imagem do mapa
        :param game_mode_name: Nome do modo de
        """
```
---------

Eu consegui concertar a lógica dos mapas da forma anterior, apenas a url estava escrita da forma incorreta, estamos utilizando a estrutura:

MAP_DATA = {
    # Exemplo de estrutura de mapas com ID e modo de jogo
    "temple ruins": {
        "id": 15000000,
        "map_image_url": "https://cdn.brawlify.com/maps/regular/15000000.png",
        "game_mode": {
            "name": "Bounty",
            "image_url": "https://cdn-old.brawlify.com/gamemode/Bounty.png?v=1"
        }
    },
    # Adicione mais mapas conforme necessário
}

Está tudo funcionando corretamente, porém eu acho inviável deixar os Brawlers e Mapa nesse scprit, eles precisarão de scripts individuais que serão acessados pelo controller, pois o arquivo aumentará demasiadamente.
Como podemos fazer de forma que tudo continue funcionando corretamente?

-------------