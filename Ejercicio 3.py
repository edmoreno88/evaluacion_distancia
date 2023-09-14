
def es_palindromo(palabra):
    #convertir la palabra a minusculas para hacer la comparacion 
    palabra = palabra.lower()

#eliminar espacios en blanco de la palabra
    palabra = palabra.replace(" ","")

#comparamos la palabra con su reverso
    if palabra == palabra[::-1]:
        return True
    else:
        return False

#solicitamos a el usuario que ingrese una palabra    
palabra = input("ingresa una palabra: ")

#verificamos si la palabra es un palindromo
if es_palindromo(palabra):
    print(f"'{palabra}' es un palindromo.")
else:
    print(f"'{palabra}' no un palindromo.")