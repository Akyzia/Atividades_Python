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

#também aceitas listas assim
lista6 = [1, 2 , 3.2, True, 'Geek', [1, 2 , 5], 145236]

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

#Forma1
#se eu quiser a lista ao contrário por exemplo
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Forma2
#dessa forma também deixa a lista ao contrário
print(lista1[::-1])#slice  (começa na posição 0 e vai até o final = ::, -1 = reverte)
print(lista2[::-1])#slice

#também pode-se copiar uma lista
lista6 = lista2.copy()
print(lista6)

#saber o numero de elementos em uma lista
print(len(lista1))

#remover o ultimo elemento da lista com pop
print(lista5)
lista5.pop()
print(lista5)

#remover um elemento pelo indice
#Obs.: Os elementos a direita deste indice serão deslocados para a esquerda
#Obs.: Se não houver elementos no indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

#Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

#repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#split
#Obs.: Por padrão, o split separa os elementos da lista pelo espaço entre elas
curso = "programação teste"
print(curso)
curos = curso.split()
print(curso)

#convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

#abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

#abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em string
curso = '$'.join(lista6)
print(curso)

#iterando sobre listas
#exemplo1 utilizando for
#para cada elemento dentro da lista, imprima esse elemento para mim
soma = 0
for elemento in lista1:
    print(elemento)
    some = soma + elemento
print(soma)

#exemplo2 utilizando while
carrinho = []#lista vazia
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
#quando digitar 'sair' vou para o loop do for

for produto in carrinho
    print(produto)
