"""
Permite ordenar una lista, tanto en orden ascendente o descendente, 
dependiendo de nuestras nesesidades
"""
numeros = [5, 3, 1, 2, 4]
vocales = ["o", "u", "a", "i", "e"]

print(f"Lista numeros: {numeros}")

numeros.sort()
print(f"\nLista numeros: {numeros}")

numeros.sort(reverse=True)
print(f"\nLista numeros: {numeros}")

#Lista vocales

print(f"\n Lista vocales: {vocales}")

vocales.sort()
print(f"\nLista vocales: {vocales}")

vocales.sort(reverse=True)
print(f"\nLista vocales: {vocales}")
