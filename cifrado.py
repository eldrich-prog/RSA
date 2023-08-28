def encriptar(message, codigo):
    """ Returns an cryoted arrat with a key """
    array_ascii = []

    for character in message:
        array_ascii.append(ord(character) + codigo)

    return array_ascii

def desincriptar(array_ascii, codigo):
    array_message = []
    for character in array_ascii:
        array_message.append(chr(character - codigo))
    return array_message

def imprimir(array):
    print("\nEl mensaje es: ")
    for character in array:
        print(character, end="")

if __name__ == '__main__':

    archivo = input("Mensaje a encriptar: ")
    codigo = int(input("Ingresa el codigo: "))
    encriptado = encriptar(archivo, codigo)

    print("Mensaje encriptado: ", encriptado)
    codigo2 = int(input("\nPara desincriptar ingresa el codigo: "))
    message = desincriptar(encriptado, codigo2)
    print("Array desincriptado: ", message)

    imprimir(message)