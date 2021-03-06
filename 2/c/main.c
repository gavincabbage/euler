// Each new term in the Fibonacci sequence is generated by adding the previous
// two terms. By starting with 1 and 2, the first 10 terms will be:
//
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do not
// exceed four million, find the sum of the even-valued terms.

#include <stdio.h>

int main() {

    int total = 0;
    int limit = 4000000;

    int prev2 = 1;
    int prev = 1;
    int term = 2;

    while (term <= limit) {
        if (term % 2 == 0) {
            total += term;
        }
        prev2 = prev;
        prev = term;
        term = prev + prev2;
    }

    printf("%d", total);
    return 0;

}
