def cryptography():
    upperA_code = ord('A')
    upperZ_code = ord('Z')
    lowera_code = ord('a')
    lowerz_code = ord('z')

    method = input("Choose en for encryption\nde for decryption : ")
    message = input("Enter message to encrypt or decrypt : ")
    key = int(input("Enter the key number : "))

    # if method not in ["en","de"]:
    #   print(f"Please enter en or de")
    #   return cryptography()
    
    # if key <= 0 :
    #     print(f"Key must be greater than 0")
    #     return cryptography()

    # if method == "en":
    #     encrypt()
    # elif method == "de":
    #     decrypt()

    # def encrypt():
    if method == "en":
        encryptedMessage = ""
        for char in message:
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
        decryptedMessage = ""
        for char in message:
            char_code = ord(char)
            if char_code >= upperA_code and  char_code <= upperZ_code:
                ascii_code = upperA_code + (char_code - upperA_code - key) % 26
                decryptedMessage += chr(ascii_code)
            elif char_code >= lowera_code and  char_code <= lowerz_code:
                ascii_code = lowera_code + (char_code - lowera_code - key) % 26
                decryptedMessage += chr(ascii_code)

        print(decryptedMessage)

cryptography()