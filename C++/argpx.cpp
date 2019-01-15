#include <stdlib.h>
#include <argp.h>

const char *argp_program_version = "argpx 1.0";

/* Program documentation. */
static char doc[] = "Argpx -- Supervisor";

/* A description of the arguments we accept. */
static char args_doc[] = "PATH";

/* Keys for options without short-options. */
#define OPT_T1  1
#define OPT_D1  2

#define VAL_DEFAULT_T1 "18"
#define VAL_DEFAULT_D1 "120"

/* The options we understand. */
static struct argp_option options[] = {
  {"verbose",    'v', 0,   0, "Produce verbose output" },
  {"syslog",     's', 0,   0, "Log to syslog instead of stderr" },
  {"threshold1",  0, "T1", 0, "Set threshold1 (default: " VAL_DEFAULT_T1 ")" },
  {"duration1",   0, "D1", 0, "Set duration1 (default: " VAL_DEFAULT_D1 ")" },
  { 0 }
};

/* Used by main to communicate with parse_opt. */
struct arguments
{
	char *args[1];                /* PATH */
	int syslog;
	int verbose;
	int threshold1;
	int duration1;
};

/* Parse a single option. */
static error_t parse_opt(int key, char *arg, struct argp_state *state)
{
	/* Get the input argument from argp_parse, which we
	   know is a pointer to our arguments structure. */
	struct arguments *arguments = (struct arguments *)state->input;

	switch (key) {
		case 's': /* syslog */
			arguments->syslog = 1;
			break;
		case 'v':
			arguments->verbose = 1;
			break;
		case OPT_T1:
			arguments->threshold1 = atoi(arg);
			break;
		case OPT_D1:
			arguments->duration1 = atoi(arg);
			break;

		case ARGP_KEY_ARG:
			if (state->arg_num >= 1) {
				/* Too many arguments. */
				argp_usage (state);
			}

			arguments->args[state->arg_num] = arg;

			break;

		case ARGP_KEY_END:
			if (state->arg_num < 1) {
				/* Not enough arguments. */
				argp_usage(state);
			}
			break;

		default:
			return ARGP_ERR_UNKNOWN;
	}
	return 0;
}

/* Our argp parser. */
static struct argp argp = { options, parse_opt, args_doc, doc };

int main (int argc, char **argv)
{
	struct arguments arguments;

	/* Default values. */
	arguments.syslog = 0;
	arguments.verbose = 0;
	arguments.threshold1 = atoi(VAL_DEFAULT_T1);
	arguments.duration1 = atoi(VAL_DEFAULT_D1);

	/* Parse our arguments; every option seen by parse_opt will
	   be reflected in arguments. */
	argp_parse (&argp, argc, argv, 0, 0, &arguments);

	printf("PATH=%s\n", arguments.args[0]);
	printf("--syslog=%d\n", arguments.syslog);
	printf("--verbose=%d\n", arguments.verbose);
	printf("--threshold1=%d\n", arguments.threshold1);
	printf("--duration1=%d\n", arguments.duration1);
	exit (0);
}
