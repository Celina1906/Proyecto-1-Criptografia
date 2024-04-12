import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Descomponer n-1 como (2^r)*d
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Test de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=32):
    while True:
        # Generar un número aleatorio de 32 bits
        n = random.getrandbits(bits)
        # Asegurar que el número tenga exactamente 32 bits
        n |= (1 << bits - 1) | 1
        if is_prime(n):
            return n

prime = generate_prime()
print("Número primo generado:", prime)



