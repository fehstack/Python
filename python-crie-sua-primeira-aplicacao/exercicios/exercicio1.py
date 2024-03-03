def exercicio1():
    
    numero = float(input("Digite um numero de 1 a 10: "))

    if numero%2 == 0:
        print("O numero é par!")
        exercicio1()
    else: print("O numero é impar")
    exercicio1()
    
exercicio1()