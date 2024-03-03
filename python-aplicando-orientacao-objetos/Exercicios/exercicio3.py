#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.

#Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro():

    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = str(modelo)
        self.cor = str(cor)
        self.ano = int(ano)
        Carro.carros.append(self)

    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo}, {carro.cor}, {carro.ano}')


carro1 = Carro('AMG63', 'Vermelho', 2020)

Carro.listar_carros()