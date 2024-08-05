"""
Este programa calcula el promedio de notas de un curso.
"""

print("=======================")
print("CALCULADORA DE PROMEDIO")
print("=======================")

promedio, total, CONTAR = 0.0, 0.0,0
SIGO = True
while SIGO:
    notadef = float(input("Introduzca la nota de un estudiante: "))
    total = total + notadef
    CONTAR = CONTAR + 1
    print("Procesar otro estudiante:(s-si, n-no):")
    resp = input()
    if resp == "n":
        SIGO = False
        promedio = total / CONTAR
    print("Promedio de notas del curso es: ", round(promedio, 2))
