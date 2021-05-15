def run():
    MILLA= 1.609344
    KILOMETRO= 0.621371

    menu= """
    Hola, que deseas convertir

    1 - Millas a Kilometros
    2 - Kilometros a Millas

    Elige una opcion: """

    opcion= int(input(menu))

    if opcion == 1:
        cantidad_milla= int(input('Cual es la cantidad de millas: '))
        conversor_milla_kilometro= cantidad_milla*MILLA
        print(f'La cantidad de kilometros es {conversor_milla_kilometro}')
    else:
        cantidad_kilometro= int(input('Cual es la cantidad de kilometros: '))
        conversor_kilometro_milla= cantidad_kilometro*KILOMETRO
        print(f'La cantidad de millas es {conversor_kilometro_milla}')



if __name__=='__main__':
    run()
