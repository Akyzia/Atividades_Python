
"""
Estruturas de repetição

Loop -> Estrutura de repetição
For  -> Uma dessas estruturas

"""

"""

A estrutura For funciona tanto em C quanto no Java

for(int i = 0: i < 10: i++){
   //execução do loop
}

Python

for item in interavel:
   //execução do loop
   
Utilizamos loops para iterar sobre sequências ou sobre valores
iteráveis

Exemplo de iteráveis:
- String
   nome = 'Geek University'
- Lista 
   lista = [1, 3, 5, 7, 9]
- Range
   numeros = range(1, 10)  
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)#temos que transformar em uma lista

#Exemplo de for 1
for letra in nome:#estou iterando sobre nome
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:#para cada numero na lista, imprima o numero
    print(numero)

#Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)
Obs.:O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
"""
for numero in range(1, 10):#o valor final não inclui
    print(numero)