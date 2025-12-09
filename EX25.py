cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "negrito": "\033[1m"
}

print("------ CALCULADORA PYTHON ------")
print("""
    +: Soma
    -: Subtração
    *: Multiplicação
    /: Divisão
""")

def calculadora (n1,escolhaDef,n2):
        if escolhaDef == "+":
            return n1 + n2
        elif escolhaDef == "-":
            return n1 - n2
        elif escolhaDef == "*":
            return n1 * n2
        elif escolhaDef == "/":
            try:
                return n1 / n2
            except ZeroDivisionError:
                print(f"{cores['vermelho']}Erro! Não é possível realizar divisão com 0.{cores['limpa']}")
                return None
        else:
            print(f"{cores['vermelho']}Erro! Operação inválida.{cores['limpa']}")
            return None
        
operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
}
try:
    primeiroNumero = int(input("Digite um número: "))
    escolha = str(input("Informe a operação a realizar: ")) 
    if escolha in operacoes:
        segundoNumero = int(input("Digite outro número: "))

        resultado = calculadora(primeiroNumero, escolha, segundoNumero)
        if resultado is not None:
            print(f"{cores['negrito']}O resultado da operação escolhida eh: {resultado}.{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}Erro! Operação inválida.{cores['limpa']}")
except ValueError:
    print(f"{cores['vermelho']}Erro! Somente números.{cores['limpa']}")
