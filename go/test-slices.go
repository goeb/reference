// This program illustrates the use of slices.Sort and slices.SortFunc.
//
// go run test-slices.go
// init: map[apple:16 banana:65 orange:21]
// sort1: [apple orange banana]
// sort2: [apple orange banana]
//
// The last 2 lines may vary if not sorted with slices.Sort / slices.SortFunc.

package main

import (
	"fmt"
	"slices"
)

func main() {
	m := map[string]int{}
	m["orange"] = 21
	m["banana"] = 65
	m["apple"] = 16

	fmt.Printf("init: %v\n", m)

	sort1(m)
	sort2(m)
}

// Extract the keys and sort them by their numeric value
// Using slices.SortFunc
func sort1(m map[string]int) {
	keys := []string{}
	for k := range m {
		keys = append(keys, k)
	}

	slices.SortFunc(keys, func(a string, b string) (int) {
		return m[a] - m[b]
	})


	fmt.Printf("sort1: %v\n", keys)
}

// Extract the keys and sort them by their numeric value
// Using slices.Sort
func sort2(m map[string]int) {
	reverse := map[int]string{}
	indices := []int{}
	for i, v := range m {
		reverse[v] = i
		indices = append(indices, v)
	}

	slices.Sort(indices)

	keys := []string{}
	for _, v := range indices {
		keys = append(keys, reverse[v])
	}
	fmt.Printf("sort2: %v\n", keys)
}
