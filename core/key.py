import random

from sympy import isprime, mod_inverse


def generate_prime(min_val=10_000, max_val=99_999):
    while True:
        num = random.randint(min_val, max_val)
        if isprime(num):
            return num


def generate_prime_pair():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        p = generate_prime()

    return [p, q]


def generate_keys():
    p, q = generate_prime_pair()

    N = p * q
    n = (p - 1) * (q - 1)

    c = pow(2, 16) + 1

    d = mod_inverse(c, n)

    public_key = (N, c)
    private_key = d

    return public_key, private_key
