#include <map>
#include <string>
#include <variant>

struct A {
	std::string name;
	std::string value;
};

struct B {
	int size;
	A a1;
	A a2;
};

int main()
{
	std::map<std::string, std::variant<int, A, B> > table;
	A a0 = A();
	a0.name = "name-a";
	table["1"] = a0;

	B b0 = B();
	b0.size = 42;

	table["2"] = b0;

	A a = std::get<A>(table["1"]);
	printf("a.name=%s\n", a.name.c_str());

	B b = std::get<B>(table["2"]);
	printf("b.size=%d\n", b.size);

	b = std::get<B>(table["1"]); // throws std::bad_variant_access
	
}
