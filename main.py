import random


def polyalphabetic_cipher(text, alphabet, key, encrypt=True):
    text = ''.join([c for c in text if c in alphabet])
    text = text.upper()
    random.seed(key)
    shifts = [random.randint(0, len(alphabet)) for _ in range(len(text))]
    result = ''
    for i, c in enumerate(text):
        index = alphabet.index(c)
        if encrypt:
            index = (index + shifts[i]) % len(alphabet)
        else:
            index = (index - shifts[i]) % len(alphabet)
        result += alphabet[index]
    return result


def encrypt(text, alphabet, key):
    return polyalphabetic_cipher(text, alphabet, key, True)


def decrypt(text, alphabet, key):
    return polyalphabetic_cipher(text, alphabet, key, False)

text = 'ПОБЕДА!!!'
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = 52152
encrypted_text = encrypt(text, alphabet, key)
print(encrypted_text)  # Выведет 'ЕЖРЬЕС'
decrypted_text = decrypt(encrypted_text, alphabet, key)
print(decrypted_text)  # Выведет 'ПОБЕДА'
