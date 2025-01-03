"""
El método remove permite eliminar un elemento dentro de una lista, 
especificando a través de un argumento, el elemento que deseeamos eliminar
"""

vocales = ["a", "e", "i", "o", "u"]
print(f"{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "u"]
print(f"\n{vocales} \nElemento a eliminar: o")
vocales.remove("o")
print(vocales)

vocales = ["a", "e", "i", "o", "i"]
print(f"\n{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "u"]
print(f"\n{vocales} \nElemento a eliminar: I")
vocales.remove("I")
print(vocales)
