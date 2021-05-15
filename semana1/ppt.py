import random 

def run():
    menu="""
    Bienvenido a Piedra, Papel o Tijera

    Tu eres el Jugador 1, puedes escoger:
    Piedra
    Papel
    Tijera

    Escribe la opción que seleccionaste: """

    opcion= input(menu)

    jugador_2= random.choice (['Piedra', 'Papel', 'Tijera'])

    if opcion == 'Piedra':
        if jugador_2 == 'Piedra':
            print('Es empate, Jugador 2 escoge Piedra')
        elif jugador_2 == 'Papel':
            print('Perdiste, Jugador 2 escoge Papel')
        else:
            print('Ganaste, Jugador 2 escoge Tijera')
    elif opcion == 'Papel':
        if jugador_2 == 'Piedra':
            print('Ganaste, Jugador 2 escoge Piedra')
        elif jugador_2 == 'Papel':
            print('Es empate, Jugador 2 escoge Papel')
        else:
            print('Perdiste, Jugador 2 escoge Tijera')
    else:
        if jugador_2 == 'Piedra':
            print('Perdiste, Jugador 2 escoge Piedra')
        elif jugador_2 == 'Papel':
            print('Ganaste, Jugador 2 escoge Papel')
        else:
            print('Es empate, Jugador 2 escoge Tijera')                     




if __name__ == '__main__':
    run()