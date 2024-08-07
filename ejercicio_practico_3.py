""""
Este programa mostrara el número mas grande de tres números ingresados.
"""

print("=============================")
print("COMPROBAR EL NÚMERO MÁS GRNDE")
print("=============================")

num_1 = int(input("\nIngresar el primer número: "))
num_2 = int(input("Ingresar el segundo número: "))
num_3 = int(input("Ingresar el tercer número: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"\n==> El número {num_1} es mas grande de los tres.")
elif num_2 > num_3:
    print(f"\n==> El número {num_2} es mas grande de los tres.")
else:
    print(f"\n==> El número {num_3} es mas grande de los tres.")

print("Fin.")
