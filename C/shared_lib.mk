
all:
	gcc -fPIC -c shared_lib.c
	gcc -shared -Wl,-soname,libfff.so -o libfff.so shared_lib.o

	gcc -fPIC -c shared_lib2.c
	gcc -fPIC -c shared_object.c
	gcc -shared -Wl,-soname,libf2.so -o libf2.so shared_lib2.o shared_object.o

	gcc -c main_using_sharedlibs.c
	gcc -o main_using_sharedlibs main_using_sharedlibs.o -lf2 -L. -lfff


