"""
Este programa registra o agenda usando diccionario.
"""

print("==================")
print("AGENDA DICCIONARIO")
print("==================")

agenda = {}

cantidad = int(input("Indique la cantidad de contactos a agendar: "))
if cantidad > 0:
    print("--- AGENDA ---")
    for c in range(cantidad):
        nombre = input("Nombre de contacto: ")
        if nombre in agenda:
            print(f"{nombre} ya registrado, su número es {agenda[nombre]}")
        else:
            agenda[nombre] = input("Indique número telefónico: ")
    print("\nListado de contactos")
    for nombre, numero in agenda.items():
        print(f"{nombre} --> {numero}")
else:
    print("La cantidad de contactos debe ser positiva")
