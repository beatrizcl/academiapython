salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))

porcentagem = porcentagem / 100

aumento = salario * porcentagem

salario = salario + aumento

print(f"O reajuste salarial é de {aumento} reais e o novo salário é: {salario} reais")