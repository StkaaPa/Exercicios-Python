# as notas apenas podem ser entre 0.0 e 10.0
nota = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))

media = ((nota + nota2)/2)

conceito = ["A", "B", "C", "D", "E"]

if 9.0 < media <= 10.0:
    print("Como a média dá", media,
          "e está entre 9.0 e 10.0 o seu conceito é", conceito[0], "e está APROVADO.")
if 7.5 < media <= 9.0:
    print("Como a média dá", media,
          "e está entre 7.5 e 9.0 o seu conceito é", conceito[1], "e está APROVADO.")
if 6.0 < media <= 7.5:
    print("Como a média dá", media,
          "e está entre 6.0 e 7.5 o seu conceito é", conceito[2], "e está APROVADO.")
if 4.0 < media <= 6.0:
    print("Como a média dá", media,
          "e está entre 4.0 e 6.0 o seu conceito é", conceito[3], "e está REPROVADO.")
if 0.0 < media <= 4.0:
    print("Como a média dá", media,
          "e está entre 0.0 e 4.0 o seu conceito é", conceito[4], "e está REPROVADO.")
elif 0.0 > media or 10.0 < media:
    print("A sua média é inválida!!!!")
