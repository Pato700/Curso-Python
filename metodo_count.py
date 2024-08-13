"""
Este método es de gran utilidad cuando tenemos la nesesidad de conocer la cantidad
de veces que aparece una cadena o carácter en específico dentro de un texto.
"""

string = 'mi mama me mima'
contador = 0

print(string.center(40, "="))

contador = string.count("M")
print(f"\nLa letra 'M' se encontro {contador} veces en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra 'm' se encontro {contador} veces en la cadena: {string}")

contador = string.count("mama")
print(f"\nLa plabra 'mama' se encontro {contador} veces en la cadena: {string}")

contador = string.count("me mima")
print(f"\nLa palabra 'me mima' se encontro {contador} veces en la cadena: {string}")

contador = string.count("ma")
print(f"\nLa palabra 'ma' se encontro {contador} veces en la cadena: {string}")

contador = string.count("m", 13)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion 13: {string}")

contador = string.count("m", 100)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion 100: {string}")

contador = string.count("m", -3)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion -3: {string}")

contador = string.count("m", 3, 7)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion 3 hasta la posision 7: {string}")


contador = string.count("m", 100, 100)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion 100 hasta la posision 100: {string}")

contador = string.count("m", -4, -1)
print(f"\nLa letra 'm' se encontro {contador} veces desde la posicion -4 hasta la posision -1: {string}")
