#Escreva um algoritmo que leia o valor de um número inteiro digitado
#pelo usuário e armazene esse valor em uma variável;
#O algoritmo deve verificar se o valor digitado é um número positivo.
#Se o valor digitado for maior do que ZERO o programa deve escrever na tela
#O número é positivo!

num = int(input('Escreva um número: '))

if(num > 0):
    print('O número é positivo!')
else:
    print('O número não é positivo!')

print('Fim do programa.')
