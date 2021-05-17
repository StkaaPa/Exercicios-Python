# -*- coding: utf-8 -*-

# tamanho em Mb
arquivo = int(input("Digite o valor do tamanho do arquivo para download: "))
# velocidade em Mbps
v_internet = int(input("Digite o valor da velocidade de internet: "))

tempo = arquivo/v_internet

print("Tempo aproximado de download:", (tempo), "minutos.")
