"""
Este programa imprime en pantalla la Sucesión de Fibonacci desde el 
0 hasta el número 1597 de manera horizontal.
"""

print("=====================")
print("SUCESIÓN DE FIBONACCI")
print("=====================")

num_uno, num_dos = 0, 1
while num_uno < 1598:
    print(num_uno, num_dos, end=" ")
    num_uno += num_dos
    num_dos += num_uno
