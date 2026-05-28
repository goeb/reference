package main
import (
    "fmt"
)

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

type Widget struct {
    name string
}

type WrappedWidget struct {
    Widget       // promoted field
    string       // other anonymous field
    price int64  // normal field
}

func test_promoted_struct() {
    widget := Widget{"my widget"}
    wrappedWidget := WrappedWidget{widget, "xyz", 1234}

	fmt.Printf("Widget: named=%s, string=%s, price=%d\n",
        wrappedWidget.name, // name is passed on to the wrapped Widget since it's
                            // the promoted field
        wrappedWidget.string, // We access the anonymous time.Time as Time
        wrappedWidget.price)

    fmt.Printf("Widget named=%s, string=%s, price=%d\n",
        wrappedWidget.Widget.name, // We can also access the Widget directly
                                   // via Widget
        wrappedWidget.string,
        wrappedWidget.price)
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

	test_promoted_struct()
}


