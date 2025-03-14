from sympy import mod_inverse


# This is a fake random function for demo purposes
def generate_prime_pair():
    return [101, 103]


def generate_keys():
    p, q = generate_prime_pair()

    N = p * q
    n = (p - 1) * (q - 1)

    c = 65537

    d = mod_inverse(c, n)

    public_key = (N, c)
    private_key = d

    return public_key, private_key
