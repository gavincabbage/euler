// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

//// Overflow nonsense? wrong answer anyway

#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    unsigned long root = (unsigned long) sqrt( ( (double) n) + 1 );
    for (unsigned long x = 2; x < root; x++) {
        if (n % x == 0) {
            return 0;
        }
    }
    return 1;
}

unsigned long getMaxPrimeFactor(int n) {
    unsigned long quotient = (unsigned long) n;
    unsigned long current = 2;
    unsigned long ndx = 0;
    while (!isPrime(quotient)) {
        if ( isPrime(current) && (quotient % current == 0) ) {
            quotient = quotient / current;
        }
        current += 1;
    }
    return quotient;
}

int main() {
    unsigned long number = 600851475143;
    printf("%lu", getMaxPrimeFactor(number));
    return 0;
}
