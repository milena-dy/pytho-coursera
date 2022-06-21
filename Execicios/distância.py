import math
aX = float (input("Insira a primeira coordenada A: "))
aY = float (input("Insira a segunda coordenada A: "))
bX = float (input("Insira a primeira coordenada B: "))
bY = float (input("Insira a segunda coordenada B: "))

distancia = math.sqrt(((aX - aY) ** 2) + ((aY - bY) ** 2))

if distancia <= 10:
    print("longe")
else:
    print("perto")
