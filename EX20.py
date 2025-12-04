cores = {
    "limpa":"\033[m",
    "Vermelho":"\033[31m",
    "Verde":"\033[32m"
}

def calcularMedia (nota1,nota2,nota3):
    p1 = 1
    p2 = 1
    p3 = 2
    mediaAluno = (nota1*p1 + nota2*p2 + nota3*p3) / (p1+p2+p3)
    return mediaAluno

# --------------- TESTE PARA VER QUAL CÓDIGO FICA MAIS LEGÍVEL --------------------------
# primeiraNota = float(input("Infomre o valor da primeira nota obtida (0-100): "))
# if primeiraNota >= 0:
#     segundaNota = float(input("Infomre o valor da segunda nota obtida (0-100): "))
#     if segundaNota >= 0:
#         terceiraNota = float(input("Infomre o valor da terceira nota obtida (0-100): "))
#         if terceiraNota >= 0:
#             media = calcularMedia(primeiraNota,segundaNota,terceiraNota)

#             if media > 60:
#                 print("Status do aluno: Aprovado.")
#             else:
#                 print("Status do aluno: Reprovado.")
#         else:
#             print("Erro! Digite apenas notas de 0 a 100.")
#     else:
#         print("Erro! Digite apenas notas de 0 a 100.")
# else:
#     print("Erro! Digite apenas notas de 0 a 100.")


primeiraNota = float(input("Informe o valor da primeira nota obtida (0-100): "))
if primeiraNota < 0:
    print(f"{cores['Vermelho']}Erro! Digite apenas notas de 0 a 100.{cores['limpa']}")
else:
    segundaNota = float(input("Informe o valor da segunda nota obtida(0-100): "))
    if segundaNota < 0:
        print(f"{cores['Vermelho']}Erro! Digite apenas notas de 0 a 100.{cores['limpa']}")
    else:
        terceiraNota = float(input("Informe o valor da nota obtida (0-100): "))
        if terceiraNota < 0:
            print(f"{cores['Vermelho']}Erro! Digite apenas notas de 0 a 100.{cores['limpa']}")
        else:
            media = calcularMedia(primeiraNota,segundaNota,terceiraNota)

            if media > 60:
                print(f"Status do aluno: {cores['Verde']}Aprovado.{cores['limpa']}")
            else:
                print(f"Status do aluno: {cores['Vermelho']}Reprovado.{cores['limpa']}")
