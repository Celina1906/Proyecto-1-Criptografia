# Se crea una lista de enteros <= al numero primo
# Sacar el inverso multiplicativo modulo N de cada numero
# donde N es el número primo


# Se importa la función generadora de números primos
# y "sympy" para calcular el inverso multiplicativo
import Parte1, sympy

def invMultMod(nums, prime):
    """Calcula el inverso multiplicativo módulo
       N de cada número dentro de la lista con
       respecto al número primo.

    Args:
        nums (list <int>): Lista de números enteros <= N
        prime (int): Número primo grande

    Returns:
        dict: Diccionario con cada número de la lista y
              su respectivo inverso multiplicativo
              módulo de N.
    """
    
    inv = {}
    for num in nums:
        try:
            # Calcula el inverso multiplicativo módulo del número primo
            inverse = sympy.mod_inverse(num, prime)
            inv[num] = inverse
        except ValueError:
            # Controla el flujo en caso de no ser inverso multiplicativo
            inv[num] = None
    return inv


