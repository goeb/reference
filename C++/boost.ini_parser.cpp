#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/ini_parser.hpp>
#include <iostream>

/* config.ini should look like this:
 *
 * [toto]
 *     x = 1
 *     y = 33
 *
 * [TOTO]
 *     x = "yoyo"
 *     y = "a b c d"
 *
 */

int main()
{

    boost::property_tree::ptree pt;
    boost::property_tree::ini_parser::read_ini("config.ini", pt);
    std::cout << pt.get<std::string>("toto.x") << std::endl;
    std::cout << pt.get<std::string>("TOTO.y") << std::endl;
}
