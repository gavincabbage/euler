// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10 001st prime number?

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

func getNthPrime(n int) int {
    count, candidate := 1, 2
    for count < n {
        candidate += 1
        if isPrime(candidate) {
            count += 1
        }
    }
    return candidate
}

func main() {
    fmt.Println(getNthPrime(10001))
}
