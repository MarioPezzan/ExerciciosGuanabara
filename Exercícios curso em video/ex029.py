kmcarro = float(int(input('Digite quantos Km/h seu carro estava: ')))
if kmcarro >= 80:
    print(f'Seu carro excedeu o limite de velocidade de 80Km/h e  foi multado em R${(kmcarro-80)*7:.2f}')
else: print('Seu carro não excedeu o limite de velocidade.')