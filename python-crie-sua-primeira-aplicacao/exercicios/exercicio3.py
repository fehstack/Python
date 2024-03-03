def exercicio3():
    minhaSenha = "Felipe123"
    meuUsuario = "Santiago"

    usuario = input("Digite seu usuario: ")
    senhaUsuario = input("Digite sua senha:")

    if usuario != meuUsuario:
        print("Usuario incorreto, tente novamente.")
        exercicio3()
    elif senhaUsuario != minhaSenha:
        print("Senha Incorreta, tente novamente.")
        exercicio3()
    else: print("Bem vindo a plataforma!")
    exercicio3()
    
exercicio3()