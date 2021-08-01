from datetime import date
ano = int(input('Que ano você nasceu? '))
idade =(date.today().year-ano)
print(f'Você nasceu em {ano} tem {idade} anos.')
if idade == 18:
    print('Você deverá se alistar esse ano!')
elif idade > 18:
    print(f'Você deveria ter se alistado a {idade-18} anos atrás ')
    print(f'Seu ano de alistamento foi em {(ano+18)}')
elif idade < 18:
    print(f'Você deverá se alistar daqui a {18-idade} anos')
    print(f'Seu ano de alistamento será em {(ano+18)}')
