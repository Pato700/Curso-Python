"""
Este programa eliminara una palabra que forme parte de una cadena de caracteres.
"""

frase = input("Introdeuce una frase: ")
palabra = input("Introduce la palabra a eliminar: ")
palabra_eliminada = ''

indice = frase.find(palabra)
palabra_eliminada = frase[0 : indice] + frase[indice + len(palabra) + 1 : ]

print(f"\nCadena con palabra eliminada: {palabra_eliminada}")
