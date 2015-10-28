#include <iostream>
#include <map>
#include <set>
#include <string>

int main ()
{
  std::map<std::string, std::set<std::string> > mymap;
  std::cout << "1. sizeof(mymap)=" << sizeof(mymap) << std::endl;

  mymap["abcdef"].insert("alice");
  mymap["abcdef"].insert("bob");
  std::cout << "2. sizeof(mymap)=" << sizeof(mymap) << std::endl;

  return 0;
}

