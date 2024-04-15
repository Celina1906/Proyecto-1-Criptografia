import random

def miller_rabin(n, t):
    #Función auxiliar para calcular (x^y) % p de manera eficiente
    def power(x, y, p):
        res = 1
        x = x % p
        while y > 0:
            if y & 1:
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res
    
    #Función auxiliar para verificar si n es compuesto utilizando el test de Miller-Rabin
    def is_composite(n, d, r, a):
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return False
        return True
    
    #Verifica si n es un número par
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    #Encuentra r y d tal que n - 1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    #Realiza t iteraciones del test de Miller-Rabin
    for _ in range(t):
        a = random.randint(2, n - 2)
        if is_composite(n, d, r, a):
            return False
    
    return True

def generate_prime(bits):
    while True:
        #Genera un número impar aleatorio de bits de longitud
        n = random.getrandbits(bits)
        if n % 2 == 0:
            n += 1
        #Realiza el test de Miller-Rabin con 20 iteraciones
        if miller_rabin(n, 20):
            return n

#Genera un número primo de 32 bits de longitud
# primo = generate_prime(32)
# print("Número primo generado:", primo)
