cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m"
}

def verificacaoTriangulo (a,b,c):
    if  a + b > c or b + c > a:
        if a == b == c:
            return print("Triângulo Equilátero.")
        elif a == b or b == c:
            return print("Triângulo Isósceles.")
        else:
            return print("Triângulo Escaleno.")
    else:
        return print(f"{cores['vermelho']}Os valores informado não formam um triângulo!{cores['limpa']}")
            
try:
    comprimento1 = float(input("Informe o comprimento do lado do triangulo: "))
    comprimento2 = float(input("Informe o comprimento do lado do triangulo: "))
    comprimento3 = float(input("Informe o comprimento do lado do triangulo: "))

    verificacaoTriangulo(comprimento1,comprimento2, comprimento3)

except ValueError:
    print(f"{cores['vermelho']}Valor Inválido! Informe um valor numérico.{cores['limpa']}")