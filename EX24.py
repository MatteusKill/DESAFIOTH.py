cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m"
}

def calcularTrapezio (bMaior, bMenor, h):
    if bMaior > 0 and bMenor > 0:
        a = ((bMaior + bMenor) * h) / 2
        return a
    else:
        return 0
    
try:
    print("----------------- CALCULADORA DA AREA DE UM TRAPEZIO -----------------")
    baseMaior = float(input("Informe um valor maior que 0 para a Base Maior: "))
    if baseMaior > 0:
        baseMenor = float(input("Informe um valor maior que 0 para a Base Menor: "))
        if baseMenor > 0:
            altura = float(input("Informe um valor para a altura: "))
            if altura > 0:
                areaTrapezio = calcularTrapezio(baseMaior, baseMenor, altura)
                print(f"A area do trapezio eh: {areaTrapezio:.2f}")
            else:
                print(f"{cores['vermelho']}Erro! Digite apenas números positivos.{cores['limpa']}")
        else:
            print(f"{cores['vermelho']}Erro! Digite apenas números positivos.{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}Erro! Digite apenas números positivos.{cores['limpa']}")

except ValueError:
    print(f"{cores['vermelho']}Erro! Somente números.{cores['limpa']}")