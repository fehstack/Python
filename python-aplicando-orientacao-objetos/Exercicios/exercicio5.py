class Pessoa:
    """
    Classe que representa uma pessoa.

    Atributos:
    - nome (str): O nome da pessoa.
    - idade (int): A idade da pessoa.
    - profissao (str): A profissão da pessoa.

    Métodos:
    - __init__(nome, idade, profissao): Método construtor da classe Pessoa, inicializa os atributos nome, idade e profissao.
    - __str__(): Método especial que retorna uma representação em string da pessoa.
    - aniversario(): Método de instância que aumenta a idade da pessoa em um ano.
    - saudacao: Propriedade que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
    """

    def __init__(self, nome, idade, profissao):
        """
        Método construtor da classe Pessoa.

        Parâmetros:
        - nome (str): O nome da pessoa.
        - idade (int): A idade da pessoa.
        - profissao (str): A profissão da pessoa.
        """
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        """
        Retorna uma representação em string da pessoa.
        """
        return f'{self.nome}, {self.idade}, {self.profissao}'

    def aniversario(self):
        """
        Aumenta a idade da pessoa em um ano.
        """
        self.idade += 1

    @property
    def saudacao(self):
        """
        Retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
        """
        return f'Bem-vindo, profissional de {self.profissao}!'


# Exemplo de uso:
usuario = Pessoa("Felipe", 15, "EDF")
print(usuario)  
usuario.aniversario()
print(usuario)  
print(usuario.saudacao)  
