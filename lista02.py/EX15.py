print('---- Calculadora de media ----')

def lerNotaValida (mensagem):
    """Função que verifica a nota se eh valida ou nao"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0 and valor <=10:
                return valor
            else:
                print('Erro! A nota tem que estar entre 0 e 10.')
        except ValueError:
            """Imprime erro caso digite um caractere"""
            print('Erro! Digite numeros.')

"""Chama a função def e armazena dentro do
argumento uma mensagem solicitando a nota"""
nota1 = lerNotaValida('Informe a primeira nota: ')
nota2 = lerNotaValida('Informe a segunda nota: ')

media = (nota1 + nota2) / 2
print(f'A media eh: {media}.')