"""
Este programa convierte numeros a palabras y viseversa dependiendo la opcion que elijas.
"""

print("=========")
print("CONVERSOR")
print("=========")

print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero. \n")

opcion = int(input("Ingresar opcion: "))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_uno = int(input("Ingrese el numero a convertir: "))

    if opcion_uno == 1:
        print('UNO')
    elif opcion_uno == 2:
        print('DOS')
    elif opcion_uno == 3:
        print('TRES')
    elif opcion_uno == 4:
        print('CUATRO')
    elif opcion_uno == 5:
        print('CINCO')
    else:
        print("Este programa solo puede convertir numeros del 1 al 5.")

elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")

    opcion_dos = input("Ingrese la palabra a convertir: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == 'uno':
        print('1')
    elif opcion_dos == 'dos':
        print('2')
    elif opcion_dos == 'tres':
        print('3')
    elif opcion_dos == 'cuatro':
        print('4')
    elif opcion_dos == 'cinco':
        print('5')
    else:
        print("Este programa solo puede convertir palabras (uno, dos, tres, cuatro y cinco).")

else:
    print("Opcion no valida.")

print("Fin.")
