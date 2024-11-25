/* Run with: go run test_goroutine.go
 */
package main

import (
	"fmt"
	"sync"
	"time"
)

var f_count, g_count int

func f(ch chan string) {
	for i := 0; i < 5; i++ {
		fmt.Println("f: f_count=", f_count)
		f_count++
		time.Sleep(100 * time.Millisecond)
		ch <- "hello from f"
	}
}

func g(ch chan string) {
	for i := 0; i < 5; i++ {
		fmt.Println("g: g_count=", g_count)
		g_count++
		msg := <-ch
		fmt.Println("g: received: ", msg)
		time.Sleep(100 * time.Millisecond)
	}
}

func main() {
	messages := make(chan string)

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		f(messages)
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		g(messages)
	}()

	wg.Wait()
	fmt.Println("end")
}

