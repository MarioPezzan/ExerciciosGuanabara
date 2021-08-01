contadorprodutos = maiorpreço = totalpreço = preçomenor = maiorquemil = 0
nome_produto_maiorpreço = ''
nome_produto_menorpreço = ''
while True:
    produto = str(input('Qual o nome do produto? ')).capitalize()
    preço = int(input('Qual o preço do produto: R$'))
    contadorprodutos += 1
    totalpreço += preço
    if contadorprodutos == 1:
        maiorpreço = preçomenor = preço
        nome_produto_maiorpreço = produto
        nome_produto_menorpreço = produto
    if preço > maiorpreço:
        maiorpreço = preço
        nome_produto_maiorpreço = produto
    if preço < preçomenor:
        preçomenor = preço
        nome_produto_menorpreço = produto
    if preço > 1000:
        maiorquemil += 1
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if stop == 'N':
        break
print(f'''O Produto com o maior preço foi {nome_produto_maiorpreço} e seu preço foi de R${maiorpreço:.2f}
O produto com menor preço foi {nome_produto_menorpreço} e seu preço foi de R${preçomenor:.2f}
A Quantidade de produtos adicionados foi {contadorprodutos} e o total da compra foi de R${totalpreço:.2f}
Quantidade de produtos com preço maior que R$1000,00 são de {maiorquemil}''')