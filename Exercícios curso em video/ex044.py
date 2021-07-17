print(f"\033[;34m{10*'-='} LOJAS PEZZA'S {10*'=-'}\033[m")
preco = float(input('Qual o preço total da compra?\033[1;32mR$'))
print("""\033[;31m[1]\033[m à vista dinheiro/cheque
\033[;32m[2]\033[m à vista no cartão
\033[;33m[3]\033[m em até 2x no cartão
\033[;34m[4]\033[m 3x ou mais no cartão""")
forma = int(input('Qual a forma de pagamento? '))
if forma == 1:
    print(f'Para pagamentos avista no dinheiro ou cheque o valor será de R$\033[;32m{preco-(preco*0.1):.2f}')
elif forma == 2:
    print(f'Para pagamentos avista no cartão o valor da compra será de R$\033[;32m{preco-(preco*0.05):.2f}')
elif forma == 3:
        print(f'Para uma compra de R$\033[;32m{preco}\033[m em 2x no cartão o valor de cada parcela será de R$\033[;32m{preco/2:.2f}\033[m sem juros' )
elif forma == 4:
    parcelas = int(input('Quantas parcelas serão? '))
    n1 = preco + (preco * 0.2)
    if parcelas > 2:
        print(f'Para pagamento parcelado em {parcelas}x no cartão o valor de cada parcela será de R$\033[;32m{n1/parcelas:.2f}\033[m')
        print(f'e o valor total da compra será de R$\033[;32m{n1:.2f}')
else:
    print('\033[;31mVALOR DIGITADO INVÁLIDO')


