

all:
	g++ -c constructor.cpp -DWITH_MAIN -o main.o
	g++ -c constructor.cpp -fPIC -o constructor.o
	g++ constructor.o -shared -fPIC -o libconstructor.so
	g++ -o constructor main.o -L . -l constructor
