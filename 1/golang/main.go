// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

package main

import "fmt"

func main() {

    total := 0
    
    for number := 0; number < 1000; number++ {
        if number % 3 == 0 || number % 5 == 0 {
            total += number
        }
    }

    fmt.Println(total)

}
