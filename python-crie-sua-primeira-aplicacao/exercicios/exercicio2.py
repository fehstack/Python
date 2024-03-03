def exercicio2():
    
    idade = int(input("Digite sua idade: "))

    if idade <= 12:
        print("Você é criança")
        exercicio2()
    elif idade >= 13 and idade <= 18:
        print("Você é adolescente")
        exercicio2()
    elif idade >= 20 and idade <= 60:
        print("Você é adulto")
    else: print("Você é idoso")
    exercicio2()
    
exercicio2()