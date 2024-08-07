"""
Este programa convierte numeros a palabras y viseversa dependiendo la num que elijas.
"""

print("=========")
print("CONVERSOR")
print("=========")

print("Menu de numes: \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero. \n")

num = int(input("Ingresar num: "))

if num == 1:
    print("\n Conversor de numero a palabra. \n")

    num = int(input("Ingrese el numero a convertir: "))

    if num == 1:
        print('UNO')
    elif num == 2:
        print('DOS')
    elif num == 3:
        print('TRES')
    elif num == 4:
        print('CUATRO')
    elif num == 5:
        print('CINCO')
    else:
        print("Este programa solo puede convertir numeros del 1 al 5.")

elif num == 2:
    print("\n Conversor de palabra a numero. \n")

    num = input("Ingrese la palabra a convertir: ")
    num = num.lower()

    if num == 'uno':
        print('1')
    elif num == 'dos':
        print('2')
    elif num == 'tres':
        print('3')
    elif num == 'cuatro':
        print('4')
    elif num == 'cinco':
        print('5')
    else:
        print("Este programa solo puede convertir palabras (uno, dos, tres, cuatro y cinco).")

else:
    print("num no valida.")

print("Fin.")
