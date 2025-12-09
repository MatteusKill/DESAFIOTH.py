ano = int(input("Informe o ano para verificar se eh bissexto: "))

if (ano % 400==0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"O ano {ano} eh bissexto.")
else:
    print(f"O ano {ano} nao eh bissexto.")