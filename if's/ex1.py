segundos = int(input("Segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
seg = resto % 60

print(horas, "hora(s),", minutos, "minuto(s) e", seg, "segundo(s)")