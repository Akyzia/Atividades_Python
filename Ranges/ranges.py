"""
Ranges
-Precisamos conhecer o loop for para usar os ranges
-Precisamos conhecer o range para trabalhar melhor com loop for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

Obs.: valor_de_parada não inclusive (inicio padrão 0,
e passo de 1 em 1)

"""

#Exemplo Forma 1
for num in range(11):#se nao especificar em qual numero ira começar, começara em 0
    print(num)

#Forma 2
range(valor_de_inciio, valor_de_parada)
#Obs.: valor_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

#Exemplo Forma 2
for num in range (1,11):
    print(num)

#Forma 3
range(valor_de_inciio, valor_de_parada, passo)
#Obs.:Passo especificado pelo usuario

#Exemplo Forma 3
for num in range (5, 50, 5):#começa no 5, vai até o 50 de 5 em 5
    print(num)