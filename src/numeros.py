def invierte_numero(numero:int):
    '''
    Recibe número entero como parámetro y devuelve la resultante de invertir los dígitos
    '''
    nuevo_numero = 0
    while numero > 0:
       extraer_cifra = numero % 10
       nuevo_numero = (nuevo_numero * 10) + extraer_cifra
       numero = numero // 10
    return nuevo_numero


def convierte_binario(numero:int):
    '''
    Recibe número en base decimal y lo devuelve en binario
    '''
    binario = 0
    while numero > 0:
        binario = (numero % 2) + binario
        numero = numero // 2
    return binario
print(convierte_binario (5))
# error es que se suman en vez de añadirse por la izquierda los valores de los modulos

