from codificacion import cifra_cesar
def test_cifra_cesar():
    print("Probando la función cesar...")
    assert(cifra_cesar("Hola Mundo", 1)) == "Ipmb Nvñep"
    assert(cifra_cesar("Hola Mundo", 13)) == "Téxn YBzpé"
    assert(cifra_cesar("Hola Mundo", 66)) == "Hola Mundo"
test_cifra_cesar()
print("Todas las pruebas pasaron correctamente")

