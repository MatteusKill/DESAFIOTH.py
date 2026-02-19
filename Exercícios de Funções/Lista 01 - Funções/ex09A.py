def calcularTempo(tempMin):
    valorMinimoHora = 9
    horaAdicional = 1.50
    if tempMin > 15 and tempMin < 60:
        minExcedido = tempMin - 15
        valorTotal = 9
        print(f"Tempo excedido em minutos: {minExcedido}")
        print(f"O valor a ser pago: {valorTotal:.2f}")
    elif tempMin > 60:
        tempoExcedido = tempMin - 60
        valorTotal = (tempoExcedido * horaAdicional) + valorMinimoHora
        print(f"Quantidade de min excedidos: {tempoExcedido}.")
        print(f"O valor total a ser pago: R${valorTotal:.2f}.")
    else:
        print("Não ultrapassou o limite de 15 min estacionado.")

tempoMinutos = int(input("Informe a quantidade de tempo estacionado: "))

calcularTempo(tempoMinutos)