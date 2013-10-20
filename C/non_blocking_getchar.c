#include <unistd.h>
#include <termios.h>
#include <stdio.h>
#include <errno.h>

/* set termio so we can do our own input processing */
static void set_termio()
{
    static struct termios orig_termio, rl_termio;
    static int term_set = 0;

    if(term_set == 0) {
        tcgetattr(0, &orig_termio);
        rl_termio = orig_termio;
        rl_termio.c_iflag &= ~(BRKINT|PARMRK|INPCK/*|IUCLC*/|IXON|IXOFF);
        rl_termio.c_iflag |=  (IGNBRK|IGNPAR);
        /* rl_termio.c_oflag &= ~(ONOCR); Costas Sphocleous Irvine,CA */
        rl_termio.c_lflag &= ~(ICANON|ECHO|ECHOE|ECHOK|ECHONL|NOFLSH);
        rl_termio.c_lflag |=  (ISIG);
        rl_termio.c_cc[VMIN] = 0; /* man -s7I termio for an explanation */
        rl_termio.c_cc[VTIME] = 0; /* on VMIN and VTIME */
        /* disable suspending process on ^Z */
        rl_termio.c_cc[VSUSP] = 0;
        tcsetattr(0, TCSADRAIN, &rl_termio);
        term_set = 1;
    }
}

int main ()
{
	char c;
	int n;
	set_termio();
	while (1)
	{	
		n = read (STDIN_FILENO, &c, 1);
		if (n == -1) {
			fprintf (stderr, "(%d) %s\n", errno, strerror (errno));
		} else if (n == 0)
		{
		} else printf ("%c", c);

		sleep (1);
		fflush (stdout);
	}
}
