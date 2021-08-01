frase = str(input('Digite uma frase: ')).upper().strip()
primerio = frase.split()
junto = ''.join(primerio)
inverso = ''
#inverso = junto[::-1]
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]
print(f'O inverso de {junto.capitalize()} é {inverso.capitalize()} portanto')
if inverso == junto:
    print('tamos um polimetro')
else:
    print('não temos um polimetro')

#print(junto)