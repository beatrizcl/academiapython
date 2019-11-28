hora, minuto, segundo = input("Digite a quantidade de horas, minutos e segundos no formato 00:00:00: ").split(':')
print(hora, minuto, segundo)
hora = int(hora)
minuto = int(minuto)
segundo = int(segundo)

hora = hora*3600
print(hora)
minuto = minuto*60
print(minuto)
print(segundo)
result = hora+minuto+segundo
print(f"A correção corresponde a {result} segundos.")
