package main
import "fmt"
func main() {
	var s string
	s = "123";
	s += "456";
	fmt.Printf("%v\n", s);

	var s2 string
	var strslice = []string{"a", "b", "c"}
	for i := range strslice {
		s2 += strslice[i]
	}
	fmt.Println(s2)
}


