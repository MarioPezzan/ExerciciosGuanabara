primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira+segunda)/2
if media <= 4.9:
    print(f'Sua média foi \033[1;31m{media}\033[m e você foi \033[1;31mREPROVADO\033[m!')
elif 5 <= media <= 6.9:
    print(f'Sua média foi \033[1;33m{media}\033[m e você está de \033[1;33mRECUPERAÇÃO\033[m!')
elif media >= 7:
    print(f'Parabéns! Sua média foi \033[1;32m{media}\033[m e você \033[1;32mPASSOU\033[m de ano!')
