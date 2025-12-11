cores = {
    "limpa":"\033[m",
    "Vermelho":"\033[31m",
    "Verde": "\033[32m"
}

def calcularImposto (ir,salario):
    if salario > 2_500:
        impostoTotal = salario - ((ir/100) * salario) 
        return impostoTotal
try:
    horasTrabalhadas = float(
        input("Informe a quantidade de horas que você trabalhou esse mes: "))
    valorHora = 40.50

    salarioBruto = valorHora * horasTrabalhadas

    salarioLiquido = calcularImposto(11, salarioBruto)

    print(f"{cores['Verde']}O seu salario liquido com base nas contas eh: {salarioLiquido:.2f}{cores['limpa']}")
except ValueError:
    print(f"{cores['Vermelho']}Erro! Valor inválido.{cores['limpa']}")