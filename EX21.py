cores = {
    "limpa":"\033[m",
    "Vermelho":"\033[31m",
    "Verde":"\033[32m"
}

def calcularMedia (nT,avS,exF):
    pesoNT = 2
    ppesoAVS = 3
    pesoExameFinal = 5
    if nT <=2:
        if avS >0 and avS <=3:
            if exF > 0 and exF <=5:
                mediaAluno = (nT*pesoNT + avS*ppesoAVS + exF*pesoExameFinal)
                return mediaAluno
            else:
                print(f"{cores['Vermelho']}Nota Inválida! Nota do exame final somente de 0 a 5.{cores['limpa']}")
                return 0
        else:
            print(f"{cores['Vermelho']}Nota Inválida! Nota da " \
            f"Avaliação Semestral somente de 0 a 3.{cores['limpa']}")
            return 0
    else:
        print(f"{cores['Vermelho']}Nota Inválida! Nota do Trabalho de Laboratório somente" \
        f"de 0 a 2.{cores['limpa']}")
        return 0

try:
    notaTrabalho = float(
        input("Informe a nota obtidada no Trabalho de Laboratório (0 a 2): ")
    )
    notaAvaliacao = float(
        input("Informe a nota obtida na Avaliação Semestral (0 a 3): ")
    )
    notaExameFinal = float(
        input("Informe a nota obtida no Exame Final(0 a 5): ")
    )

    mediaFinal = calcularMedia(notaTrabalho, notaAvaliacao, notaExameFinal)

    if mediaFinal <= 2.9:
        print(f"Status do Aluno: {cores['Vermelho']}Reprovado.{cores['limpa']}")
    elif mediaFinal <= 5.9:
        print(f"Status do Aluno: {cores['Vermelho']}Recuperação.{cores['limpa']}")
    else:
        print(f"Status do Aluno: {cores['Verde']}Aprovado.{cores['limpa']}")
except ValueError:
    print(f"{cores['Vermelho']}Erro! Somente números.{cores['limpa']}")