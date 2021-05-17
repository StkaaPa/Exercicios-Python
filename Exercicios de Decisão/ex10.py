from typing import MappingView


print("Em que turno você estuda")
turno = str(input("Digite o caracter referente ao turno em que estuda: "))
"""
Introduza apenas as letras M,N ou V respetivamente ao seu turno
"""
if turno.isalpha():
    if turno == "M" or "m":
        print("Bom dia!!")
    elif turno == "V" or "v":
        print("Boa tarde!!")
    elif turno == "N" or "n":
        print("Boa noite!!")
    else:
        print("O turno introduzido é inválido!!")
else:
    print("Apenas pode introduzir caracteres!!!")
