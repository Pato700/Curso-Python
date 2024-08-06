"""
Este programa registra o agenda contactos usando un diccionario.
"""

print("==================")
print("AGENDA DICCIONARIO")
print("==================")

agenda = {}

cantidad = int(input("Indique la cantidad de contactos a agendar: "))
if cantidad > 0:
    print("--- AGENDA ---")
    for _ in range(cantidad):
        nombre = input("Nombre de contacto: ")
        if nombre in agenda:
            print(f"{nombre} contacto ya registrado, su número es {agenda[nombre]}")
        else:
            agenda[nombre] = input("Numero telefónico: ")
    print("\nLista de contactos")
    for nombre, numero in agenda.items():
        print(f"{nombre} --> {numero}")
else:
    print("La cantidad de contactos debe ser positiva")
