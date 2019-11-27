num1 = int(input ("Digite um número: "))
num2 = int(input ("Digite um numero: "))
soma = num1 + num2
subtr = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2
if num1 > 0:
    mod1 = num1
else:
    mod1 = num1 * (-1)
if num2 > 0:
    mod2 = num2
else:
    mod2 = num2 * (-1)
rest = num1 % num2
print(f"O resultado da soma dos números é {soma}.")
print(f"O resultado da subtração dos números é {subtr}.")
print(f"O resultado da multiplicação dos números é {mult}.")
print(f"O resultado da duvisão dos números é {div}.")
print(f"O resultado da exponenciação dos números é {exp}.")
print(f"O resultado do módulo do primeiro número é {mod1}.")
print(f"O resultado do módulo do segundo número é {mod2}.")
print(f"O resultado do resto da divisão dos números é {rest}.")