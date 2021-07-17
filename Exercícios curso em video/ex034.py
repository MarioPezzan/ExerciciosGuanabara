salario = float(input('Qual o salario do funcionario R$'))
if salario >= 1250:
    print(f'Antes do aumento o salario era de R${salario:.2f} após o aumento passou a ser R${(salario*0.1)+salario:.2f} ')
else:
    print(f'Antes do aumento o salario era de {salario:.2f} após o aumento passou a ser R${(salario*0.15)+salario:.2f}')
