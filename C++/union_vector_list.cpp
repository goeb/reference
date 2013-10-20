
#include <iostream>
#include <set>
#include <vector>
using namespace std;

main()
{
std::set<std::string > nodesListFromEnv;
std::vector<std::string > nodeList;

nodesListFromEnv.insert("toto");
nodesListFromEnv.insert("titi333");

nodeList.push_back("vector1");
nodeList.push_back("vector2");
nodeList.push_back("vector3");

nodesListFromEnv.insert(nodeList.begin(), nodeList.end());

std::set<std::string >::iterator it;
for (it=nodesListFromEnv.begin(); it!=nodesListFromEnv.end(); it++)
{
    cout << *it << endl;
}

}
