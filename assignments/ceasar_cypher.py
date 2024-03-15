plaintext_message = input('Enter a message: ')
secret_key = int(input('Enter a number from 1-26 for the secret key: '))
ciphertext = ''

for char in plaintext_message:
    if char.isalpha():
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
            new_pos = (ord(char) - start + secret_key) % 26 + start
            new_char = chr(new_pos)
            ciphertext += new_char
    else:
        ciphertext += char

print(f'The ciphertext is : {ciphertext}')
