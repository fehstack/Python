class Restaurante:
    """
    Classe que representa um restaurante.

    Atributos de Classe:
    - restaurantes (list): Uma lista para armazenar todas as instâncias de restaurantes.

    Métodos Estáticos:
    - listar_restaurantes(): Lista todos os restaurantes cadastrados.

    Métodos de Instância:
    - __init__(nome, categoria, endereco, numero_restaurante, ativo=False): Método construtor da classe Restaurante.
        - Parâmetros:
            - nome (str): O nome do restaurante.
            - categoria (str): A categoria do restaurante.
            - endereco (str): O endereço do restaurante.
            - numero_restaurante (int): O número do restaurante.
            - ativo (bool, opcional): Indica se o restaurante está ativo ou não. Por padrão, é False.

    - cadastrarRestaurante(): Permite ao usuário cadastrar um novo restaurante.
    """

    restaurantes = []

    def __init__(self, nome, categoria, endereco, numero_restaurante, ativo=False):
        """
        Método construtor da classe Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        - endereco (str): O endereço do restaurante.
        - numero_restaurante (int): O número do restaurante.
        - ativo (bool, opcional): Indica se o restaurante está ativo ou não. Por padrão, é False.
        """
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.numero_restaurante = numero_restaurante
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    @staticmethod
    def listar_restaurantes():
        """
        Lista todos os restaurantes cadastrados.
        """
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome}, Categoria: {restaurante.categoria}, Endereco: {restaurante.endereco}, '
                  f'Numero: {restaurante.numero_restaurante}, Ativo: {restaurante.ativo}')

    @staticmethod
    def cadastrarRestaurante():
        """
        Permite ao usuário cadastrar um novo restaurante.
        """
        print("Digite as informações do restaurante")
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        endereco = input("Endereço: ")
        numero = input("Numero: ")

        restaurante = Restaurante(nome, categoria, endereco, numero)
        Restaurante.restaurantes.append(restaurante)


# Exemplo de uso:
Restaurante.cadastrarRestaurante()
Restaurante.listar_restaurantes()
