#include <execinfo.h>
#include <stdio.h>
#include <stdlib.h>

/* Compile with:
 *     gcc backtrace2.c -rdynamic
 */

/* Obtain a backtrace and print it to stdout. */
void print_trace(void)
{
  void *array[10];
  size_t size;
  char **strings;
  size_t i;

  size = backtrace(array, 10);
  strings = backtrace_symbols(array, size);

  printf("Obtained %zd stack frames.\n", size);

  for(i = 0; i < size; i++)
     printf("%s\n", strings[i]);

  free(strings);
}

/* A dummy function to make the backtrace more interesting. */
void dummy_function(void)
{
  print_trace();
}

void g()
{
	dummy_function();
}

void f()
{
	g();
}

int main(void)
{
  f();
  return 0;
}
