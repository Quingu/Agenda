try:
    with open("email.txt") as arquivo_email:
        print(arquivo_email.readlines())
except FileNotFoundError:
    print("Arquivo não existe")