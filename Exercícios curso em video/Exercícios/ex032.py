from datetime import date
ano = input('Qual ano você deseja analisar? Digite "atual" para analisar o ano atual: ').lower()
if ano == 'atual':
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')
