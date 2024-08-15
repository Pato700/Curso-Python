"""
Este programa invierte una cadena de caracteres, y a su vez, esta cadena de caracteres debera ser
ingresado por el usuario desde el teclado.
"""

# Solicitar al usuario que ingrese una cadena de caracteres
string = input("Ingresa una cadena de caracteres: ")

# Crear una variable para almacenar la cadena invertida
string_reversed = ""

# Utilizar un bucle for para recorrer la cadena original
for character in string:
    # Agregar cada carácter al principio de la cadena invertida
    string_reversed = character + string_reversed

# Imprimir la cadena invertida
print(f"Cadena invertida: {string_reversed}")
