city = input('Digite o nome da sua cidade: ').lower().strip()
n = 'santo' in city[:5]
if not n:
    print('não tem')
else:
    print('tem')