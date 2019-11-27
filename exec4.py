import math

x1, y1 = (input("Digite a primeira coordenada x/y: ")).split()
x2, y2 = (input("Digite a segunda coordenada x/y: ")).split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

dist = float(math.sqrt((x1-x2)**2+(y1-y2)**2))

print(f"A distância entre as coordenadas é {dist}.")
