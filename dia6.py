# Sumar los números de una lista
numeros = [1, 2, 3, 4, 5,6]
suma = 0

for n in numeros:
    suma += n

print("La suma es:", suma)

# Mini‑ejercicio: imprimir solo los pares
for n in numeros:
    if n % 2 == 0:
        print(n, "es par")
