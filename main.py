########################################
# Proyecto 1 - Criptografía - IC-8052  #
#                                      #
# Celina Madrigal - 2020059364         #
# Maria Jose Porras - 2019066056       #
# Pablo Villafuerte - 2019068262       #
# Gustavo Pérez - 2020084832           #
#                                      #
# Ultima modificacion: 15/04/2024      #
########################################

# Importación de los archivos
import Parte1, Parte2, GeneradorZn

# Generación del número primo
prime = Parte1.generate_prime(32)

# Lista con enteros entre [0, 100001]
listNums = [x for x in range(1, 100001)]
invsMultMod = Parte2.invMultMod(listNums, prime)

# Encontramos 3 generadores del número primo
GeneradorZn.generator_of_Zn(prime)