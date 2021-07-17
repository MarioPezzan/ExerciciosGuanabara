import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem dos escolhidos será: ')
print(lista)