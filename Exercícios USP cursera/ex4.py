n1 = int(input('Digite um numero: '))
n2 = n1 % 3
n3 = n1 % 5
if n2 == 0:
    if n3 == 0:
        print('FizzBuzz')
    else:
        print(n1)
else:
    print(n1)