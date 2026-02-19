def calcularTempo(tempMin):
    PIS = 0.33
    COFINS = 0.20
    ICMS = 17
    imposto = 17.53
    valorMinimoHora = 9
    horaAdicional = 1.50
    if tempMin > 15 and tempMin < 60:
        minExcedido = tempMin - 15
        valorTotal = 9 + (9 * imposto/100)
        print(f"Tempo excedido em minutos: {minExcedido}")
        print(f"""
            --- TABELA DE IMPOSTO ACRESCIDOS ---
            PIS = {PIS}
            COFINS = {COFINS}
            ICMS = {ICMS}
            TOTAL IMPOSTO = {imposto}
""")
        print(f"O valor a ser pago: {valorTotal:.2f}")
    elif tempMin > 60:
        tempoExcedido = tempMin - 60
        valorExcedido = (tempoExcedido * horaAdicional) + valorMinimoHora
        valorTotal  = valorExcedido + (valorExcedido * imposto/100)
        print(f"Quantidade de min excedidos: {tempoExcedido}.")
        print(f"""
            --- TABELA DE IMPOSTO ACRESCIDOS ---
            PIS = {PIS}
            COFINS = {COFINS}
            ICMS = {ICMS}
            TOTAL IMPOSTO = {imposto}
""")
        print(f"O valor total a ser pago: R${valorTotal:.2f}.")
    else:
        print("Não ultrapassou o limite de 15 min estacionado.")

tempoMinutos = int(input("Informe a quantidade de tempo estacionado: "))

calcularTempo(tempoMinutos)