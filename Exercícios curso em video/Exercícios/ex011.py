print('Quantos litros de tinta precisa para se pintar uma parede?')
n3 = float(input('A cada 1 litro de tinta se pinta quantos m²? '))
n1 = float(input('Digite a largura da parede em metros: '))
n2 = float(input('Digite a altura da parede em metros: '))
n4 = n1*n2
print(f'Levando em consideração que a parede tem a dimenção de {n1} x {n2} e que sua área é de {n4}m² e que para cada 1 litro de tinta se pinta {n3}m², serão usadas {n4/n3} Litros de tinta')