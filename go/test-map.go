
package main

import "fmt"

func main() {
	mymap := make(map[int]string)

	mymap[33] = "hello33"

	x, y := mymap[33]
	fmt.Printf("x=%v, y=%v\n", x, y)
	x, y = mymap[44]
	fmt.Printf("x=%v, y=%v\n", x, y)
}
