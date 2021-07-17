media = 0
velho = 0
nom1 = ''
mulhermaisvelha = 0
sexom = 0
for c in range(1, 5):
    print(5*'-', f'{c}° PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade
    if c == 1 and sexo in 'Mm':
        velho = idade
        nom1 = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nom1 = nome
    if sexo in 'Ff':
        sexom += 1
    if c == 1 and sexo in 'Ff':
        mulhermaisvelha = idade
    if sexo in 'Ff' and idade > mulhermaisvelha:
        mulhermaisvelha = idade
print(f'A média de idade do grupo é de {media/4}')
print(f'a idade do mais velho é de {velho} e seu nome é {nom1}')
if mulhermaisvelha < 20 and sexom > 1:
    print(f'Ao todo são {sexom} mulheres com menos de 20 anos')
if mulhermaisvelha > 20 and sexom > 1:
    print(f'Ao todo são {sexom} mulheres com idade maior que 20 anos')
if mulhermaisvelha < 20 and sexom == 1:
    print(f'á somente {sexom} mulher com menos de 20')
if mulhermaisvelha > 20 and sexom == 1:
    print(f'Ao todo são {sexom} mulher com idade maior que 20 anos')