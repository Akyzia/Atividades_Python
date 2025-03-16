"""
Escopo de variaveis
Precisamos definir qual a limitação dessa variavel
Onde essa variavel será lida no meu programa?

Dois casos de escopo:

1 - Variaveis globais:
   -São reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variaveis locais:
   -São reconhecidas apenas no bloco onde foram declaradas, ou seja,
   seu escopo está limitado ao bloco onde foi declarado.

"""
"""Python é uma linguagem de tipagem dinamica, significa
 que ao declararmos uma variavel, não colocamos o tipo de dado dela
Este tipo é inferido ao atribuirmos o valor da mesma

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""

#Exemplo em python (Variavel global)
numero = 42
print(numero)

numero = 'Geek'
print(numero)
print(type(numero))

#Exemplo em python (Variavel local)
numero = 42

if numero >10:
    novo = numero + 10 #novo é uma variavel local
    print(novo)

print(novo)#se eu tentar imprimir, terá um erro, pois não é declarada fora, apenas dentro (local)