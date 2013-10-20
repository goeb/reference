
CPPFLAGS=-g -Wall -W -pedantic -O0 -fprofile-arcs -ftest-coverage
#CPPFLAGS=-g -Wall -W -pedantic -O0

all:
	g++ -c ClassA.cpp $(CPPFLAGS) -fPIC
	g++ -c ClassB.cpp $(CPPFLAGS) -fPIC
	#g++ -shared -soname,libtest_gcov.so -o libtest_gcov.so ClassA.o ClassB.o
	g++ -shared -o libtest_gcov.so ClassA.o ClassB.o $(CPPFLAGS)
	g++ -c test_gcov.cpp
	g++ -o test_gcov test_gcov.o $(CPPFLAGS) -L. -ltest_gcov -ldl
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
	test_gcov

with_dlopen:
	g++ -c ClassA.cpp $(CPPFLAGS) -fPIC
	g++ -c ClassB.cpp $(CPPFLAGS) -fPIC
	g++ -shared -o libtest_gcov.so ClassA.o ClassB.o $(CPPFLAGS)
	g++ -c test_gcov.cpp
	g++ -o test_gcov test_gcov.o $(CPPFLAGS) -ldl
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
	test_gcov

