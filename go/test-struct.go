package main
import "fmt"

type person struct {
	name string
	age uint8
}

type vehicle struct {
	class string
	age uint8
}

type ephemeral interface {
	getAge() uint8
}

func (self person) getAge() uint8 {
	return self.age
}

func (self vehicle) getAge() uint8 {
	return self.age
}

func isOld(subject ephemeral) bool {
	return subject.getAge() > 50
}

func main() {
	var bob = person{name: "bob", age: 51}
	var bob2 = struct {
		name string
		age uint8
	}{"bob", 51}

	if bob == bob2 {
		fmt.Println("bob == bob2")
	} else {
		fmt.Println("bob != bob2")
	}

	fmt.Println("bob old?", isOld(bob))

	var car vehicle
	fmt.Println("car old?", isOld(car))

}


