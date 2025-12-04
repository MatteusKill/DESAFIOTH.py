cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "verde":"\033[32m"
}

try:
    salarioTrabalhador = float(input("Informe o valor do seu salário: "))
    if salarioTrabalhador <= 0:
        print(f"{cores['vermelho']}Informe um valor maior que 0!{cores['limpa']}")
    else:
        valorPrestacao = float(input("Informe o valor do empréstimo: "))
        
        percentual20 = (salarioTrabalhador * (20/100)) + salarioTrabalhador

        if valorPrestacao > percentual20:
            print(f"{cores['vermelho']}Empréstimo não concedido!{cores['limpa']}")
        else:
            print(f"{cores['verde']}Empréstimo concedido.{cores['limpa']}")
except ValueError:
    print(f"{cores['vermelho']}Erro! Somente números.{cores['limpa']}")