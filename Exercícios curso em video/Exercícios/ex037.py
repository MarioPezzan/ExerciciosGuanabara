num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converção 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
if num == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif num == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif num == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida, digite o número de uma opção valida!')
