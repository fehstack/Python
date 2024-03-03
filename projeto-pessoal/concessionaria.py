import nt
import os

# Lista de carros
carros = [] #=[{"Nome": "AMG63", "Categoria": "Esportivo", "Ativo": True}]

def subtitulo(texto):
    """
    Limpa a tela e exibe o texto como um subtítulo.

    Args:
        texto (str): Texto a ser exibido como subtítulo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    
def voltarAoMenu():
    """
    Exibe uma mensagem para voltar ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu principal...')
    main()
    
def finalizar_app():
    """
    Finaliza o aplicativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o app')
    quit()

def letreiro():
    """
    Exibe um letreiro na tela.
    """
    print("""
██████╗░███████╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██╔════╝████╗░████║██╔══██╗████╗░██║██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
██║░░██║█████╗░░██╔████╔██║██║░░██║██╔██╗██║███████║██║░░░██║░░░██║░░░██║░░██║
██║░░██║██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║██╔══██║██║░░░██║░░░██║░░░██║░░██║
██████╔╝███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░""")
    
def exibirOpcoes():
    """
    Exibe as opções do menu principal.
    """
    print("\n-BEM VINDO A TELA INICIAL-\n")
    print("1. Cadastrar Veiculo")
    print("2. Listar veiculos")
    print("3. Dar baixa")
    print("4. Encerrar programa\n")
    
def escolher_opcao():
    """
    Solicita ao usuário que escolha uma opção e executa a função correspondente.
    """
    opcaoEscolhida = input("Escolha a opção desejada: ")
    
    if opcaoEscolhida == "1":
        cadastroVeiculo()
    elif opcaoEscolhida == "2":
        listarVeiculos()
    elif opcaoEscolhida == "3":
        baixaVeiculos()
    elif opcaoEscolhida == "4":
        finalizar_app()
    else:
        print("\nOpção invalida, tente novamnte.\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        voltarAoMenu()

def cadastroVeiculo():
    """
    Permite ao usuário cadastrar um novo veículo.
    """
    subtitulo("BEM VINDO A TELA DE CADASTRO\n")
    
    nomeVeiculo = input("Nome: ")
    categoriaVeiculo = input(f"Categoria do {nomeVeiculo}: ")
    
    # Formata os dados do carro e os adiciona à lista de carros
    dadosCarro = {"Nome": nomeVeiculo, "Categoria": categoriaVeiculo, "Ativo": False}
    carros.append(dadosCarro)
    print(f"O carro {nomeVeiculo} foi cadastrado com sucesso!")
    voltarAoMenu()
    
    
def listarVeiculos():
    """
    Lista todos os veículos cadastrados.
    """
    subtitulo("LISTANDO CARROS... \n")
    
    print(f'{"| Nome do carro".ljust(22)} | {"Categoria".ljust(20)} | {"Ativo".ljust(10)} |\n')
    
    for carro in carros:
        # Acessa as informações de cada carro e as imprime na tela
        nomeVeiculo = carro["Nome"]
        categoriaVeiculo = carro["Categoria"]
        veiculoAtivo = "Ativado" if carro["Ativo"] else "Desativado"
        print(f'| {nomeVeiculo.ljust(20)} | {categoriaVeiculo.ljust(20)} | {veiculoAtivo.ljust(10)} |')
    voltarAoMenu()

def baixaVeiculos():
    """
    Permite ao usuário dar baixa em um veículo.
    """
    subtitulo("\n-PLATAFORMA DE BAIXA VEICULAR-\n")
    
    carroDesejado = input("Digite o carro que deseja dar baixa: ")
    carroEncontrado = False
    
    for carro in carros:
        if carroDesejado == carro["Nome"]:
            carroEncontrado = True
            carro["Ativo"] = not carro["Ativo"]
            mensagem = f"O carro {carroDesejado} foi ativado com sucesso" if carro["Ativo"] else f"O carro {carroDesejado} foi desativado com sucesso"
            print(mensagem)
            break  # Sai do loop assim que encontrar o veículo desejado
    
    if not carroEncontrado:
        print("O carro não foi encontrado na lista para baixa.")
            
    voltarAoMenu()

            
        
    voltarAoMenu()

def main():
    """
    Função principal do programa.
    """
    letreiro()
    exibirOpcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
