# upper_letters: 65-90
# lower_letters: 97-122

def encrypt(text, keys, key_index=0, translated=''):
    if len(text) == 0: 
        return translated
    char = text[0]
    char_code = ord(char)
    if key_index >= len(keys):
        key_index = 0
    if char_code in range(65, 91):
        translated += chr(((char_code + keys[key_index]) % 26) + 65)
    else: 
        translated += char
    return encrypt(text[1:], keys, key_index + 1, translated)

def decrypt(text, keys, key_index=0, translated=''): 
    if len(text) == 0: 
        return translated
    char = text[0]
    char_code = ord(char)
    if key_index >= len(keys):
        key_index = 0
    if char_code in range(65, 91):
        translated += chr(((char_code - keys[key_index]) % 26) + 65)
    else: 
        translated += char
    return decrypt(text[1:], keys, key_index + 1, translated)


def translate_text(text, key, mode):
    keys = [ord(i) for i in key.upper()]
    if mode == 'encrypt':
        return encrypt(text, keys)
    elif mode == 'decrypt':
        return decrypt(text, keys)
        
    


    