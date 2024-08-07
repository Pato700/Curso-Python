""""
Operadores Lógicos (and, or y not).
"""
#Conjunción

print("================")
print("Conjunción (and)")
print("================")

num = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num > 2 and num < 5:
    print("El número", num, "cumple con la condición.\n")
else:
    print("El número", num, "no cumple con la condición.\n")

#Disyunción

print("===============")
print("Disyunción (or)")
print("===============")

palabra = input("Para cumplir la condición escribe 'si' o 'yes': ")

if palabra == 'si' or palabra == 'yes':
    print("La condición se ha cumplido.\n")
else:
    print("La condición no se ha cumplido.\n")

#Negación

print("==============")
print("Negación (not)")
print("==============")

num = int(input("Introduce un número igual a 5: "))

if not num == 5:
    print("\nEl número es diferente de cinco y si cumple la condición.\n")
else:
    print("\nEl número es igual a cinco y no cumple con la condición.\n")
