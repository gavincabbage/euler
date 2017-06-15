// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
// a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

package main

import (
    "fmt"
    "math"
)

func eq(a, b int) float64 {
    af, bf := float64(a), float64(b)
    root := math.Sqrt(af*af + bf*bf)
    return ( af * (af + root) ) + ( af * bf ) + (bf * (bf + root) )
}

func solveForABC() (int, int, int) {
    for a := 1; a < 998; a++ {
        for b := 1; b < 998; b++ {
            if eq(a, b) == float64(500000) {
                return a, b, 1000-a-b
            }
        }
    }
    return 0, 0, 0
}

func main() {
    a, b, c := solveForABC()
    result := a * b * c
    fmt.Println(result)
}
