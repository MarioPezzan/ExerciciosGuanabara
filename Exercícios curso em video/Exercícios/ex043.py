peso = int(input('Qual seu peso?(KG) '))
altura = float(input('Qual sua altura?(M) '))
IMC = peso/(altura**2)
print(f'Seu IMC é de {IMC:.2f}, e ', end='')
if IMC < 18.5:
    print('você está abaixo do peso')
elif 18.5 >= IMC < 25:
    print('você está no peso ideal')
elif IMC <= 30:
    print('você está sobrepeso')
elif IMC < 40:
    print('você está com obesidade')
elif IMC >= 40:
    print('você está com obesidade mórbida')