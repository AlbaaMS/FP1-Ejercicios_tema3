'''
from cadenas import estiliza_mensaje 
def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=False, usa_dieresis=True, sustituye_espacios="-") == "Hölä-Mündö"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"
test_estiliza_mensaje()
print("Todas las pruebas pasaron correctamente.")
'''
#Ejercicio 1
def invierte_cadena(texto):
    return texto[::-1]
# yo había puesto cadena = [ "Texto de prueba", "", "seres" ], corregido con gemini ai
def cadena_test():
    assert invierte_cadena("") == ""
    assert invierte_cadena("Texto de prueba") == "abeurp ed otxeT"
    assert invierte_cadena("seres") == "seres"  # Palíndromo

cadena_test()
print("Todas las pruebas pasaron correctamente")