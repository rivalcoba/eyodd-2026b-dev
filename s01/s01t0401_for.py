# Solucion con Ciclo for
import time

timestamp01 = time.time()

### Programa que calcula la suma de los N numeros naturales
number = 100
sum = 0

# Ciclo for
for value in range(1,number+1):
	sum = sum + value

print(f"La suma es {sum}")

### Programa completo
timestamp02 = time.time()
print(f"Tiempo de ejecucion: {timestamp02 - timestamp01}")
