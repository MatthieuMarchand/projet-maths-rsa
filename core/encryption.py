dic = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz!?.' "


def encrypt(message, public_key):
    N, c = public_key
    char_map = {char: idx + 1 for idx, char in enumerate(dic)}
    encrypted_message = [(char_map[char] ** c) % N for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key, N):
    reverse_map = {idx + 1: char for idx, char in enumerate(dic)}
    decrypted_message = ''.join(reverse_map[(num ** private_key) % N] for num in encrypted_message)
    return decrypted_message
