import random

from sympy import mod_inverse


# This is a pseudo random function for demo purposes
def generate_prime():
    prime_numbers = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    return random.choice(prime_numbers)


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()

    N = p * q
    n = (p - 1) * (q - 1)

    c = 65537

    d = mod_inverse(c, n)

    public_key = (N, c)
    private_key = d

    return public_key, private_key
