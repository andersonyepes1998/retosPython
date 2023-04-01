# El valle de aburra afronta altas temperaturas año tras año, 
# Cree una que permita calcular la temperatura media de la tierra partir 
# de recibir 20 datos diarios de temperatura por 8 días diferentes
import random
import math

day1 = []
day2 = []
day3 = []
day4 = []
day5 = []
day6 = []
day7 = []
day8 = []

indice = 0

for indice in range(20):
    day1.append(random.randint(1, 100))
    day2.append(random.randint(1, 100))
    day3.append(random.randint(1, 100))
    day4.append(random.randint(1, 100))
    day5.append(random.randint(1, 100))
    day6.append(random.randint(1, 100))
    day7.append(random.randint(1, 100))
    day8.append(random.randint(1, 100))

datos = day1 + day2 + day3 + day4 + day5 + day6 + day7 + day8

lowDatos = math.floor((len(datos) - 1) / 2)
highDatos = math.ceil((len(datos) - 1) / 2)
media = (datos[lowDatos] + datos[highDatos]) / 2

print(media)
