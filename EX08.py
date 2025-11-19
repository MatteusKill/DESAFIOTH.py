import math

print("----- RAIS QUADRADA DE UM NUMERO -----")
numeroDigitado = float(input("Digite um numero:"))

if numeroDigitado > 0:
    raiz = math.sqrt(numeroDigitado)
    print(f"A raiz quadrada de {numeroDigitado} eh: {raiz}.")
else:
    print("O numero digitado nao eh invalido!")