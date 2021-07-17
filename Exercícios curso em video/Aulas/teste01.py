print("PROJETO TCHAU! \n")
print("PARTE 2 - INSTRUCAO: COBERTO POR ALGUMA ANTENA ")

'// COLETANDO DADOS PONTO'
print ("\nINFORME AS COORDENADAS DO PONTO")
XQ = int (input ("DIGITE A CORDENADA Xq: "))
YQ = int (input ("DIGITE A CORDENADA Yq: "))

'// DADOS ANTENA'
'// ANTENA A1=(15200,11901) RAIO DE ALCANCE R1=800'
XA1 = int(15200)
YA1 = int(11901)
R1 = int(800)
RAIO1 = R1 * R1

'// ANTENA A2=(16093,12287) RAIO DE ALCANCE R2=700'
XA2 = int(16093)
YA2 = int(12287)
R2 = int(700)
RAIO2 = R2 * R2

'// CALCULO AREA DE COBERTURA ANTENA'
CALCULO_ANTENA1 = ((XQ-XA1)*(XQ-XA1))+((YQ-YA1)*(YQ-YA1))
CALCULO_ANTENA2= ((XQ-XA2)*(XQ-XA2))+((YQ-YA2)*(YQ-YA2))

if CALCULO_ANTENA1 <= RAIO1:
    print("\nTRUE - O Ponto esta na area de cobertura")
elif CALCULO_ANTENA2 <= RAIO2:
    print("\nTRUE - O Ponto esta na area de cobertura")
else:
    print("\nFALSE - O Ponto esta fora da area de cobertura")
