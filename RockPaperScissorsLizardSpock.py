# Piedra, papel, tijeras, lagarto, Spock #

"""
Reglas:
- Tijera corta a papel
- Papel tapa a piedra
- Piedra aplasta a lagarto
- Lagarto envenena a Spock
- Spock rompe a tijera
- Tijera decapita a lagarto
- Lagarto devora a papel
- Papel desautoriza a Spock
- Spock vaporiza a piedra
- Piedra aplasta a tijera
"""

import random    # Para selección aleatoria del ordenador


all_options = ["piedra", "papel", "tijera", "lagarto", "spock"]

partida = input("¿Jugamos? <y/n>: ")

u = 0   # Victorias usuario
c = 0   # Victorias computadora

while partida == "y":
    print(f"\nLas opciones son: {all_options}")

    user = input("¿Qué eliges?: ")

    computer = random.choice(all_options)


    if user == computer:
        print("EMPATE!")

    elif user == "tijera" and computer == "papel":
        u = u + 1
        print("Tijera corta a papel. Tú ganas!")

    elif user == "papel" and computer == "piedra":
        u = u + 1
        print("Papel tapa a piedra. Tú ganas!")

    elif user == "piedra" and computer == "lagarto":
        u = u + 1
        print("Piedra aplasta a lagarto. Tú ganas!")

    elif user == "lagarto" and computer == "spock":
        u = u + 1
        print("Lagarto envenena a Spock. Tú ganas!")

    elif user == "spock" and computer == "tijera":
        u = u + 1
        print("Spock rompe a tijera. Tú ganas!")

    elif user == "tijera" and computer == "lagarto":
        u = u + 1
        print("Tijera decapita a lagarto. Tú ganas!")

    elif user == "lagarto" and computer == "papel":
        u = u + 1
        print("Lagarto devora a papel. Tú ganas!")

    elif user == "papel" and computer == "spock":
        u = u + 1
        print("Papel desautoriza a Spock. Tú ganas!")

    elif user == "spock" and computer == "piedra":
        u = u + 1
        print("Spock vaporiza a piedra. Tú ganas!")

    elif user == "piedra" and computer == "tijera":
        u = u + 1
        print("Piedra aplasta a tijera. Tú ganas!")

    elif computer == "tijera" and user == "papel":
        c = c + 1
        print("Tijera corta a papel. Perdiste :c")

    elif computer == "papel" and user == "piedra":
        c = c + 1
        print("Papel tapa a piedra. Perdiste :c")

    elif computer == "piedra" and user == "lagarto":
        c = c + 1
        print("Piedra aplasta a lagarto. Perdiste :c")

    elif computer == "lagarto" and user == "spock":
        c = c + 1
        print("Lagarto envenena a Spock. Perdiste :c")

    elif computer == "spock" and user == "tijera":
        c = c + 1
        print("Spock rompe a tijera. Perdiste :c")

    elif computer == "tijera" and user == "lagarto":
        c = c + 1
        print("Tijera decapita a lagarto. Perdiste :c")

    elif computer == "lagarto" and user == "papel":
        c = c + 1
        print("Lagarto devora a papel. Perdiste :c")

    elif computer == "papel" and user == "spock":
        c = c + 1
        print("Papel desautoriza a Spock. Perdiste :c")

    elif computer == "spock" and user == "piedra":
        c = c + 1
        print("Spock vaporiza a piedra. Perdiste :c")

    elif computer == "piedra" and user == "tijera":
        c = c + 1
        print("Piedra aplasta a tijera. Perdiste :c")

    else:
        print("Algo salió mal")

    print(f"\n Has ganado {u} veces.")
    print(f"\n Has perdido {c} veces.")

    partida = input("¿Otra vez? <y/n>: ")
