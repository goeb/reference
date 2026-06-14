// go run test-litteral-strings.go
// a=5c7833305c783331
// b=3031
// a==b false
// x=3031303230330a3034303530360a
// y=3031303230330a3034303530360a
// x==y true

package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := `\x30\x31`
	b := "\x30\x31"
	fmt.Printf("a=%x\n", a)
	fmt.Printf("b=%x\n", b)
	fmt.Println("a==b", a == b)

	x := []byte(`010203
040506
`)
	y := []byte("010203\n040506\n")
	fmt.Printf("x=%x\n", x)
	fmt.Printf("y=%x\n", y)
	fmt.Println("x==y", reflect.DeepEqual(x, y))
}

