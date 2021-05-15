def run():
    radio= int(input('Cual es el radio de tu cilindro: '))
    altura= int(input('Cual es la altura de tu cilindro: '))
    volumen= 3.1416*(radio**2)*altura
    print(f'El volumen de tu cilindri es {volumen}')




if __name__ == '__main__':
    run()