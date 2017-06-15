# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def eq(a, b):
    root = math.sqrt(a*a + b*b)
    return ( a * (a + root) ) + ( a * b ) + (b * (b + root) )

def solve_for_a_b_c():
    for a in range(1, 998):
        for b in range(1, 998):
            if eq(a, b) == 500000:
                return a, b, 1000 - a - b

a, b, c = solve_for_a_b_c()
print(a*b*c)
