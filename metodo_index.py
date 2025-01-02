"""
Nos permite localizar dentro de una lista, un elemento en especifico, 
devolviendo un valor de tipo entero, el cual representa el índice de la primera coincidencia 
del elemento especificado a encontrar 
"""

vocales = ["a", "e", "i", "o", "u", "a"]

print(f"Lista: {vocales}")
print(f"La letra a esta en la posicion: {vocales.index('a')}")
print(f"La letra i esta en la posicion: {vocales.index('i')}")
print(f"La letra u en el rango 2-final esta en la posicion: {vocales.index('u', 2)}")
print(f"La letra i en el rango 2-4 esta en la posicion: {vocales.index('i', 2, 4)}")
