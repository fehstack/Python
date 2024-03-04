from modelos.restaurante import Restaurante

from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receberAvaliacao('Gui', 10)
restaurante_praca.receberAvaliacao('Lais', 8)
restaurante_praca.receberAvaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
