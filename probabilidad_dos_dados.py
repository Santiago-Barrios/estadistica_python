import random

def tirar_dado(numero_de_tiros):

    secuancia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro1 = random.choice([1,2,3,4,5,6])
        tiro2 = random.choice([1,2,3,4,5,6])
        resultado = tiro1 + tiro2
        secuancia_de_tiros.append(resultado)

    return secuancia_de_tiros


def main(numero_de_tiros, numero_de_intentos):

    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12 += 1
    

    probabilidad_de_tiros_con_12 = tiros_con_12 / numero_de_intentos
    print(f'Probabilidad de obtener un 12 con 2 dados en {numero_de_tiros} tiros es igual a {probabilidad_de_tiros_con_12} ')


def run():
    numero_de_tiros = int(input('Cuantos tiros del dado deseas: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulación: '))

    main(numero_de_tiros, numero_de_intentos)

if __name__ == '__main__':
    run()