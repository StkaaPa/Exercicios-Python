
year = int(input("Digite um ano: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("O Ano selecionado foi/será bissexto.")
else:
    print("O ano selecionado não/não será foi bissexto.")
