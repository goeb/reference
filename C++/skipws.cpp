// skipws flag example
#include <iostream>
#include <sstream>
using namespace std;

int main () {
  unsigned long long a, b, c, d;

  istringstream iss ("  111 000 222 3333");
  iss >> skipws >> a >> b >> c >> d;
  cout << "a=" << a << ", b=" << b << ", c=" << c << ", d=" << d << endl;

  iss.seekg(0);
  iss >> noskipws >> a >> b >> c >> d;
  cout << "a=" << a << ", b=" << b << ", c=" << c << ", d=" << d << endl;
  return 0;
}
