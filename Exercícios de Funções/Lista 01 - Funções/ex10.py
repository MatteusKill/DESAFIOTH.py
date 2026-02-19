def calcularFinanciamento(valorEntrada, valorVeiculo, numeroParcelas, taxaJuros):
    valorFinanciado = valorVeiculo - valorEntrada
    taxaJuros = taxaJuros / 100
    montanteFinal = valorFinanciado * (1 + taxaJuros) ** numeroParcelas
    valorParcela = montanteFinal / numeroParcelas
    totalPago = valorEntrada +  montanteFinal
    totalJuros = totalPago - valorVeiculo
    print(f"Total pago: {totalPago:.2f}")
    print(f"Quantia dos juros pagos: {totalJuros:.2f}")
    print(f"Valor de cada parcela: {valorParcela:.2f}")

valorVeic = float(input("Informe o valor do veiculo: "))
entrada = float(input("Informe o valor da entrada: "))
valorTaxa = float(input("Informe o valor da taxa: "))
qntdParcela = float(input("Informe a quantidade de parcelas: "))

calcularFinanciamento(valorEntrada=entrada, valorVeiculo=valorVeic, numeroParcelas=qntdParcela,taxaJuros=valorTaxa)