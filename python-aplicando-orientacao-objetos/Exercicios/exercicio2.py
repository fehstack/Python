class Musicas:
    """
    Classe que representa uma coleção de músicas.

    Atributos de classe:
    - musicas (list): Uma lista para armazenar todas as instâncias de músicas.
    - nome (str): O nome da música.
    - artista (str): O nome do artista ou banda.
    - duracao (int): A duração da música em segundos.

    Métodos:
    - __init__(nome, artista, duracao): Método construtor da classe Musicas, inicializa os atributos nome, artista e duracao para cada instância.
    - listarMusicas(): Método estático que lista todas as músicas cadastradas, mostrando seus nomes, artistas e durações.
    """

    musicas = []  # Lista para armazenar todas as músicas

    def __init__(self, nome, artista, duracao):
        """
        Método construtor da classe Musicas.

        Parâmetros:
        - nome (str): O nome da música.
        - artista (str): O nome do artista ou banda.
        - duracao (int): A duração da música em segundos.
        """
        self.nome = str(nome)
        self.artista = str(artista)
        self.duracao = int(duracao)

        # Adiciona a instância atual (self) à lista de músicas da classe Musicas.

        Musicas.musicas.append(self)

    @staticmethod
    def listarMusicas():
        """
        Método estático para listar todas as músicas cadastradas.
        """
        for musica in Musicas.musicas:
            print(f'{musica.nome}, {musica.artista}, {musica.duracao}')


musica1 = Musicas('Felipe Ret', "Ret", 250)


Musicas.listarMusicas()
