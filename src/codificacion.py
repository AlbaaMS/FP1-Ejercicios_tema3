alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def letra_a_posicion(letra):
    if letra in alfabeto:
        return alfabeto.find(letra)
    else:
        return None
    
def posicion_a_letra(posicion):
    if 0 <= posicion < len(alfabeto):
        return alfabeto[posicion]

def cifra_cesar (texto_codificar, clave):
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
            posicion = (posicion + clave)
            res += posicion_a_letra(posicion) 
        else:
            res += i

    return res

cifra_cesar("Hola Mundo",1)
