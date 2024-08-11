"""
Este método hace que ingreses valores tanto como string, enteros, ect.
"""

#Metodo 1
nombre = 'Patrick'
edad = 26

print("Hola {} tienes {} años.".format(nombre, edad))

#Metodo 2
print("Hola {nombre} tienes {edad} años.".format(nombre = 'Patrick', edad = 26))

#Metodo 3
nombre = 'Patrick'
edad = 26

print("Hola {1} tienes {0} años.".format(edad, nombre))
