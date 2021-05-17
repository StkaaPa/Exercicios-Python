nota = int(input("introduza a primeira nota: "))
nota2 = int(input("introduza a segunda nota: "))
nota3 = int(input("introduza a terceira nota: "))

media = (nota + nota2 + nota3)/3

if media < 7 and media >= 0:
    print("Está reprovado com uma média de ", media, "valores.")
if media >= 7 and media <= 9:
    print("Está aprovado com uma média de ", media, "valores.")
if media == 10:
    print("Está aprovado com distinçao, com uma média de ", media, "valores.")
elif media > 10:
    print("A média calculada é impossível!!!!")
