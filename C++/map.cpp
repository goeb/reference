
#include <iostream>
#include <map>

int main ()
{
    std::map<char,int> mymap;
    mymap['a']=10;
    mymap['b']=20;
    mymap.erase ('c');
    mymap.erase ('c');

    std::map<char,int>::iterator it;
    for (it=mymap.begin(); it!=mymap.end(); ++it)
        std::cout << it->first << " => " << it->second << '\n';

    return 0;
}
