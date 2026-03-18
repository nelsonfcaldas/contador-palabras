
contactos = {
        "Ana":"099111111",
        "Luis": "099222222",
        "Sofía": "099333333"
        }
nombre = input ("Ingresa un nombre: ")
if nombre in contactos:
    print("Telefono:",contactos[nombre])
else:
    print("No existe ese contacto")

