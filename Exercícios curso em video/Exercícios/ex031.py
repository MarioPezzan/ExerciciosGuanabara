km = float(input('Quantos quilometros você viajará? '))
print(f'Você iniciará uma viagem de {km}Km')
if km >= 200:
    print(f'E terá que pagar R${km*0.45:.2f}')
else:
    print(f'E terá que pagar R${km*0.50:.2f}')