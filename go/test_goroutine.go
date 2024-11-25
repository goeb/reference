/* Run with: go run test_goroutine.go
 */
package main

import (
	"fmt"
	"sync"
	"time"
)

var f_count, g_count int

func f() {
	for i := 0; i < 5; i++ {
		fmt.Println("f: f_count=", f_count)
		f_count++
		time.Sleep(100 * time.Millisecond)
	}
}

func g() {
	for i := 0; i < 5; i++ {
		fmt.Println("g: g_count=", g_count)
		g_count++
		time.Sleep(100 * time.Millisecond)
	}
}

func main() {
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		f()
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		g()
	}()

	wg.Wait()
	fmt.Println("end")
}

