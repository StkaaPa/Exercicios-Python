# -*- ocidng: utf-8-*-


nota1 = int(input("Digite a sua primeira nota: "))
nota2 = int(input("Digite a sua segunda nota: "))

media = ((nota1 + nota2)/2)

if media >= 7 and media < 10:
    print("Você está aprovado.")
elif media == 10:
    print("Você está aprovado com distinção.")
else:
    print("Você está reprovado.")

if media < 0 and media >= 11:
    print("Não é possível ter essa média.")
