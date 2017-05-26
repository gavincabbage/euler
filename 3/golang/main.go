// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

package main

import (
    "fmt"
    "math"
)

func isPrime(n int) bool {
    for x := 2; x < int(math.Sqrt(float64(n))+1); x++ {
        if n % x == 0 {
            return false
        }
    }
    return true
}

func getPrimeFactorization(n int) []int {
    primeFactors := make([]int, 1)
    quotient := n
    current := 2
    for !isPrime(quotient) {
        if isPrime(current) && quotient % current == 0 {
            primeFactors = append(primeFactors, current)
            quotient = quotient / current
        }
        current += 1
    }
    return append(primeFactors, quotient)
}

func main() {
    number := 600851475143
    primeFactors := getPrimeFactorization(number)
    fmt.Println(primeFactors[len(primeFactors)-1])
}
