"""
Este programa compara dos números para determinar si son diferentes, 
iguales, mayor o menor que el otro.
"""

print("================")
print("COMPARAR NUMEROS")
print("================")

num_uno = int(input("Ingrese el primer número: "))
num_dos = int(input("Ingrese el segundo número: "))

print("\nResulltado:")

if num_uno != num_dos:
    print(f"==> {num_uno} es diferente a {num_dos}")
else:
    print(f"==> {num_uno} es igual a {num_dos}")

if num_uno > num_dos:
    print(f"==> {num_uno} es mayor que {num_dos}")
elif num_uno < num_dos:
    print(f"==> {num_uno} es menor que {num_dos}")

print("Fin.")
