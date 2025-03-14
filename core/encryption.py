dic = "abcdefghijklmnopqrstuvwxyz!?.' "


def encrypt(message, public_key):
    N, c = public_key
    char_map = {char: idx + 1 for idx, char in enumerate(dic)}
    encrypted_message = [(pow(char_map[char], c)) % N for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key, public_key):
    N, c = public_key
    
    reverse_map = {index + 1: char for index, char in enumerate(dic)}
    message = ''.join(reverse_map[(pow(num, private_key)) % N] for num in encrypted_message)
    return message
