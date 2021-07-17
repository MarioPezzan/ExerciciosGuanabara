from datetime import date
cont = 0
cont2 = 0
print('Digite a idade de 7 pessoas')
idade = (date.today().year)
for c in range(1, 8):
    ano = int(input(f'ano de nascimento da {c}° pessoa: '))
    idade = (idade - ano)
    if idade < 17:
        cont += 1
    if idade >= 18:
        cont2 += 1
print(f'Existem {cont} pessoas que não atingiram a maioridade e {cont2} pessoas que atingiram a maioridade')
