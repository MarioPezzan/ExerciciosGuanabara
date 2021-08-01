numero = int(input('Qual valor você quer sacar? '))
toralnotas50 = numero // 50
resto = numero - (toralnotas50 * 50)
if resto != 0:
    if toralnotas50 != 0:
        print(f'Dará o total de {toralnotas50} cédulas de R$50')
    totalnotas20 = resto // 20
    if totalnotas20 != 0:
        conta = numero - (totalnotas20 * 20)
        print(f'Dará o total de {totalnotas20} cédulas de R$20')
    if resto != 0:
        totalnotas10 = resto // 10
        if totalnotas10 != 0:
            resto = resto - (totalnotas10 * 10)
            print(f'Dará o total de {totalnotas10} cédulas de R$10')
        if resto != 0:
            totalnotas1 = resto // 1
            print(f'Dará o total de {totalnotas1} cédulas de R$1')
