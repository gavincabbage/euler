# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

# Notes:
#
# Have to find the minimal common prime factorization. Example for 10:
#
# 5*2*2*2*3*3*7 = 2520
#
# 2 = 2
# 3 = 3
# 4 = 2*2
# 5 = 5
# 6 = 3*2
# 7 = 7
# 8 = 2*2*2
# 9 = 3*3
# 10 = 5*2

import math

def is_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def prime_factors(number):
    factors = []
    if number < 2:
        return factors
    current = 2
    while not is_prime(number):
        if number % current == 0:
            factors.append(current)
            number = number // current
        else:
            current = next_prime(current)
    factors.append(number)
    return factors

def common_prime_factors(max):
    common = []
    factors_matrix = [prime_factors(number) for number in range(max+1)]

    max_factor_counts = {}
    for factors in factors_matrix:
        counted = {factor : factors.count(factor) for factor in factors}
        for factor in counted.keys():
            if factor not in max_factor_counts or \
                    counted[factor] > max_factor_counts[factor]:
                max_factor_counts[factor] = counted[factor]
    return max_factor_counts

def product_common_prime_factors(max):
    product = 1
    common_factors = common_prime_factors(max)
    print(common_factors)
    for factor in common_factors:
        product *= factor**common_factors[factor]
    return product

print(product_common_prime_factors(20))
