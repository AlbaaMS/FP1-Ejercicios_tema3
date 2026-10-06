
from cadenas import * 

def test_invierte_cadena():
    print("Probando invierte_cadena...")
    assert invierte_cadena("") == ""
    assert invierte_cadena("Texto de prueba") == "abeurp ed otxeT"
    assert invierte_cadena("seres") == "seres"

def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1", alterna_may_min = True) == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, sustituye_espacios="_") == "HoLa_MuNdO"

def probar_es_palindromo():
    assert es_palindromo("reconocer") == True
    assert es_palindromo("rotor") == True
    # Sensible a mayúsculas
    assert es_palindromo("Ana", ignora_mayusculas = True) == True
    # Frases con espacios
    assert es_palindromo("Amor a Roma", ignora_mayusculas = True, ignora_espacios = True) == True
    assert es_palindromo("yo hago yoga hoy", ignora_espacios = True) == True #assertation error??
    # Casos que no son palíndromos
    assert es_palindromo("python") == False
    assert es_palindromo("Hola Mundo") == False

test_invierte_cadena()
probar_es_palindromo()
test_estiliza_mensaje()
print("Todas las pruebas pasaron correctamente.")
