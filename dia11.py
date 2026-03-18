while True:
    try:
        numero = int(input("Ingresa un número: "))
        print("Ingresaste:", numero)
        break
    except ValueError:
        print("Error: debes ingresar un número válido")

