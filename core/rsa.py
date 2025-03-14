import random
from sympy import isprime, mod_inverse
from math import gcd 

dic = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz!?.' "

prime_numbers = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def generate_prime_quickly():
    return random.choice(prime_numbers)

# Methode lente pour trouver un premier
def generate_prime(min_val=101, max_val=999):
    while True:
        num = random.randint(min_val, max_val)
        if isprime(num):
            return num

def generate_keys():
    p = generate_prime_quickly()
    q = generate_prime_quickly()
    while p == q:
        q = generate_prime_quickly()
    
    N = p * q
    n = (p - 1) * (q - 1)
    
    c = random.randint(2, n - 1)
    while gcd(c, n) != 1:
        c = random.randint(2, n - 1)
    
    d = mod_inverse(c, n)
    return (N, c), d

def encrypt(message, public_key):
    N, c = public_key
    char_map = {char: idx + 1 for idx, char in enumerate(dic)}
    encrypted_message = [(char_map[char] ** c) % N for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key, N):
    reverse_map = {idx + 1: char for idx, char in enumerate(dic)}
    decrypted_message = ''.join(reverse_map[(num ** private_key) % N] for num in encrypted_message)
    return decrypted_message

# Exemple d'utilisation
public_key, private_key = generate_keys()

print("Clée publique: ", public_key)
print("Clée privée: ", private_key)

message = "bonjour. attention la derniere version du samsung pro est desormais en vente libre sans le protocole new generation. il se peut qu'une version plus moderne soit mise sur le marche mais pour l'instant nous le laissons tel quel pour voir si les consommateurs l'achetent et si oui a quelle quantite. nous lancerons un plan de restructuration du reseau courant janvier ce qui nous permettra de tester ce nouveau produit de facon plus precise. a noter aussi que le nokia a perdu enormement de points sur le marche japonnais. il faudrait peut etre parler aussi de ce point lors de la prochaine reunion. bien a vous."
print("Encryption")
encrypted = encrypt(message, public_key)
print("Message encrypté:", encrypted)
print("Décryptage")
decrypted = decrypt(encrypted, private_key, public_key[0])
print("Message décrypté:", decrypted)
#
# message = input("Message")
# encrypted = encrypt(message, public_key)
# print("Encrypted:", encrypted)
# decrypted = decrypt(encrypted, private_key, public_key[0])
# print("Decrypted:", decrypted)