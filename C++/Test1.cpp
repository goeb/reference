
#include "Class1.hpp"
#include <iostream>
using namespace std;

namespace Framework {
	namespace Boundaries {
		class Semaphore {
		public:
			int zz;
			void print(void) {
				cout << "Framework::Semaphore\n";
			}
		};
	}
}

namespace N2 {

namespace Framework {
	namespace Boundaries {
		class Semaphore {
		public:
			int zz;
			void print(void) {
				cout << "N2::Framework::Semaphore\n";
			}
		};
	}
}

class Test1 {
public:
	int toto;
	int do_doc(void) {
		cout << "N2::Test1::do_doc()\n";
		N1::Class1 a;
		Framework::Boundaries::Semaphore s;
		a.run();
		s.print();
	}

};

}
