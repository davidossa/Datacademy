def run():
    base= int(input('Cual es la base de tu triangulo: '))
    altura= int(input('Cual es la altura de tu triangulo: '))
    area= (base*altura)/2
    isosceles= (((base/2)**2)+(altura**2))**0.5
    area_isosceles= (base*((isosceles**2)-((base**2)/4))**0.5)/2

    if base == altura:
        print(f'El area de tu triangulo equilatero es {area}')
    elif area == area_isosceles:
        print(f'El area de tu triaungulo isosceles es {area}')
    else:
        print(f'El area de tu triangulo escaleno es {area}')        


if __name__== '__main__':
    run()

