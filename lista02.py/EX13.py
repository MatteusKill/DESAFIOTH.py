print('----- MAIOR OU MENOR Ex13 -----')
primeiroNumero = int(input("Digite um numero inteiro: "))
segundoNumero = int(input("Digite outro numero inteiro: "))

if primeiroNumero > segundoNumero:
    print(f'O primeiro numero eh maior que o segundo numero: {primeiroNumero}.')
elif segundoNumero > primeiroNumero:
    print(f'O segundo numero eh maior que o primeiro numero: {segundoNumero}.')
else: 
    print('Os numero digitados sao iguais.')