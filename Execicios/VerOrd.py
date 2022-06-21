x = float (input("Insira um número: "))
y = float (input("Insira um número: "))
z = float (input("Insira um número: "))

if x < y:
    if y < z:
        print("Crescente")
    else:
        print("Não está em ordem crescente.")
else:
    print("Não está em ordem crescente.")