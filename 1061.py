dia_inicial = int(input().split()[1])
hora = input().split(":")

hora_inicial = int(hora[0])
minuto_inicial = int(hora[1])
seg_inicial = int(hora[2])

dia_final = int(input().split()[1])
hora = input().split(":")

hora_final = int(hora[0])
minuto_final = int(hora[1])
seg_final = int(hora[2])

dias = dia_final - dia_inicial

horas = hora_final - hora_inicial
if horas < 0:
    horas += 24
    dias -= 1

minutos = minuto_final - minuto_inicial
if  minutos < 0:
    minutos += 60
    horas -= 1

segundos = seg_final - seg_inicial
if segundos < 0:
    segundos += 60
    minutos -= 1

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias,horas,minutos,segundos))



