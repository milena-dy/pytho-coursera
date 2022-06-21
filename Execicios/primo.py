n = int(input("Digite um número inteiro positivo: "))
numero = 2
primo = True
while (numero <= n-1) and (primo):
    if (n % numero == 0):
        primo = False
    numero = numero + 1
if (primo):
    print("É primo.")
else:
    print("Não é primo.")