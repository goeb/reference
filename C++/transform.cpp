#include <iostream>
#include <algorithm>
#include <string>

void test_transform(const char* s)
{
	std::string systemTitle = s;
	transform(systemTitle.begin(), systemTitle.end(), systemTitle.begin(),::tolower);
	std::cout << s << " -> " << systemTitle << "\n";
}

main()
{
	test_transform("abcd1234");
	test_transform("ABCD1234AAA999GGG====+++");
	test_transform("123AHJK88888---PPP");
	test_transform("abcd1234&é(-zz");
}
