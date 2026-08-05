# Solucion con Ciclo for
import time

timestamp01 = time.time()

### Programa que calcula la suma de los N numeros naturales
number = 100
sum = 0

# Ciclo while
if number < 0:
	print("Ingrese un numero positivo...")
else:
	sum = 0
	while(number > 0):
		sum += number
		number =- 1
	print(f"La suma es {sum}")

### Programa completo
timestamp02 = time.time()
print(f"Tiempo de ejecucion: {timestamp02 - timestamp01}")
