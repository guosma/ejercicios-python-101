"""
Completar la funcion para que devuelva la "frase" pasada como parámetro
reemplazadas todas sus vocales con la "a" (o cualquier otra "vocal" que se
pase como parámetro)
"""


from hashlib import new


def cambia_vocales(frase:str, vocal="a") -> str:
    
    LETRAS = "aeiouAEIOU"
    vocales = ['a','e','i','o','u']
    vocales_mayusculas = ['A','E','I','O','U']
    
    if vocal in vocales:
        vocales.remove(vocal)
    if vocal.upper() in vocales_mayusculas:
        vocales_mayusculas.remove(vocal.upper())
    
    
    for letra in LETRAS:

        if letra in vocales:
            frase = frase.replace(letra,vocal.lower())
        if letra in vocales_mayusculas:
            frase = frase.replace(letra,vocal.upper())
    return frase


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR 

assert cambia_vocales("PEPEpe", "i") == "PIPIpi"
assert cambia_vocales("PEPEpe", "I") == "PIPIpi"
assert cambia_vocales("hola") == "hala"
assert cambia_vocales("Juan Carlos") == "Jaan Carlas"
assert cambia_vocales("Pepito", "e") == "Pepete"
assert cambia_vocales(vocal="i", frase="me llamo juan") == "mi llimi jiin"

print('Ejercicio terminado OK')