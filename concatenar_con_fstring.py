"""
Los f-string son mas rápidas y mas legibles al momento de concatenar.
"""

#ejemplo 1
print(f"El resultado de la suma de 5 + 15 = {5+15}")

#ejemplo 2
nombre = 'Patrcik'
estatura = 1.75
edad = 26

print(f"Hola {nombre} mides {estatura} y tienes {edad} años.")

#ejemplo 3
nombre = input("¿Cuál es tu nombre?: ")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un segundo número: "))
print(f"Hola {nombre} el resultado de {num_uno} y {num_dos} es: {num_uno + num_dos}")
