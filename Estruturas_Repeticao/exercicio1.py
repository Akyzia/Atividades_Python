"""
Exercicio 1
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""

#Exercicio 1
contador = int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f'O numero {indice} eh multiplo de 3.')
        contador = contador + 1
    indice = indice + 1

