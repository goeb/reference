// go run test-init.go
// getString
// init-1
// init-2
// main

package main

import "fmt"

var str string = getString()

func main() {
	fmt.Println("main")
}

func init() {
	fmt.Println("init-1")
}

func init() {
	fmt.Println("init-2")
}

func getString() string {
	fmt.Println("getString")
	return "hello"
}
