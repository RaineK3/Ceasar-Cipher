def cryptography():
    upperA_code = ord('A')
    upperZ_code = ord('Z')
    lowera_code = ord('a')
    lowerz_code = ord('z')

    method = input("Choose 'en' for encryption\n'de' for decryption : \n\n")

    if method not in ["en","de"]:
      print(f"Please enter en or de")
      return cryptography()
    
    # if method == "en":
    #     encrypt()
    # elif method == "de":
    #     decrypt()

    # def encrypt():
    def evenorodd(key):
        if key%2 == 0:
            return keyeven
        else:
            return keyodd

    if method == "en":
        message = input("Enter message to encrypt : ")
        # key = int(input("Enter the key number : "))
        keyeven = int(input("Enter the number of positions down/up for eventh character : "))
        keyodd = int(input("Enter the number of positions down/up for oddth character : "))
        encryptedMessage = ""
        for char in message:
            index = message.index(char)
            key = evenorodd(index)
            print(key)
            char_code = ord(char)
            if char_code >= upperA_code and  char_code <= upperZ_code:
                ascii_code = upperA_code + (char_code - upperA_code + key) % 26
                encryptedMessage += chr(ascii_code)
            elif char_code >= lowera_code and  char_code <= lowerz_code:
                ascii_code = lowera_code + (char_code - lowera_code + key) % 26
                encryptedMessage += chr(ascii_code)

        print(encryptedMessage)

    # def decrypt():
    if method == "de":
        message = input("Enter message to decrypt : ")
        # key = int(input("Enter the key number : "))
        keyeven = int(input("Enter the number of positions down/up for eventh character : "))
        keyodd = int(input("Enter the number of positions down/up for oddth character : "))
        decryptedMessage = ""
        for char in message:
            index = message.index(char)
            key = evenorodd(index)
            print(key)
            char_code = ord(char)
            if char_code >= upperA_code and  char_code <= upperZ_code:
                ascii_code = upperA_code + (char_code - upperA_code - key) % 26
                decryptedMessage += chr(ascii_code)
            elif char_code >= lowera_code and  char_code <= lowerz_code:
                ascii_code = lowera_code + (char_code - lowera_code - key) % 26
                decryptedMessage += chr(ascii_code)

        print(decryptedMessage)

cryptography()