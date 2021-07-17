print('Aprovador de emprestimo bancario.')
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário mensal? R$'))
anos = int(input('Em quantos anos você deseja pagar? '))
prestacao = valor/(anos*12)
n1 = (50/100)*salario
print(f'Para pegar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
if prestacao >= n1:
    print('\033[0:31mEmprestimo negado')
else:
    print('\033[0;32mEmprestimo aprovado')
