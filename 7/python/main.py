# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

def is_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def get_nth_prime(n):
    count = 1
    candidate = 2
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

print(get_nth_prime(10001))
