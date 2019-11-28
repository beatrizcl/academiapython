sec = int(input("Digite o tempo em segundos: "))
if (sec>3600):
    hora = int((sec/60)/60)
    minutos = int((sec/60)%60)
    print(minutos)
    aux = (sec/60)
    print(aux)
    segundos = (sec%60)
    print(segundos)

else:
    hora = 0
    print(hora)
    minutos = int(sec/60)
    print(minutos)
    aux = (sec/60)
    print(aux)
    segundos = (sec%60)
    print(segundos)

print(f"{sec} segundos equivale a {hora}:{minutos}:{segundos} horas.")
