'''
cadena = str(input("Dame la cadena"))
def invierte_cadena (texto):
    invierte_cadena = texto [::-1]
    return invierte_cadena
print(invierte_cadena (cadena))
'''
def es_palindromo(texto):
    texto == texto [::1]
    ignora_espacios  = texto.script
    ignora_mayuculas = texto.lower()
if texto == texto [::1]: True
elif ignora_espacios == True: 
    es_palindromo
elif ignora_mayusculas == True:
    es_palindromo
else: False

def prueba_palindromo(texto):
    assert prueba_palindromo("reconocer") == "reconocer"
    assert prueba_palindromo("Amor a Roma") == "Amor a Roma"
prueba_palindromo()
print("Todas las pruebas pasaron correctamente")