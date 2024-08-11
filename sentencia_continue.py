"""
Este programa es un bucle al cumplirse la condición la sentencia continue
seguira ejecutandose hasta que la condición deje de cumplirse.
"""

print("==================")
print("SENTENCIA CONTINUE")
print("==================")

contador = 0

while contador < 10:
    contador += 1

    if contador == 5 :
        continue
    print("Valor actual de la variable: ", contador)
