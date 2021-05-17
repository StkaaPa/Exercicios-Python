num = int(input("insira um número menor que 1000: "))
numstr = str(num)
qtnumero = len(numstr)

if num < 1000:
    if qtnumero == 3:
        centena = numstr[0:1]
        dezenas = numstr[1:2]
        unidades = numstr[2:3]
        print(num, " = "+centena + " centenas, " +
              dezenas + " dezenas e" + unidades + " unidades ")

    elif qtnumero == 2:
        dezenas = numstr[0:1]
        unidades = numstr[1:2]
        print(num, " = " + dezenas + " dezenas e" + unidades + " unidades ")

    elif qtnumero == 1:
        unidades = numstr[0:1]
        print(num, " = "+unidades + " unidades ")
else:
    print("o numero introduzido é maior que 1000.")
