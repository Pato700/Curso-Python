#Crear agenda con diccionarios
agenda = {}

cantidad = int(input("Indique la cantidad de contactos a agendar: "))
if cantidad > 0:
    print("--- AGENDA ---")
    for c in range(0,cantidad):
        nombre = input("Nombre de contacto: ")
        if nombre in agenda:
            print("{} ya registrado, su  número {}".format(nombre,agenda[nombre]))
        else:
            agenda[nombre]=input("Indique número telefónico: ")
            
    print("\nListado de contactos")
    for nombre, numero in agenda.items():
        print(nombre, " --> ", numero)
else:
    print("La cantidad de contactos debe ser positivo")