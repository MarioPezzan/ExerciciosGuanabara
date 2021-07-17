tupla = ('Futuro', 'Ronaldo')
for n in tupla:
    print(f'\n{n}', end=' ')
    for vogais in n:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')