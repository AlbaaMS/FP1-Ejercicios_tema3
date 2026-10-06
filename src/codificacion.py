ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def letra_a_posicion(letra:str) -> int:
    if letra in ALFABETO:
        return ALFABETO.find(letra)
    else:
        return None
    
def posicion_a_letra(posicion):
    if 0 <= posicion < len(ALFABETO):
        return ALFABETO[posicion]
    else:
        return None

def cifra_cesar (texto_codificar:str, clave:int) -> str: 
    '''
    Cambiar las letras de una palabra a un número fijo más adelante que viene dado por la clave
    Parámetros:
    Texto a codificar (str)
    Clave (int): número que varía
    '''
    res = ""
    for i in texto_codificar:
        posicion = letra_a_posicion(i)
        if posicion is not None:
            nueva_posicion = (posicion + clave) % len(ALFABETO)
            res += posicion_a_letra(nueva_posicion) 
        else:
            res += i

    return res

def rompe_cesar(texto_codificar:str) -> None:
    for clave in range (len(ALFABETO)):
        texto = cifra_cesar(texto_codificar,-clave) # -clave para que deshaga los cambios con la pos en clave
        print(f"La clave {clave}: texto {texto}")

rompe_cesar("j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!")