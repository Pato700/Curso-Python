# Calculo promedio de notas de un curso
promedio, total, contar = 0.0, 0.0,0
sigo = True
while sigo:
        notadef = float(input("Introduzca la nota de un estudiante: "))
        total = total + notadef
        contar = contar + 1
        print("Procesar otro estudiante:(s-si, n-no):")
        resp = input()
        if resp == "n":
            sigo = False
        promedio = total / contar
        print("Promedio de notas del curso es: " + str(promedio))