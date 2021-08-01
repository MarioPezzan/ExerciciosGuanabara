a = ''
while a != 'M' and a != 'F':
    a = str(input('Digite seu sexo[M/F]: ')).upper().strip()
    if a != 'm' and a != 'f':
        print('valor invalido, digite F ou M')
if a == 'F':
    print('Você é do gênero feminino!')
elif a == 'M':
    print('Você é do gênero masculino!')
