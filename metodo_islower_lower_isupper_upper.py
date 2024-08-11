"""
El método islower valida con false o true si un string está es minúscula.
El metodo lower convierte las todas las letras del string en minúscula.
El método isupper valida con false o true si un string está es mayúscula.
El metodo upper convierte las todas las letras del string en mayúscula.
"""

string = input("Introduce un String: ")

print(f"\nTodas las letras estan en minusculas: {string.islower()}")
string = string.lower()
print(f"String en minuscula: {string}")

print(f"\nTodas las letras estan en mayusculas: {string.isupper()}")
print(f"String en mayuscula: {string.upper()}")
print(f"String original: {string}")
