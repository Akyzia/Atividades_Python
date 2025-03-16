"""
Estruturas lógicas: and (e),or (ou), not (não), is (é)

Operadores unários:
    - not

Operadores binários:
   - and, or, is

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor booleano é invertido, ou seja,
se for True, vira False, se for False, vira True
"""
#variaveis do tipo boolean
ativo = True
logado = True

#and
#por exemplo, para o usuário acessar o sistema
#ele precisa estar ativo. Para isso deve acessar o link no e-mail e ativar a conta
if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

#variaveis do tipo boolean
ativo = True
logado = True
#or
if ativo or logado:#um ou outro precisa ser True
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

#variaveis do tipo boolean
ativo = True
logado = False
#not
if not ativo:#se não for ativo, então print abaixo
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:#se não
    print('Bem-vindo, usuário')

#variaveis do tipo boolean
ativo = False
logado = False
#is
if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:#se não
    print('Bem-vindo, usuário')

#variaveis do tipo boolean
ativo = True
logado = False
#is
if ativo:
    print('Bem-vindo, usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

#ativo é True?
print(ativo is True)