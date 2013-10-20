
all:
	g++ -fPIC -shared -o libWagon.so Wagon.cpp -g
	g++ -fPIC -shared -o libshared.so shared.cpp -g
	g++ -o main main.cpp -g -ldl -lWagon -L.
