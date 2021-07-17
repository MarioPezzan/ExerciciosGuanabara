extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[n]}')