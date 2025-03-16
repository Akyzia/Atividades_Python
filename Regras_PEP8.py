"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem python
A ideia da PEP8 é que possamos escrever códigos python de forma pythonica.
[1] - Utilize Canel Zase para nomes de classes:

class Calculadora:
      pass

[2] - Utilize nomes em minúsculo, separado por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    class


numero 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
--separar funções e definições de classe com duas linhas em branco:
--métodos dentro de uma classe devem ser separados com uma única linha em branco

class Classe:
    pass


class Outra:
    pass

[5] - Imports
--imports devem sempre ser feitos em linhas separadas:

#import errado
import sys, os

#import certo
import sys
import os

#Não já problemas em utilizar:

from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringTyoe,
    ListType,
    SetType,
    OutroType
)

#imports devem ser colocados no topo do arquivo, logo
depois de quaisquer comentários ou docstrings e antes
de constantes ou variáveis globais.

[6] - Espaços em expressoes e instruções

#Não faça:
função(_algo[_1_], {_outro: 2_}_)

#Faça:
funcao(algo[1], {outro: 2})

#Não faça:
algo_(1)

#Faça:
algo(1)

#Não faça:
dict_['chave'] = list_[indice]

#Faça:
dict['chave'] = lista[indice]

#Faça:
x = 1
y = 3

variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha

print ('Algo')

"""