import random
from math import gcd

from sympy import mod_inverse

prime_numbers = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def generate_prime():
    return random.choice(prime_numbers)


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()

    N = p * q
    n = (p - 1) * (q - 1)

    c = random.randint(2, n - 1)
    while gcd(c, n) != 1:
        c = random.randint(2, n - 1)

    d = mod_inverse(c, n)

    public_key = (N, c)
    private_key = d

    return public_key, private_key
