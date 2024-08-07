""""
Este programa es una calculadora capáz de calcular suma, resta, multiplicación, , división, 
división entera, exponente y módulo o resto.
"""

print("====================")
print("CALCULADORA MULTIPLE")
print("====================")

print("\nMenú de numes:")
print("1. Suma.")
print("2. Resta.")
print("3. Multiplicación.")
print("4. División.")
print("5. División Entera.")
print("6. Exponente.")
print("7. Módulo o Resto.")

num = int(input("\nElije una opción: "))

if num == 1:
    print("\nElegista Suma.")
    num = int(input(("Ingrese el primer número: ")))
    num += int(input(("Ingrese el segundo número: ")))
    print(f"El resultado de la suma es {num}")
elif num == 2:
    print("\nElegista Resta.")
    num = int(input(("Ingrese el primer número: ")))
    num -= int(input(("Ingrese el segundo número: ")))
    print(f"El resultado de la resta es {num}")
elif num == 3:
    print("\nElegista Multiplicación.")
    num = int(input(("Ingrese el primer número: ")))
    num *= int(input(("Ingrese el segundo número: ")))
    print(f"El resultado de la multiplicación es {num}")
elif num == 4:
    print("\nElegista División.")
    num = float(input(("Ingrese el primer número: ")))
    num /= float(input(("Ingrese el segundo número: ")))
    print(f"El resultado de la división es {round(num, 2)}")
elif num == 5:
    print("\nElegista División Entera.")
    num = int(input(("Ingrese el primer número: ")))
    num //= int(input(("Ingrese el segundo número: ")))
    print(f"El resultado de la división entera es {num}")
elif num == 6:
    print("\nElegista Exponente.")
    num = int(input(("Ingrese el primer número: ")))
    num **= int(input(("Ingrese el segundo número: ")))
    print(f"El resultado del exponente es {num}")
elif num == 7:
    print("\nElegista Módulo o Resto.")
    num = int(input(("Ingrese el primer número: ")))
    num %= int(input(("Ingrese el segundo número: ")))
    print(f"El resultado del módulo o resto es {num}")
else:
    print("Opción no")

print("Fin.")
