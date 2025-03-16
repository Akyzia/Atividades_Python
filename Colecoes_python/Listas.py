"""
MUITO IMPORTANTE!!!

"""

"""
Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5,
    este array será SEMPRE do tipo inteiro, e poderá ter SEMPRE, no máximo, 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir
adicionando elementos:
- Qualquer tipo de dado: Não possuem tipo de dado fixo: ou seja, podemos colocar qualquer
tipo de dado.
- As listas em python são representadas por colchetes: []

"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e']

lista3 =[]

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else: print(f'Não encontrei o número {num}')

#Podemos facilmente ordenar uma lista
list.sort()#ordenando a lista
print(lista)#imprimindo a lista

#Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append
"""

print(lista1)
lista1.append(42)
print(lista1)

#lista1.append(12, 34, 56) #Erro, pois a função append aceita só um elemento, e aqui tem 3

lista1.append([8, 3, 1])#aqui a lista  aparece como elemento unico
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])#extend faz a mesma coisa que o append, mas coloca a lista como elemento adicional a lista
print(lista1)


#Podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente juntas duas listas
lista1 = lista1 + lista2 #utilizar o + faz a mesma coisa que o extend
print(lista1)


#se eu quiser a lista ao contrário por exemplo
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#dessa forma também deixa a lista ao contrário
print(lista1[::-1])#slice  (começa na posição 0 e vai até o final = ::, -1 = reverte)
print(lista2[::-1])#slice