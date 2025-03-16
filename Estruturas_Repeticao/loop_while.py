"""

Loop while

Forma geral

while expressão_booleana:
     //execução do loop

O bloco do while será repetido enquanto a expressão booleana
for verdadeira.

Exemplo:

num = 5
num < 5

"""
#Exemplo 1
#loop infinito
numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1

#Obs.: em um loop while, é importante que cuidemos do critério
#de parada para não causar um loop infinito.

#Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou, Jéssica? ')

