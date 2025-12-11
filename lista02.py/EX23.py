cores ={
    "limpa":"\033[m",
    "vermelho":"\033[31m",
}
mes = {
    1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio",
    6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro",
    11:"Novembro", 12:"Dezembro"
    }

try:
    n1 = int(input("Informe um numero inteiro (1-12): "))

    if n1 > 0 and n1 <=12:
        print(f"O mes correspondente ao número eh: {mes[n1]}")
    else:
        print(f"{cores['vermelho']}Erro! Digite apenas números de 1 a 12.{cores['limpa']}")
except ValueError:
    print(f"{cores['vermelho']}Erro! Digite apenas números inteiros.{cores['limpa']}")