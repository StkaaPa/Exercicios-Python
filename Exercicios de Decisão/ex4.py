
letra = str(input("Digite uma letra: "))

if letra.isalpha():
    if letra == 'a':
        print("É uma vogal.")
    elif letra == 'e':
        print("É uma vogal.")
    elif letra == 'i':
        print("É uma vogal.")
    elif letra == 'o':
        print("É uma vogal.")
    elif letra == 'u':
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print(letra, "Não é uma letra.")
