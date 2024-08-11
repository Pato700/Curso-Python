"""
El método rstrip elimina únicamente los ultimos caracteres de una cadena,
en cambio lstrip elimina únicamnete los primeros caracteres de una cadena.
"""

#ejemplo rstrip
cadena = '\tPatrick\n'
print(cadena)

cadena = cadena.rstrip("ck\n")

print(cadena)

#ejemplo lstrip
cadena = '\tPatrick\n'
print(cadena)

cadena = cadena.lstrip("\tPa")

print(cadena)
