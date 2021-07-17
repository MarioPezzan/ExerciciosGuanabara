nu = int(input('Digite um numero inteiro de 0 a 9999: '))
print(f'Unidade: {nu // 1 % 10}')
print(f'Dezena: {nu // 10 % 10}')
print(f'Centena: {nu // 100 % 10}')
print(f'milhar: {nu // 1000 % 10}')

