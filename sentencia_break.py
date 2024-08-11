"""
Este programa es un bucle al cumplirse la condición la sentencia break rompe el bucle.
"""

print("==================")
print("SENTENCIA BREAK \n")
print("==================")

contador = 0

while contador < 10:
    contador += 1

    if contador == 5 :
        break
    print("Valor actual de la variable: ", contador)

print("Fin del programa, la sentencia break se ha ejecutado")
