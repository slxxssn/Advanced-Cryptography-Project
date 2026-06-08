def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.upper()) + shift - 65) % 26 + 65)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.upper()) - shift - 65) % 26 + 65)
        else:
            result += char

    return result


def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char.upper()) + shift - 65) % 26 + 65)
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char.upper()) - shift - 65) % 26 + 65)
            key_index += 1
        else:
            result += char

    return result