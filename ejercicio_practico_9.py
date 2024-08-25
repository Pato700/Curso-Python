"""
El programa solicita una frase desde teclado, ya sea una letra, un numero o caracter especial. 
Posteriormente, el programa debera imprimir en pantalla la frase ingresada desde teclado, 
"sin vocales", y en caso de que el caracter en especifico sea parte de la frase, el bucle debera 
finalizar su ejecucion.

requeriemientos indispensables:
utilizar un ciclo o bucle, ya sea while o for.
considerar que el usuario puede ingresar vocales en mayuscula o minusculas
"""

# Solicitar al usuario que ingrese una frase
string = input("Ingresa una frase: ")

# Solicitar al usuario que ingrese un carácter específico
letter = input("Ingresa un carácter específico para terminar el bucle: ")

# Recorrer cada carácter en la frase
for character in string:
    if character.lower() == letter.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character, end = "")
