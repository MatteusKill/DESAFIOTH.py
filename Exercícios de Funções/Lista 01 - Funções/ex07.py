def calcularSalario (horaTrabalhada, valorHora):
    cargaSemanal = 40
    if horaTrabalhada > cargaSemanal:
        horaExtra = horaTrabalhada - cargaSemanal
        salarioBase = cargaSemanal * valorHora
        valorExtras = horaExtra * (valorHora * 1.5)
        valorSalario = salarioBase + valorExtras
        print(f"Quantidade de horas totais trabalhadas: {horaTrabalhada}")
        print(f"Quantidade de horas extras: {horaExtra}")
        print(f"O salario a ser recebido: R${valorSalario:.2f}")
    else:
        valorSalario = horaTrabalhada * valorHora
        print(f"Quantidade de horas totais trabalhadas: {horaTrabalhada}")
        print(f"o seu salario com base nas horas trabalhadas: R${valorSalario:.2f}")
    
horaT = int(input("Informe a quantidade de horas trabalhadas na semana: "))
valorH = float(input("Informe o valor da sua hora de trabalho: "))

calcularSalario(horaT, valorH)