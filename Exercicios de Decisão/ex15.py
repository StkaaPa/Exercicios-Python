num = int(input("Digite um lado do triangulo: "))
num2 = int(input("Digite outro lado do triângulo: "))
num3 = int(input("Digite outro lado do triângulo: "))

if num + num2 < num3 or num2 + num3 < num or num3 + num < num2:
    print("Isso não é um triângulo, pois a soms de quaisquer dois lados é menor que o terceiro lado!!!")
elif num == num2 == num3:
    print("Como todos os lados são iguais, é um triangulo equilátero!!!")
elif num == num2 or num2 == num3 or num3 == num:
    print("Como tem dois lados iguais é um triangulo isósceles!!!!")
elif num != num2 != num3:
    print("Como todos os lados são diferentes é um triangulo escaleno!!!!")
