extern char ** environ;

int main(int argc, char ** argv, char **envp)
{
    int i;
    for (i = 0; i < argc; i++)
    {
        printf("argv[%d]=%s\n", i, argv[i]);
    }

    i = 0;
    while (envp && envp[i])
    {
        printf("envp[%d]=%s\n", i, envp[i]);
        i++;
    }

    i = 0;
    while (environ && environ[i])
    {
        printf("environ[%d]=%s\n", i, environ[i]);
        i++;
    }
    return 0;
}
