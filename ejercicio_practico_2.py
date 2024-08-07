"""
Este programa determinará e indicará si el número es par o impar.
"""

print("==================")
print("NÚMERO PAR O IMPAR")
print("==================")

try:
    num = int(input("Ingresar un número para determinar si es par o impar: "))
    if num % 2 == 0:
        print(f"\n==> El número {num} es par.")
    else:
        print(f"\n==> El número {num} es impar.")
except ValueError:
    print("La entrada no es un número entero válido.")

print("Fin.")
