
#include <termios.h>
#include <unistd.h>

#include <string.h>
#include <string>
#include <list>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <signal.h>


std::list<void*> mallocList;
std::list<char*> newList;
std::list<std::string> stringList;
const int CHUNK_SIZE = 1024*1024; // 1 MB
int level = 0;



static struct termios oldt, newt;
void init_terminal()
{
	//system ("/bin/stty raw");

    /*tcgetattr gets the parameters of the current terminal
    STDIN_FILENO will tell tcgetattr that it should write the settings
    of stdin to oldt*/
    tcgetattr( STDIN_FILENO, &oldt);
    /*now the settings will be copied*/
    newt = oldt;

    /*ICANON normally takes care that one line at a time will be processed
    that means it will return if it sees a "\n" or an EOF or an EOL*/
    newt.c_lflag &= ~(ICANON);          

    /*Those new settings will be set to STDIN
    TCSANOW tells tcsetattr to change attributes immediately. */
    tcsetattr( STDIN_FILENO, TCSANOW, &newt);

}

void restore_terminal()
{
	tcsetattr( STDIN_FILENO, TCSANOW, &oldt);
}

void do_new() 
{
	char *x = new char[CHUNK_SIZE];
	memset(x, 0xAB, CHUNK_SIZE);
	newList.push_back(x);
	printf("new: %d chunks\n", newList.size());	
}

void do_delete()
{
	if (newList.size() > 0) {
		char *x = newList.front();
		delete[] x;
		newList.pop_front();
		printf("delete: %d chunks remaining\n", newList.size());
	} else {
		printf("delete: nothing to delete\n");
	}
}

void do_new_string() 
{
	char *x = new char[CHUNK_SIZE];
	memset(x, 0xAB, CHUNK_SIZE);
	std::string s;
	s.assign(x, CHUNK_SIZE);
	stringList.push_back(s);
	delete[] x;
	printf("string: %d chunks\n", stringList.size());	
}

void do_delete_string()
{
	if (stringList.size() >0) {
		stringList.pop_front();
		printf("delete-string: %d chunks remaining\n", stringList.size());
	} else {
        printf("delete-string: nothing to delete\n");
    }
}

void do_malloc() 
{
	void *x = malloc(CHUNK_SIZE);
	memset(x, 0xAB, CHUNK_SIZE);
	mallocList.push_back(x);
	printf("malloc: %d chunks\n", mallocList.size());	
}

void do_free()
{
	if (mallocList.size() > 0) {
		void * x = mallocList.front();
		free(x);
		mallocList.pop_front();
		printf("free: %d chunks remaining\n", mallocList.size());
	} else {
		printf("free: nothing to free\n");
	}
}

int menu();

void do_stack()
{
	level ++;
	char x[CHUNK_SIZE];
	memset(x, 0xCD, CHUNK_SIZE);
	printf("stack: level=%d\n", level);
	while (1) {
		int action = menu();
		if (action == 'u') {
			level--;
			printf("unstack: level=%d\n", level);
			return;
		 } // unstack
	}
}

int menu() {
	printf("m: malloc, f: free, n: new, d: delete, s: stack, u: unstack, L: new-string, l:delete-string, q: quit\n");

	int action = getchar();
	printf("\n");

	if (action == 'm') do_malloc();
	else if (action == 'f') do_free();
	else if (action == 'n') do_new();
	else if (action == 'd') do_delete();
	else if (action == 'L') do_new_string();
	else if (action == 'l') do_delete_string();
	else if (action == 's') do_stack();
	else if (action == 'u') ; // do nothing (managed in do_stack)
	else if (action == 'q') {
		restore_terminal();
		exit(1);
	} else {
		printf("nop\n");
		putchar(action); // 
	}

	return action;
}



void * thread1(void * param)
{
    int i = *(int *)param;
    printf("thread[%d] thread1 starting...\n", i);
    printf("thread[%d] closing...\n", i);

	while (1) menu();

}

#define MESSAGING_MGR_THREAD_SIZE 6*1024*1024

main()
{
	init_terminal();

    pthread_t iThread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_attr_setstacksize(&attr, MESSAGING_MGR_THREAD_SIZE);

	int i = 1;
    int x = pthread_create(&iThread, &attr, thread1, &i);

	while (1) {
		sleep(1);
		//int action = menu();
		
	}
}

