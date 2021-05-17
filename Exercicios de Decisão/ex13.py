num = int(input("Digite um numero de acordo com o dia da semana: "))

if num == 1:
    print("domingo")
if num == 2:
    print("segunda-feira")
if num == 3:
    print("terça-feira")
if num == 4:
    print("quarta-feira")
if num == 5:
    print("quinta-feira")
if num == 6:
    print("sexta-feira")
if num == 7:
    print("sábado")
elif num < 1 or num > 7:
    print("o número que introduziu não se refere a nenhum dia da semana!!!")
