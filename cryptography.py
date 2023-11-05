def cryptography(message,keyeven,keyodd):
  upperA_code = ord('A')
  upperZ_code = ord('Z')
  lowera_code = ord('a')
  lowerz_code = ord('z')
  

  def computekey(key):
    key = key % 26
    if key < 0 :
      key = key + 26
    return key
  
  def evenorodd(index):
    if index%2 == 0:
        key = computekey(keyeven)
    else:
        key = computekey(keyodd)
    return key
  start_at = 0
  modifiedmessage = ""
  for char in message:
    index = message.index(char,start_at)
    start_at +=1
    key = evenorodd(index)
    char_code = ord(char)
    if char_code >= upperA_code and  char_code <= upperZ_code:
      ascii_code = upperA_code + (char_code - upperA_code + key) % 26
      modifiedmessage += chr(ascii_code)
    elif char_code >= lowera_code and  char_code <= lowerz_code:
      ascii_code = lowera_code + (char_code - lowera_code + key) % 26
      modifiedmessage += chr(ascii_code)
    else:
      modifiedmessage += char

  return modifiedmessage
