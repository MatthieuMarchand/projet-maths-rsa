import unicodedata

dic = "abcdefghijklmnopqrstuvwxyz !?.'"


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def safe_string(string):
    return ''.join(char if (char in dic) else "" for char in strip_accents(string))


def encrypt(message, public_key):
    N, c = public_key
    char_map = {char: idx + 1 for idx, char in enumerate(dic)}
    encrypted_message = [pow(char_map[char], c, N) for char in safe_string(message)]
    return encrypted_message


def decrypt(encrypted_message, private_key, public_key):
    N, c = public_key

    reverse_map = {index + 1: char for index, char in enumerate(dic)}
    message = ''.join(reverse_map[pow(num, private_key, N)] for num in encrypted_message)
    return message
