print('----- INFORME DOIS NUMEROS E VEJA QUAL O MAIOR DELES -----\n')
primeiroNumero = input("Digite um numero: \n")
segundoNumero = input("Digite outro numero: \n")

if primeiroNumero > segundoNumero:
    print("O primeiro numero digitado eh maior.")
elif segundoNumero> primeiroNumero:
    print("O segundo numero digitado eh maior.")
else:
    print("Os numeros digitado sao iguais.")
