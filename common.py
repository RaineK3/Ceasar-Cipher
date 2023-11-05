#encryption and decryption at the same method by using different parameters
from cryptography import cryptography
def common():

  method = input("Choose 'en' for encryption\n'de' for decryption : \n\n")

  if method not in ["en","de"]:
    print(f"Please enter en or de")
    return common()
  
  message = input("Enter message to encrypt or decrypt : ")
  keyeven = int(input("Enter the number of positions down/up for eventh character : "))
  keyodd = int(input("Enter the number of positions down/up for oddth character : "))

  if method == "en":
    ciphertext = cryptography(message,keyeven,keyodd)
    print(f"Ciphertext : {ciphertext}")
  elif method == "de":
    plaintext = cryptography(message,26-keyeven,26-keyodd)
    print(f"Plaintext : {plaintext}")

common()
  
