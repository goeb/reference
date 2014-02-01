
#include <sstream>
#include <iostream>

main()
{
    std::stringstream fstr;
	fstr << "toto1\n";
	std::cout << "fstr=" << fstr.str();
	fstr.str("");
	fstr << "toto2\n";
	std::cout << "fstr=" << fstr.str();
	fstr.str("");
	fstr << "toto3\n";
	std::cout << "fstr=" << fstr.str();
	fstr.str("");
	fstr << "toto4" "-xxxx" "\n";
	std::cout << "fstr=" << fstr.str();

	fstr.str("");
	fstr << "toto-x1\n";
	fstr << "toto-x2\n";
	fstr << "toto-x3\n";
	fstr << "toto-x4";

    fstr.str("2;4143456571487684;4143456571487684;7;7;0;8;6;2;1300168545;1300168584;2051;2099;2019;12;13;3;4;0;0;0;1300168584.1;1300182202.1;1300182203.0;1300182284.1;1300182285.0;1360766849.2;1360767052.1;1360767053.0;1360771661.1;1360771666.0;0 xxxxxxx \n"
            "3;4143456571487684;\n"
            "\n"
            "6;4143456571487684;4143456571487684;7;7;0;8;6;2;1300168545;1300168584;2051;2099;2019;12;13;3;4;0;0;0;1300168584.1;1300182202.1;1300182203.0;1300182284.1;1300182285.0;1360766849.2;1360767052.1;1360767053.0;1360771661.1;1360771666.0;0\n"
            "# comment line");

	char cline[1000];
	while (fstr)
	{
		fstr.getline(cline, 999);
		std::cout << "cline=" << cline << "\n";
	}
}
