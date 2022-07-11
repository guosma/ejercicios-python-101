"""
La siguiente funcion busca contar cuantas veces se repite cada palabra.
Por ejemplo de "Hola Juan. Hola Pedro" devuelve {"Hola": 2, "Juan.": 1, "Pedro": 1}
Tarea: Corregir el error de la función para que devuelva el resultado correcto
"""


def contar_palabras(frase:str)->dict:
    """ 
    Esta funcion toma una frase y devuelve un diccionario
    con una llave por cada palabra y un valor igual a la
    cantidad de veces que aparece en la frase
    """
    palabras = frase.split()
    resultados = {}
    for palabra in palabras:
        resultados[palabra] = palabras.count(palabra)
    return resultados


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


f1 = contar_palabras("Hola dijo Juan. Hola dijo pedro")
assert f1['Hola'] == 2, f"La función devolvió {f1['Hola']} y esperamos 2"

f2 = contar_palabras("Hola dijo Juan. Hola dijo pedro. Hola")
assert f2['Hola'] == 3, f"La función devolvió {f1['Hola']} y esperamos 3"

print('Ejercicio terminado OK')