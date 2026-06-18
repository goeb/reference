// Go versions 1.18 and 1.22 do not behave the same when executing errors.As().
//
// ~/go/bin/go1.18 run test-errors.As.go
// ok= false
//
// ~/go/bin/go1.22.2 run test-errors.As.go
// MyErrorContainer.Unwrap()
// ok= true

package main

import (
	"errors"
	"fmt"
)

type MyCustomErr struct{}

func (e *MyCustomErr) Error() string {
	return "my custom error"
}

type MyErrorContainer struct {
	errs []error
}

// Never called, but method is necessary for error interface
func (e *MyErrorContainer) Error() string {
	fmt.Println("MyErrorContainer.Error()")
	return "xxxxxx"
}

// Unwrap is called with go1.22 but not with go1.18
func (e *MyErrorContainer) Unwrap() []error {
	fmt.Println("MyErrorContainer.Unwrap()")
	return e.errs
}

func main() {
	e1 := &MyCustomErr{}
	e2 := &MyErrorContainer{errs: []error{e1}}
	var customErr *MyCustomErr
	ok := errors.As(e2, &customErr)
	fmt.Println("ok=", ok)
}
