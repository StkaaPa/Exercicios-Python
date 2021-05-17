
sal = float(input("Digite o valor do seu salário: "))
aumento = sal * 0.20
aumento2 = sal * 0.15
aumento3 = sal * 0.10
aumento4 = sal * 0.05

salfinal = aumento + sal
salfinal2 = aumento2 + sal
salfinal3 = aumento3 + sal
salfinal4 = aumento4 + sal


if sal <= 280.00:
    print("O sálario introduzido foi de", sal, "R$. O percentual aumentado no seu salário foi de 20%, e o valor do aumento é de",
          aumento, "R$. O seu novo salário é de", salfinal, "R$.")
elif 280.00 < sal <= 700.00:
    print("O sálario introduzido foi de", sal, "R$. O percentual aumentado no seu salário foi de 15%, e o valor do aumento é de",
          aumento2, "R$. O seu novo salário é de", salfinal2, "R$.")
elif 700.00 < sal <= 1500.00:
    print("O sálario introduzido foi de", sal, "R$. O percentual aumentado no seu salário foi de 10%, e o valor do aumento é de",
          aumento3, "R$. O seu novo salário é de", salfinal3, "R$.")
elif sal > 1500.00:
    print("O sálario introduzido foi de", sal, "R$. O percentual aumentado no seu salário foi de 5%, e o valor do aumento é de",
          aumento4, "R$. O seu novo salário é de", salfinal4, "R$.")
