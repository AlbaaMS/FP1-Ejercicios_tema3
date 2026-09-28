'''
cadena = str(input("Dame la cadena"))
def invierte_cadena (texto):
    invierte_cadena = texto [::-1]
    return invierte_cadena
print(invierte_cadena (cadena))
'''
# cadenas.py

def es_palindromo(cadena, ignora_espacios=False, ignora_mayusculas=False):
    """
    Devuelve True si la cadena es un palíndromo, False en caso contrario.
    
    Parámetros:
    - cadena (str): La cadena a evaluar.
    - ignora_espacios (bool): Si es True, elimina los espacios del texto.
    - ignora_mayusculas (bool): Si es True, convierte todo a minúsculas.
    """
    texto = cadena

    if ignora_mayusculas:
        texto = texto.lower()

    if ignora_espacios:
        texto = texto.replace(" ", "")

    return texto == texto[::-1]


def probar_es_palindromo():
    # Palíndromos simples (palabras individuales)
    assert es_palindromo("reconocer") == True
    assert es_palindromo("rotor") == True
    assert es_palindromo("radar") == True
    
    # Sensible a mayúsculas y espacios (por defecto False)
    assert es_palindromo("Ana") == False
    assert es_palindromo("Ana", ignora_mayusculas=True) == True

    # Frases con espacios
    assert es_palindromo("Amor a Roma") == False
    assert es_palindromo("Amor a Roma", ignora_espacios=True, ignora_mayusculas=True) == True
    assert es_palindromo("Luz azul", ignora_espacios=True, ignora_mayusculas=True) == True
    assert es_palindromo("yo hago yoga hoy", ignora_espacios=True) == True

    # Casos que no son palíndromos
    assert es_palindromo("python") == False
    assert es_palindromo("Hola Mundo", ignora_espacios=True, ignora_mayusculas=True) == False

    print("¡Todas las pruebas pasaron correctamente!")