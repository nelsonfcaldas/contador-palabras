
# Escribir números en un archivo
with open("salida.txt", "w") as f:
    for i in range(1, 100):
        f.write(str(i) + "\n")

# Leer archivo y contar líneas
with open("salida.txt", "r") as f:
    lineas = f.readlines()

print("El archivo tiene", len(lineas), "líneas")

