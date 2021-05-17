
print("O valor mínimo para levantar é de 10 euros e o valor máximo é de 600 euros!")
x = int(input("Introduza o valor a extrair: "))

num1 = int(x / 100)
x = x % 100

num2 = int(x / 50)
x = x % 50

num3 = int(x / 10)
x = x % 10

num4 = int(x / 5)
x = x % 5

num5 = int(x)

print("Para levantar a quantia desejada, o programa fornece {} notas de 100€, {} notas de 50€, {} notas de 10€, {} notas de 5€ e {} notas de 1€".format(
    num1, num2, num3, num4, num5))
