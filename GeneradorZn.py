from math import gcd
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primer_primo_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and es_primo(i):
            return i
    return n


def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
"""
    while b != 0:
        r=  a % b
        a= b
        b=r
    return a


def ord_shanks(a, n):
    if gcd(a, n) != 1:
        raise ValueError("a debe ser coprimo con n")
    
    m = int(n ** 0.5) + 1
    alpha = pow(a, m, n)
    beta = alpha
    for i in range(1, m + 1):
        beta = (beta * alpha) % n
        if beta == 1:
            return i * m
    
    return None
def euler(n):
    if n<1:
        print("Error n debe ser mayor a uno")
    else:
        cont=0
        for  i in range(1,n+1):
            if mcd(i,n)==1:
                cont=cont+1
    return cont
def euler2(n):
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
         
def orden(a, n):
    for t in range(1, n):
        if pow(a, t, n) == 1:#La función pow() toma dos argumentos obligatorios: la base y el exponente, y opcionalmente un tercer argumento que especifica el módulo (si se desea calcular la potencia modular).
            return t
    return None
def genZn(n):
    ordenZn=euler2(n)
    for alpha in range(1, n):
        if(orden(alpha,n)==ordenZn):
            print(alpha," Es un generador del grupo multiplicativo de Z",n)
            break;
def genZn2(n):
    phi=euler2(n) #Se puede cambiar por n-1 si es n es primo
    p=primer_primo_divisor(phi)
    print(p)
   
    exp=round(phi/p)
    print(exp)
    for alpha in range(1, n):
        if pow(alpha,exp, n) != 1:#La función pow() toma dos argumentos obligatorios: la base y el exponente, y opcionalmente un tercer argumento que especifica el módulo (si se desea calcular la potencia modular).
            print(alpha," Es un generador del grupo multiplicativo de Z",n)
            
            
    
