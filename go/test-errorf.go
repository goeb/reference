// go run test-errorf.go
// i=0: got UnsupportedIndex: unsupported index: index 0
// i=1: got BadValue: bad value: index 1
// i=2: got a generic error: index 2
// i=3: got <nil>

package main

import (
	"fmt"
	"errors"
)

type UnsupportedIndex struct {
	err error
}

func (e *UnsupportedIndex) Error() string {
	return "unsupported index: " + e.err.Error()
}

func (e *UnsupportedIndex) Unwrap() error {
	return e.err
}

type BadValue struct {
	err error
}

func (e *BadValue) Error() string {
	return "bad value: " + e.err.Error()
}

func (e *BadValue) Unwrap() error {
	return e.err
}

func main() {
	for i := 0; i<4; i++ {
		err := checkThings(i)
		//fmt.Println(err)

		var unsupportedIdxErr *UnsupportedIndex
		var badValErr *BadValue

		fmt.Printf("i=%v: ", i)

		// Check the type of the error here
		if err == nil {
			fmt.Printf("got <nil>\n")
			
		} else if errors.As(err, &unsupportedIdxErr) {
			fmt.Printf("got UnsupportedIndex: %v\n", unsupportedIdxErr)
			
		} else if errors.As(err, &badValErr) {
			fmt.Printf("got BadValue: %v\n", badValErr)
			
		} else {
			fmt.Printf("got a generic error: %v\n", err)
		}
	}
}

func checkThings(index int) error {
	if index == 0 {
		return &UnsupportedIndex{fmt.Errorf("index 0")}
	} else if index == 1 {
		return fmt.Errorf("bad value: %w", &BadValue{errors.New("index 1")})
	} else if index == 2 {
		return fmt.Errorf("index 2")
	} else {
		return nil
	}
}
