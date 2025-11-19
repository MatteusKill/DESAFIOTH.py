print("----- VERIFICACAO DO TURNO EM QUE ESTUDA-----")
print("M-MANHA")
print("V-VESPERTINO")
print("N-NOTURNO")
print("\n")
turnoDigitado = str(input("Informe o turno que voce estuda: ")).upper()

if turnoDigitado == 'M':
    print('Bom dia!')
elif turnoDigitado == 'V':
    print('Boa tarde!')
elif turnoDigitado == 'N':
    print("Boa noite!")
else:
    print("Valor invalido!")