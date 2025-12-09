cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m"
}

n1 = int(input("Informe um valor de 1 a 7: "))

diaSemana = {
    1:"Domingo", 2:"Segunda-Feira", 3:"Terça-Feira",
    4:"Quarta-Feira", 5:"Quinta-Feira",6:"Sexta-Feira",7:"Sábado"
}

if n1 > 0  and n1 <= 7:
    print(f"O dia da semana eh: {diaSemana[n1]}")
else:
    print(f"{cores['vermelho']}Erro! Digite um número válido.{cores['limpa']}")