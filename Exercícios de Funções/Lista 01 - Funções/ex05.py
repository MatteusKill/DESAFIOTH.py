def somaImposto(custo:float, taxaImposto):
    result = (custo * (taxaImposto/100)) + custo
    return result

print(somaImposto(2.50, 15))
