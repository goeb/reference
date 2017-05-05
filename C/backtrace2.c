#include <execinfo.h>
#include <stdio.h>
#include <stdlib.h>

/* Compile with:
 *     gcc backtrace2.c -rdynamic
 *
 * Output:
 * ---- directly to stdout ----
 * ./a.out(print_trace+0x14)[0x80487bf]
 * ./a.out(dummy_function+0xb)[0x8048871]
 * ./a.out(g+0xb)[0x804887f]
 * ./a.out(f+0xb)[0x804888d]
 * ./a.out(main+0x16)[0x80488a6]
 * /lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf6)[0xb75ff276]
 * ./a.out[0x80486d1]
 * ---- to a buffer, then to stdout ----
 * Obtained 7 stack frames.
 * ./a.out(print_trace+0x14) [0x80487bf]
 * ./a.out(dummy_function+0xb) [0x8048871]
 * ./a.out(g+0xb) [0x804887f]
 * ./a.out(f+0xb) [0x804888d]
 * ./a.out(main+0x16) [0x80488a6]
 * /lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf6) [0xb75ff276]
 * ./a.out() [0x80486d1]
 */

/* Obtain a backtrace and print it to stdout. */
void print_trace(void)
{
  void *array[10];
  size_t size;
  char **strings;
  size_t i;

  size = backtrace(array, 10);

  printf("---- directly to stdout ----\n");
  backtrace_symbols_fd(array, size, 1);
  
  printf("---- to a buffer, then to stdout ----\n");
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
