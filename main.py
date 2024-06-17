from vigenere import translate_text
from helpers import check_act, check_key

while True:
    res = input('You want encrypt or decrypt text?\n'
                '(Enter \'e\' or \'d\')\n'
                '>>>  ').strip()
    mode = check_act(res)

    if not mode:
        print('\n\nThis answer is not valid\n'
              'Only \'e\' or \'d\' are valid\n\n')
        continue
    else:
        break

while True:
    key = input('Enter a random word\n'
                '>>>  ')
    is_valid_key = check_key(key)
    
    if is_valid_key:
        break
    else:
        print('\n\nKey must contain only english letters\n\n')
        continue

text = input('Enter text: '
             '\n>>>  ').upper()

translated = translate_text(text, key, mode)

print('\n===================\n\n')
print(f'The {mode}ed text: {translated}\n\n')

