
prod = int(input("Insira o primeiro preço: "))
prod2 = int(input("Insira o segundo preço: "))
prod3 = int(input("insira o terceiro preço: "))


def preco():
    if prod < prod2 and prod < prod3:
        print("Leve o produto 1 pois é o mais barato.")
    elif prod2 < prod and prod2 < prod3:
        print("Leve o produto 2 que é o mais barato.")
    elif prod3 < prod and prod3 < prod2:
        print("Leve o produto 3 que é o mais barato.")


preco()
