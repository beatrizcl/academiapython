num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite novamente um número inteiro: "))
num3 = float(input("Digite um número real: "))

resp1 = (num1*2)*(num2/2)
resp2 = (num1**3)+num3
resp3 = (num3**3)

print(f"O resultado  do produto do dobro do primeiro número com metade do segundo é {resp1}")
print(f"A soma do triplo do primeiro número com o terceiro é {resp2}")
print(f"O terceiro número elevado ao cubo é {resp3}")