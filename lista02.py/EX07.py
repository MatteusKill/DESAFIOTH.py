print('----- BRECHO DE REVENDA -----')
precoProduto = float(input("Digite o preco da aquisicao produto: "))

if precoProduto < 50:
    precoAlterado = precoProduto + (precoProduto * (45 / 100))
else:
    precoAlterado = precoProduto + (precoProduto * (30/100))

print(f'''
Preco recomendado para revenda: {precoAlterado:.2f}.
''')

