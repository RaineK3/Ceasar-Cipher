#method = input("Choose encryption or decryption : ")
message = input("Enter message to encrypt or decrypt : ")
key = int(input("Enter the key number : "))

upperA_code = ord('A')
upperZ_code = ord('Z')
lowera_code = ord('a')
lowerz_code = ord('z')
encryptedMessage = ""
for char in message:
  char_code = ord(char)
  ascii_code = upperA_code + (char_code - upperA_code + key) % 26
  if char_code >= upperA_code and  char_code <= upperZ_code:
    ascii_code = upperA_code + (char_code - upperA_code + key) % 26
    encryptedMessage += chr(ascii_code)
  elif char_code >= lowera_code and  char_code <= lowerz_code:
    ascii_code = lowera_code + (char_code - lowera_code + key) % 26
    encryptedMessage += chr(ascii_code)

print(encryptedMessage)