# -*- coding: utf-8 -*-

mes = str(input("Digite o mês no qual quer saber o seu salário liquido:"))
v = float(input("Digite o valor de quanto ganha por hora: "))
# o numero médio de horas de trabalho por mês é 144 horas
h = float(input("Digite o valor de horas que trabalhou no referido mês: "))
salario = v * h  # salário bruto ao fim do mês
inss = salario * 8/100
ir = salario * 11/100
sindicato = salario * 5/100
descontos = inss + ir + sindicato
sliquido = salario - inss - ir - sindicato
print("O salário bruto no mês", mes, "é de", salario, "euros.")
print("Do sálario bruto indicado foram descontados", inss, "euros para a inss, foram descontados", ir,
      "euros para o imposto de renda \nforam descontados", sindicato, "euros para o sindicato, o que prefaz um total de descontos de", descontos, "euros.")
print("Depois de calculados todos os descontos o seu salário líquido ao fim do mês",
      mes, "é de", sliquido, "euros.")
