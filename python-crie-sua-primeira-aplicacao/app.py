import os

restaurantes = [{"Nome": "PizzaHut","Categoria" : "Pizza","Telefone" : "11978477931","Ativo":True},
                {"Nome": "Dominus","Categoria" : "Pizza","Telefone": "11978477932","Ativo":False},
                {"Nome": "1900","Categoria" : "Pizza","Telefone" : "11978477933","Ativo":True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def voltarAoMenu():
    input('\nDigite uma tecla para voltar ao menu principal...')
    os.system('cls')
    main()

def exibirSubTitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status de restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')
    
def opcao_invalida():
    print("\nOpção invalida!\n")
    voltarAoMenu()

def cadastrarRestaurante():
    exibirSubTitulo("Bem vindo a tela de cadastro!\n")
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {"Nome":nome_restaurante, "Categoria":categoria_restaurante, "Ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltarAoMenu()
    
def listarRestaurante():
    exibirSubTitulo("Listando restaurantes\n")
    
    # l.just serve para padronizar o tamanho que sera imprimido.
    
    print(f'{'| Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status |\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f'| {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltarAoMenu()

def alterarStatus():
    exibirSubTitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            
            # O not tem a função de alterar de true para false ou vice e versa, ou seja se o status do ativo era True, apos adicionar o not será False.
            
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante["Ativo"] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    
    voltarAoMenu()
    
def escolher_opcao(): 
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)]
        
        if opcao_escolhida == 1: 
            cadastrarRestaurante()

        elif opcao_escolhida == 2: 
            listarRestaurante()

        elif opcao_escolhida == 3: 
            alterarStatus()

        elif opcao_escolhida == 4:
            print("Finalizar app")
            finalizar_app()
        else: 
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
