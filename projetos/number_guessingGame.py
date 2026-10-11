numero = int(__import__('random').randint(1,9))
entrada=int(input("adivinhe o número entre 1 e 9: "))
if entrada==numero:
    print("você acertou")
else:
    print("quase lá")
    entrada2=int(input("tente de novo: "))
    if entrada2==numero:
        print("parabéns")
    else:
        print("errou de novo")
        entrada3=int(input("tente mais uma vez: "))
        if entrada3==numero:
            print("parabéns")
        else:
            print("errou de novo, tá dificil?")
            entrada4=int(input("tente de novo: "))
            if entrada4==numero:
                print("parabéns")
            else:
                print("por pouco, o número era:" ,numero)