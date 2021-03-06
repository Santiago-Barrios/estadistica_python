import random
import math


def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)
    acumulador = 0

    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)

def desviacion_estandar(X):
    var = varianza(X)
    return math.sqrt(var)


if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range (20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)
    print(X)
    print(f'la media del arreglo es = {mu} \nsu varianza = {Var} \ndesviacion_estandar = {sigma}  ')