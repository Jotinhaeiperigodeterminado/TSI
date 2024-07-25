#Escreva um algoritmo que solicite ao usuário o valor de duas notas e
#armazene o resultado em duas variáveis diferentes (float);
#Calcule o resultado da média desses valores;
#Imprima “Você está em RECUPERAÇÃO!!!” caso o resultado da média seja
#maior ou igual a 30 e menor do que 70.

nota1 = float(input('Adicione a nota: '))
nota2 = float(input('Adicione a nota: '))

media = (nota1 + nota2) / 2

if(media >= 30 and media < 70):
    print('Você está em RECUPERAÇÃO!!!')
elif(media < 30):
    print('Você está REPROVADO!!!')
else:
    print('Você está APROVADO!!!')

print('Fim do progama.')