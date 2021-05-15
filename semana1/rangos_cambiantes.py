def run():
    numero1= int(input('Ingresa el numero mas bajo: '))
    numero2= int(input('Ingresa el numero mas alto: '))
    numero3= int(input('Ingresa el numero de comparacion: '))

    if numero3 > numero1 and numero3 < numero2:
        print(f'El numero de comparacion {numero3} esta en el rango')
    elif numero3 < numero1:
        print(f'El numero de comparacion {numero3} esta por debajo del rango')
    elif numero3 > numero2:
        print(f'El numero de comparacion {numero3} esta por encima del rango')



if __name__ == '__main__':
    run()