VERMELHO = '\033[91m'
RESET = '\033[0m'
VERDE = '\033[32m'
print('----- CALCULADORA DE PESO IDEAL -----')

def lerAltura ():
        while True:
                try:
                        h = float(input("Informe a sua altura: "))
                        if h > 0 and h < 3.00:
                                return h
                        else:
                                print(f'{VERMELHO}Erro! Digite um valor valido para altura (0 a 3).{RESET}')
                except ValueError:
                        print(f'{VERMELHO}Erro! Digite somente numero.{RESET}')

def lerSexo ():
        while True: 
                sexo = input('Informe o seu sexo (M/F): ').upper()
                if sexo == 'M' or sexo == 'F':
                        return sexo
                else:
                        print(f'{VERMELHO}Erro! Informe um valor valido (M/F).{RESET}')

def calcularPesoIdeal (altura, sexo):
        if sexo == 'M':
                return (72.7 * altura) - 58
        else:
                return (62.1 * altura) - 44.7
        
print('\n')
print('===== RESULTADO =====')

alturaUsuario = lerAltura()
sexoUsuario = lerSexo ()

pesoIdeal = calcularPesoIdeal (alturaUsuario, sexoUsuario)

print(f'{VERDE}O peso ideal eh: {pesoIdeal:.2f}KG.{RESET}')