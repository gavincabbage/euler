# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

number = 600851475143

def is_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def get_prime_factorization(n):
    prime_factors = []
    quotient = n
    current = 2
    while not is_prime(quotient):
        if is_prime(current) and quotient % current == 0:
            prime_factors.append(current)
            quotient = quotient // current
        current += 1
    prime_factors.append(quotient)
    return prime_factors

print(get_prime_factorization(number)[-1:][0])
