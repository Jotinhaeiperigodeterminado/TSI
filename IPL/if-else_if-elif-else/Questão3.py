#Escreva um programa que leia dois valores que representem o início
#e o fim de um intervalo. O programa deverá ler um terceiro valor
#digitado e verificar se este terceiro valor está dentro do intervalo ou
#fora. Caso esteja fora do intervalo, deverá informar se está na parte
#inferior ou superior do intervalo.

num1 = int(input('Escreva um número: '))
num2 = int(input('Escreva um número: '))
num3 = int(input('Escreva um número: '))

if num3 in range(num1, num2):
    print('O terceiro valor está dentro do intervalo.')
else:
    print('O terceiro valor está fora do intervalo.')

print('Fim do progama.')
