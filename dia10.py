def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Usar la función
for num in range(1, 51):
    if es_primo(num):
        print(num, "es primo")

