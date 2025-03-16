"""

Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java

Utilizamos o break para sair de loops de maneira projetada

"""

#Exemplo 1

for num in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)#quando chega no 6 para o loop e imprime a frase abaixo
print('Sai do loop')

#Exemplo 2
while True:
    comando = input('Digite algo: ')
    if comando.upper() == 'sair':#quando eu digitar sair, eu saio do loop
        break
