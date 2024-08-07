"""
Este programa compara dos números para determinar si son diferentes, 
iguales, mayor o menor que el otro.
"""

print("================")
print("COMPARAR NUMEROS")
print("================")

num = int(input("Ingrese el primer número: "))
num = int(input("Ingrese el segundo número: "))

print("\nnum:")

if num != num:
    print(f"==> {num} es diferente a {num}")
else:
    print(f"==> {num} es igual a {num}")

if num > num:
    print(f"==> {num} es mayor que {num}")
elif num < num:
    print(f"==> {num} es menor que {num}")

print("Fin.")
