def invierte_numero(numero:int):
    '''
    Recibe número entero como parámetro y devuelve la resultante de invertir los dígitos
    '''
    nuevo_numero = 0
    while numero > 0:
       extraer_cifra = numero % 10
       nuevo_numero = (nuevo_numero * 10) + extraer_cifra
       numero //= 10 #siginifca que numero = numero // 10
    return nuevo_numero


def convierte_binario(numero:int):
    '''
    Recibe número en base decimal y lo devuelve en binario
    '''
    if numero == 0:
        return "0"
    
    res = ""
    while numero != 0:
        numero, binario = numero // 2, (numero % 2)
        res += str(binario) + res #concatena el digito que ha salido en "binario" por la izq

    return res

def sumar_divisores_propios(numero:int) -> int:
    '''
    Devuelve la suma de los divisores propios del número recibido
    '''
    res = 0 
    for i in range(1,numero):
        if numero % i == 0: #i es divisor de número
            res += 1
    return res

def clasifica_numero(numero:int) -> str:
    '''
    Recibe un entero y da clasificación de este según la suma de sus divisores propios
    '''
    suma_divisores = sumar_divisores_propios(numero)
    if suma_divisores == numero:
        return "Perfecto"
    elif suma_divisores > numero:
        return "Abundante"
    else:
        return "Deficiente"

def clasifica_rango(limite:int) -> None:
    '''
    Muestra la clasificación de todos los num de 1 al limite
    '''
    for i in range(1, limite + 1):
        print(f"{i}: {clasifica_numero(i)}")

def busca_perfecto(posicion: int) -> int:
    '''
    Busca y devuelve el número perfecto cuya posición se indique.
    Por ejemplo, si posicion es 1, se devuelve el primer número perfecto (6).
    '''
    n = 1
    contador = 0
    while True:
        if clasifica_numero(n) == "PERFECTO":
            contador += 1
            if contador == posicion:
                return n
        n += 1



