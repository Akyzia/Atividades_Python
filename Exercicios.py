"""
1. Faça um programa que leia um número inteiro e imprima-o.
"""

numero: int = int(input("Informe um numero inteiro: "))

print(numero)

"""
2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
"""

numero1: int = int(input('Informe o primeiro inteiro: '))
numero2: int = int(input('Informe o segundo inteiro: '))
numero3: int = int(input('Informe o terceiro inteiro: '))

soma: int = numero1 + numero2 + numero3

print(f"A soma dos numeros {numero1} com {numero2} e {numero3} eh {soma}")


"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

"""

valor1: int = int(input('Informe o primeiro valor: '))
valor2: int = int(input('Informe o segundo valor: '))
valor3: int = int(input('Informe o terceiro valor: '))

soma: int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

print(f"A soma dos quadrados dos valores {valor1} com {valor2} e {valor3} eh {soma}")
