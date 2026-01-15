cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "amarelo":"\033[33m"
}

operacao = {"+": "Adicao", "-": "Subtacao", "/": "Divisao", "*": "Multiplicação"}

try: 
    print(f"""
{cores['amarelo']}+: Adição ||  -: Subtração  ||  /: Divisão  ||  *: Multiplicação{cores['limpa']}\n""")
    opcao = input("Informe a operacao a ser realizada: ")
    if opcao not in operacao:
        print(f"{cores['vermelho']}Erro! Operacao Inexistente.{cores['limpa']}")
    else:
        if opcao == "+":
            n1 = int(input("Informe um numero: "))
            n2 = int(input("Informe um numero: "))

            print(f"{cores['amarelo']}O resultado eh: {n1 + n2}.{cores['limpa']}")
        elif opcao == "-":
            n1 = int(input("Informe um numero: "))
            n2 = int(input("Informe um numero: "))

            print(f"{cores['amarelo']}O resultado eh: {n1 - n2}.{cores['limpa']}")
        elif opcao == "*":
            n1 = int(input("Informe um numero: "))
            n2 = int(input("Informe um numero: "))

            print(f"{cores['amarelo']}O resultado eh: {n1 * n2}.{cores['limpa']}")
        else:
            n1 = int(input("Informe o numerador: "))
            n2 = int(input("Informe o denominador (nao pode ser 0): "))
            if n2 == 0:
                print(f"{cores['vermelho']}Erro! Nao eh possivel dividir por 0.{cores['limpa']}")
            else:
                print(f"{cores['amarelo']}O resultado eh: {n1 + n2}.{cores['limpa']}")


except ValueError:
    print(f"{cores['vermelho']}Erro! Somente numeros.{cores['limpa']}")
except:
    print(f"{cores['vermelho']}Erro!{cores['limpa']}")