frase = str(input('Digite uma frase: ').lower().strip())
print('Quantidade de A encontrado na frase:', frase.count('a'))
print(f'Posição do primeiro A na frase:', frase.find('a')+1)
print(f'A posição do ultimo A aparece:', frase.rfind('a')+1)