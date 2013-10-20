#include <iostream>
#include <vector>
using namespace std;

class A {
public:
	string name;
	int value;
};

void add(vector <A> & aList, string name, int value) {
	A a;
	a.name = name;
	a.value = value;
	aList.push_back(a);
}

main() {
	vector<A> AList;
	add(AList, "toto", 333);
	add(AList, "tu tou you tou", 4545);
	add(AList, "mister Brown is happy.", 22);

	vector<A>::iterator It = AList.begin();
	while ( It != AList.end() ) {
		A a = *It;
		cout << "XX:" << a.name << "\n";
		It++;
	}

}
