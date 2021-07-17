cont_homens = cont_pessoasidade = cont_idademulher = 0
while True:
    print(15*'-', f'CADASTRE UMA PESSOA', 15*'-')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        cont_pessoasidade += 1
    if sexo == 'M':
        cont_homens += 1
    if idade < 20 and sexo == 'F':
        cont_idademulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).upper()
    if continuar == 'N':
        break
print(15*'-')
print(f'Total de pessoas com mais de 18 anos: {cont_pessoasidade}')
print(f'Quantidades de homens: {cont_homens}')
print(f'Contidade de mulheres com menos de 20 anos: {cont_idademulher}')
