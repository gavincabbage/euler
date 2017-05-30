# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# Notes:
#
# Product of two 3-digit numbers between 10000 (100*100) and 998001 (999*999).
#
# 988001 possibilities
#
# Six or less likely five digits long.
#
# Palindromes first and second halves match - take 3 numbers.
#
# 10**3 = 1000
#
# 1000 Possibilities!

def largest_palindrome():
    for half in range(998,0,-1):
        palindrome = int( str(half) + str(half)[::-1] )
        for first_factor in range(999,0,-1):
            divided = palindrome / first_factor
            if palindrome % int(divided) == 0 and len(str(int(divided))) == 3:
                return palindrome, first_factor, divided

print(largest_palindrome())
