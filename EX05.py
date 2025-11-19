print('------ VERIFICACAO F OU M -----')
letraDigitada = str(input("Digite uma letra: ")).upper()

if letraDigitada == 'M':
    print("M-MASCULINO")
elif letraDigitada == 'F':
    print("F-FEMININO")
else:
    print("Erro! Sexo invalido.")