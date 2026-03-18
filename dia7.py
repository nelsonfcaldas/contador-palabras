
#Juego de adivinar numero
import random

secreto = random.randint(1,10)
intento= None
contador=0

while intento != secreto:
    intento = int(input("Adivina el numero 1-10):"))
    contador += 1

print (" ¡Correcto! Lo lograste en ", contador, "intentos")

