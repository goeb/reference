#include <iostream>
#include <map>
#include <set>
#include <list>
#include <string>

int main ()
{
  std::map<std::string, std::set<std::string> > mymap;
  std::cout << "sizeof(map)=" << sizeof(mymap) << std::endl;

  std::list<std::string> myList;
  std::cout << "sizeof(list)=" << sizeof(myList) << std::endl;

  std::string myset;
  std::cout << "sizeof(set)=" << sizeof(myset) << std::endl;

  std::string mystring;
  std::cout << "sizeof(string)=" << sizeof(mystring) << std::endl;

  return 0;
}

