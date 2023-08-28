from __future__ import annotations
from abc import ABC, abstractmethod
import math



class Cryptografy:

    def __init__(self, algorithm: Algorithm) -> None:
        self._algorithm = algorithm

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm 
    
    @algorithm.setter
    def algorithm(self, algorithm: Algorithm) -> None:
        self._algorithm = algorithm

    def encrypt(self, archivo) -> None:
        message = self.open_file(archivo)
        message = self._algorithm.encrypt(message)
        self.save_encrypt(message)


    def decrypt(self, archivo) -> None:
        archivo = self.open_file(archivo)
        message = [int(num) for num in archivo.split(",")]
        message = self._algorithm.decrypt(message)
        self.save_decrypt(message)
    
    def open_file(self, file_name:str) -> list:
        file = open(file_name, "r")
        text = file.read()
        file.close()
        return text
    
    def save_file(self, file_name:str, message:str) -> None:
        file = open(file_name, "w")
        file.write(message)
        file.close()

    def save_encrypt(self, array_message:list) -> None:
        message = ",".join(str(num) for num in array_message)
        self.save_file("encrypt.txt", message)
        print("\nEl mensaje encriptado es:\n", self.open_file("encrypt.txt"))

    def save_decrypt(self, array_message:list) -> None:
        message = "".join(str(num) for num in array_message)
        self.save_file("decrypt.txt", message)
        print("\nEl mensaje desencriptado es:\n\"", self.open_file("decrypt.txt"), "\"")
        
    def public_key(self):
        return self._algorithm.get_public_key()
    
class Algorithm(ABC):

    @abstractmethod
    def encrypt(self) -> int:
        pass

    @abstractmethod
    def decrypt(self) -> int:
        pass

class RSA(Algorithm):

    def __init__(self, p:int, q:int) -> int:
        self._p = p
        self._q = q
        self._modulo = p * q
        self._phi = self.__calculate_phi()
        self._public_key = self.public_key()
        self._private_key = self.priv_key()
    
    def encrypt(self, message:str ) -> int:
        array_ascii = self.str_to_ascii(message)
        message_encrypted = self.array_encrypted(array_ascii)
        return message_encrypted
    
    def decrypt(self, array_ascii:list) -> list:
        message_decrypted = self.array_decrypted(array_ascii)
        message_decrypted = self.ascii_to_str(message_decrypted)
        return message_decrypted
    
    def array_encrypted(self, array_ascii:list) -> list:
        message_encrypted = []
        for character in array_ascii:
            message_encrypted.append(self.encryption_operation(character))
        return message_encrypted
    
    def array_decrypted(self, array_ascii:list) -> list:
        message_decrypted = []
        for character in array_ascii:
            message_decrypted.append(self.decryption_operation(character))
        return message_decrypted
    
    def encryption_operation(self, num_ascii:int) -> int:
        encrypted = pow(num_ascii, self._public_key)
        encrypted = (encrypted % self._modulo)
        return encrypted

    def decryption_operation(self, num_ascii:int) -> int:
        decrypted = pow(num_ascii, self._private_key)
        decrypted = (decrypted % self._modulo)
        return decrypted
    
    def str_to_ascii(self, message:str) -> list:
        array_ascii = []
        for character in message:
            array_ascii.append(ord(character))
        return array_ascii
    
    def ascii_to_str(self, array_ascii:list) -> str:
        message = ""
        for character in array_ascii:
            message += chr(character)
        return message

    def get_public_key(self):
        return self._public_key
    

    def public_key(self, key = 2) -> int:
        if math.gcd(key, self._phi) == 1 and key < self._phi:
            return key
        else:
            return self.public_key(key+1)
    
    def priv_key(self, num = 1) -> int:
        j = (1 + (num * self._phi)) / self._public_key
        if j.is_integer():
            return int(j)
        else:
            return self.priv_key(num+1)
        

    def __calculate_phi(self) -> int:
        # minimo comun multiplo de p-1 y q-1
        phi = int((self._p-1) * (self._q-1) / math.gcd(self._p-1, self._q-1))
        return phi
    
def main(p, q):

    cryptografy_rsa = Cryptografy(RSA(p, q))
    cryptografy_rsa.encrypt("archivo.txt")
    cryptografy_rsa.decrypt("encrypt.txt")
    key = cryptografy_rsa.public_key()
    print("\nLlave publica: ", key)

if __name__ == "__main__":
    #main(401, 409)
    #main(11, 13)
    main(17, 19)