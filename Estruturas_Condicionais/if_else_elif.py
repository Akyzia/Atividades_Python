"""
Estruturas condicionais
if, else, elif

elif = junção entre if e else (Exemplo: else if) se for usar
#essa condicional, então posso usar elif
elif não existe no java e no C por exemplo

"""
"""
#Estrutura condicional if, else em C

if(idade < 18){
   print('Menor de idade');
}else if (idade == 18){
   printf('Tem 18 anos');
}else{
   printf('É menor de idade');
}

"""

#Estruturas condicionais em Python
idade = 18
#se idade <18 faça tal coisa, ou seja, vai imprimir "menor de idade"
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print ('Maior de idade')

#também é possivel, mas não é bom utilizar
if idade < 18:
    print('Menor de idade')
if idade == 26:
    print('Maior de idade')