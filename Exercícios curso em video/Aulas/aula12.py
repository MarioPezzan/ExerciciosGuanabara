nome = str(input('Qual seu nome? ')).title()
if nome == 'Mario':
    print('Que nome bonito você tem!')
elif nome == 'Ronaldo' or nome == 'Vampeta' or nome == 'Rogerio':
    print('Seu nome é igual de um jogador de futebol famoso!')
elif nome in 'Ana Julia Claudia Sandra':
    print('você tem um nome feminino bem bonito!')
elif nome == 'Gustavo' or nome == 'Jhow':
    print('Seu nome é uma bosta amigo')
print(f'Tenha uma Boa tarde {nome}!')