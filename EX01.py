primeiroNumeroInt = int(input("Digite um numero inteiro: "))
segundoNumeroInt = int(input("Digite um numero inteiro: "))
numeroReal = float(input("Digite um numero real: "))

#CALCULAR PRODUTO DO PRIMEIRO COM METADE DO SEGUNDO
resultado1 = primeiroNumeroInt * (segundoNumeroInt / 2)

#CALCULAR A SOMA DO TRIPLO DO PRIMEIRO COM O TERCEIRO
resultado2 = (primeiroNumeroInt * 3) + numeroReal

#NUMERO DIGITADO AO CUBO
resultado3 = numeroReal **3

print(f"""
O produto do primeiro com metade do segundo: {resultado1}.

A soma do triplo do primeiro com o terceiro: {resultado2}.

O terceiro numero digitado ao cubo: {resultado3}.

""")