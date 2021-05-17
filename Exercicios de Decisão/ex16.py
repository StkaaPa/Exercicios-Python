
import math

print("A Equação de 2º grau da forma: ax^2 + bx + c")

a = int(input("Digite um valor para a: "))

if a == 0:
    print("Como o valor inserido é de zero, a equação não é de 2º grau!!")
else:
    b = int(input("Digite um valor para o b:"))
    c = int(input("Digite um valor para o c:"))
    delta = ((b*b) - (4*a*c))

    if delta < 0:
        print("Como o delta calculado dá negativo, a equação não possui raízes.")
    elif delta == 0:
        delta = -b/(2*a)
        print("Como o delta é igual a zero, a equação possui uma raíz que é", delta)
    else:
        raiz1 = (-b - math.sqrt(delta))/(2*a)
        raiz2 = (-b + math.sqrt(delta))/(2*a)
        print("De acordo com os valores introduzidos, a sua equação tem duas raízes com os valores de", raiz1, "e", raiz2)
