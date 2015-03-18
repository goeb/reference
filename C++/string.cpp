#include <iostream>

void test(const std::string &s)
{
	std::cout << "s.size()=" << s.size() <<
		", s.capacity()=" << s.capacity() << std::endl;
}

main()
{
	std::string s = "";
	s += '\0';
	s += 'x';
	test(s);

	std::string s2 = "";
	s2 += s[0];
	s2 += s[1];

	test(s2);

	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	s2 += "hello world!";
	test(s2);
	std::string s3;
	s3.assign(s2.c_str()+1);
	std::cout << "s3: ";
	test(s3);
}
