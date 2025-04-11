#include <any>
#include <string>
#include <stdio.h>

struct A {
	int type;
	std::any value;
};

int main()
{
	std::string name("John");
	std::any a = name;
	printf("name=%s\n", std::any_cast<std::string>(a).c_str());
	a = 333;
	printf("a=%d\n", std::any_cast<int>(a));

	A my_a;
	my_a.type = 1;
	my_a.value = std::string("hello");

	A my_b;
	my_b = my_a;

	printf("my_b: %d, %s\n",
			std::any_cast<int>(my_b.type),
			std::any_cast<std::string>(my_b.value).c_str());
}
