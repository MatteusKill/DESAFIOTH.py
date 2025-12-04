cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m"
}

try:
    numeroInteiro = int(input("Informe um número inteiro mairo que 0 e menor que 1000: "))

    if numeroInteiro <= 0:
        print(f"{cores['vermelho']}Erro! Digite um valor maior que 0.{cores['limpa']}")
    else:
        if numeroInteiro < 10:
            print(f"O valor inserido tem somente um algarismo: {numeroInteiro}.")
        elif numeroInteiro < 100:
            dezena = numeroInteiro // 10
            unidade = numeroInteiro % 10
            print(f"A soma dos algarismos {dezena} e {unidade} eh: ", dezena+unidade)
        elif numeroInteiro < 1000:
            centena = numeroInteiro // 100
            dezena = numeroInteiro // 10
            restoDezena = dezena % 10
            unidade = numeroInteiro % 10
            print("A soma dos algarismo do numero digitado eh: ", centena + restoDezena + unidade)
        else:
            print(f"{cores['vermelho']}Valor ultrapassado! Insira um valor de 0 a 999.{cores['limpa']}")
except ValueError:
    print(f"{cores['vermelho']}Erro! Valor inválido, somente números.{cores['limpa']}")