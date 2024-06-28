alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, key):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + key) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f'Your encrypted text is: {cipher_text}\n')


def decryption(cipher_text, key):
    plain_text = ''
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - key) % 26
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += char
    print(f'Your decrypted text is: {plain_text}\n')


run = True
while run:
    what_action = input("Which action you want?[encrypt/decrypt/quit]: ").lower()
    if what_action == 'encrypt':
        text = input("Enter the text: ").lower()
        shift_key = int(input("Enter shift Key: "))
        encryption(text, shift_key)
        continue
    elif what_action == 'decrypt':
        text = input("Enter the text: ").lower()
        shift_key = int(input("Enter shift Key: "))
        decryption(text, shift_key)
        continue
    elif what_action == 'quit':
        run = False
    else:
        print('Input the right syntax.')
        continue
