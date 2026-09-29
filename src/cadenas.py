#Ejercicio 1
def invierte_cadena(texto: str) -> str:
    '''
    Invierte el texto que recibe por parámetro
    Parámetro:
    texto (str): El texto a invertir
    Devuelve:
    (str) El texto recibido, al revés
    '''
    res = ""
    for c in texto:
        res= c + res
    return res

def es_palindromo(texto: str, ignora_espacios: bool= False, ignora_mayusculas: bool = False ) -> bool:
    """
    Devuelve True si la cadena es un palíndromo, False en caso contrario.
    Parámetros:
    - texto (str): La cadena a evaluar.
    - ignora_espacios (bool): Si es True, elimina los espacios del texto.
    - ignora_mayusculas (bool): Si es True, convierte todo a minúsculas.
    """
    if ignora_espacios:
        texto = texto.replace("","")

    if ignora_mayusculas:
        texto = texto.lower()

    return texto == invierte_cadena(texto)

def estiliza_mensaje(texto:str, alterna_may_min: bool = True, sustituye_espacios: str = " ") -> str:
    res = ""
    toca_mayusculas = True
    for c in texto:
        if alterna_may_min and c.isalpha():
            if toca_mayusculas:
                c = c.upper()
            else:
                c= c.lower()
                toca_mayusculas = not toca_mayusculas
        res += c
        
   # TODO implementar sustituye espacios


    