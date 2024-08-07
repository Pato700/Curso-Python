""""
Este programa asigna o suma un valor.
"""
nombre = 'Hola '
nombre += input("Escribe tu nombre: ")

print(f"{nombre} Esto es el incremento y decremento de una variable.\n")

print("Incremento o aumento:")
x = 1
print(f"El valor inicia de x es: {x}")

x += 1
x += 1
x += 1
x += 1
print(f"El valor final de x es {x}")

print("Decremento o disminución:")
print(f"El valor inicia de x es: {x}")

x -= 1
x -= 1
x -= 1
x -= 1
print(f"El valor final de x es {x}")

print("Fin.")
