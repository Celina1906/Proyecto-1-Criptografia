from math import gcd

def is_prime(num):
    """
    Comprueba si un número es primo.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_prime_divisor(n):
    """
    Encuentra el primer divisor primo de un número.
    """
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n

def euler_function(n):
    """
    Calcula la función totiente de Euler para un número dado.
    """
    if n < 1:
        print("Error: n debe ser mayor a uno")
        return None

    phi = n  # Inicializamos phi con n
    divisor = 2  # Comenzamos con el primer primo

    while divisor * divisor <= n:
        if n % divisor == 0:
            while n % divisor == 0:
                n //= divisor
            phi -= phi // divisor
        divisor += 1

    if n > 1:
        phi -= phi // n

    return phi

def generator_of_Zn(n):
    """
    Encuentra un generador del grupo multiplicativo Zn.
    """
    phi = euler_function(n)
    p = first_prime_divisor(phi)
    exp = round(phi/p)
    cont = 0
    for alpha in range(1, n):
        if pow(alpha, exp, n) != 1:
                print(alpha, " es un generador del grupo multiplicativo de Z", n)
                cont += 1
        if cont >= 3:
            break
            

#generator_of_Zn(71)  
