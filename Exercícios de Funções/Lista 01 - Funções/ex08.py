def calcularExcesso(pesoKG):
    pesoMaximo = 50
    if pesoKG > pesoMaximo:
        kgExcedido = pesoKG - pesoMaximo
        precoMulta = 4.00 * kgExcedido
        print(f"Quantidade de KG excedido: {kgExcedido:.2f}")
        print(f"Valor da multa: {precoMulta:.2f}")
    else:
        print("Nao receberá multa! A quantidade informada não excedeu a quantidade do regulamento.")

pesoPeixe = float(input("Informe a quantidade em KG do peixe pescado: "))

calcularExcesso(pesoPeixe)