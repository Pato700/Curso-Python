"""
Con estos métodos es posible alinear el texto que imprimimos en pantalla, de acuerdo a
nuestras nesesidades, es decir, podemos alinear una impresión en pantalla, 
"""

string = 'menu'

print("Métodos con espacios:")
print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))

print("\nMétodos con carácter:")
print(string.center(20, "="))
print(string.ljust(20, "="))
print(string.rjust(20, "="))

print("\nVariable modificada:")
string = string.center(10, "=")
print(string)
