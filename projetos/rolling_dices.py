inicio = True
while inicio:
    lados = int(input("how many sides you want in your dice? "))
    dado = __import__('random').randint(1, lados)
    print("\nrolling dices... ")
    print(f"your dice number is {dado}\n")
    choice = input("you want to roll the dices again ? (y/n) ").lower()
    if choice == "n":
        print("thank you for rolling with us :)")
        break