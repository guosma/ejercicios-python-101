"""
Completar la funcion para que devuelva la "frase" pasada como parámetro
reemplazadas todas sus vocales con la "a" (o cualquier otra "vocal" que se
pase como parámetro)
"""


from hashlib import new


def cambia_vocales(frase:str, vocal="a") -> str:
    
    vocales = ['a','e','i','o','u']
    
    if vocal in vocales:
        vocales.remove(vocal)

    new_frase = frase
    
    for letra in frase:

        if letra in vocales:
            new_frase = new_frase.replace(letra,vocal)
    
    return new_frase


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR 

assert cambia_vocales("hola") == "hala"
assert cambia_vocales("Juan Carlos") == "Jaan Carlas"
assert cambia_vocales("Pepito", "e") == "Pepete"
assert cambia_vocales(vocal="i", frase="me llamo juan") == "mi llimi jiin"

print('Ejercicio terminado OK')