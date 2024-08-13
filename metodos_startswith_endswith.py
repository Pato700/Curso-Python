"""
El método startswith(), 
se utiliza para comprobar si una cadena de caracteres comienza con una subcadena en particular.
El método endswith(), 
se utiliza para comprobar si una cadena de caracteres termina con una subcadena en particular.
"""

string = 'Patrcik se peina solo'
resultado = 0
starts_with = 'Ejemplo con startswith():'
ends_with = 'Ejemplo con endswith):'

print(f"\n{starts_with.rjust(50, '=')}")

resultado = string.startswith("P")
print(f"\n{string} comienza con la subcarpeta P: {resultado}")

resultado = string.startswith("p")
print(f"\n{string} comienza con la subcarpeta p: {resultado}")

resultado = string.startswith("Patrick")
print(f"\n{string} comienza con la subcarpeta Patrick: {resultado}")

resultado = string.startswith("se", 8)
print(f"\n{string} comienza con la subcarpeta se, desde la posicion 8: {resultado}")

resultado = string.startswith("se", 8, 9)
print(f"\n{string} comienza con la subcarpeta se, desde la posicion 8 hasta la posicion 9: {resultado}")

resultado = string.startswith("se", 100, 100)
print(f"\n{string} comienza con la subcarpeta se, desde la posicion 100 hasta la posicion 100: {resultado}")

resultado = string.startswith("se", -6, -1)
print(f"\n{string} comienza con la subcarpeta se, desde la posicion -6 hasta la posicion -1: {resultado}")


print(f"\n{ends_with.rjust(50, '=')}")

resultado = string.endswith("O")
print(f"\n{string} termina con la subcarpeta O: {resultado}")

resultado = string.endswith("o")
print(f"\n{string} termina con la subcarpeta o: {resultado}")

resultado = string.endswith("solo")
print(f"\n{string} termina con la subcarpeta solo: {resultado}")

resultado = string.endswith("solo", 10)
print(f"\n{string} termina con la subcarpeta se, desde la posicion 10: {resultado}")

resultado = string.endswith("solo", 9, 14)
print(f"\n{string} termina con la subcarpeta se, desde la posicion 9 hasta la posicion 14: {resultado}")

resultado = string.endswith("se", 100, 100)
print(f"\n{string} termina con la subcarpeta se, desde la posicion 100 hasta la posicion 100: {resultado}")

resultado = string.endswith("se", -6, -1)
print(f"\n{string} termina con la subcarpeta se, desde la posicion -6 hasta la posicion -1: {resultado}")
