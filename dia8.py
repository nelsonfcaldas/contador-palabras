nombres = []
    
for i in range(5):
       nombre = input ("Ingresa un nombre: ")
       nombres.append(nombre)

print("Lista original:", nombres)
print("Lista invertida:", list(reversed(nombres)))

    nombres_unicos = list(set(nombres))
    print("Sin duplicados:", nombres_unicos)

