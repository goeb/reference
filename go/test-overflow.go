// This program illustrates integer overflows
//
// go run test-overflow.go 1
// MaxUint=0xffffffffffffffff
// MaxInt=0x7fffffffffffffff
// MinInt=0x-8000000000000000
// MinInt - 1=0x7fffffffffffffff
// MaxUint + 1=0x0
// MaxInt + 1=0x-8000000000000000
 
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	const MaxUint = ^uint(0) 
	const MaxInt = int(MaxUint >> 1) 
	const MinInt = -MaxInt - 1

	fmt.Printf("MaxUint=0x%x\n", MaxUint)
	fmt.Printf("MaxInt=0x%x\n", MaxInt)
	fmt.Printf("MinInt=0x%x\n", MinInt)

	argi, _ := strconv.Atoi(os.Args[1])

	x := MinInt - argi
	fmt.Printf("MinInt - %v=0x%x\n", argi, x)

	y := MaxUint + uint(argi)
	fmt.Printf("MaxUint + %v=0x%x\n", argi, y)

	z := MaxInt + argi
	fmt.Printf("MaxInt + %v=0x%x\n", argi, z)
}
