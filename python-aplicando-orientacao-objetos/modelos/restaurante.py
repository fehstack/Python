from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Classe que representa um restaurante.

    Atributos:
    - nome (str): O nome do restaurante.
    - categoria (str): A categoria do restaurante (por exemplo, Gourmet, FastFood, etc.).
    - ativo (bool): Indica se o restaurante está ativo ou não.

    Métodos:
    - __init__(nome, categoria): Método construtor da classe Restaurante, inicializa os atributos nome, categoria e ativo.
    - __str__(): Retorna uma representação em string do restaurante no formato 'nome | categoria'.
    - listar_restaurantes(): Método estático que lista todos os restaurantes cadastrados, mostrando seus nomes, categorias e estado de atividade.
    """

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Método construtor da classe Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = [] 
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Retorna uma representação em string do restaurante no formato 'nome | categoria'.
        """
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes cadastrados, mostrando seus nomes, categorias e estado de atividade.
        """
        print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliacao".ljust(20)} | {"Ativo".ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}')
                                                                                           
    @property
    def ativo(self):
        """
        Retorna o estado de atividade do restaurante como uma string ('Verdadeiro' ou 'Falso').
        """
        return 'Verdadeiro' if self._ativo else 'Falso'
    
    def alternarEstados(self):
        self._ativo = not self._ativo 
        
    def receberAvaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    
    @property   
    def media_avaliacoes(self):
        if not self._avaliacao:
            return f'Sem nota'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media

    