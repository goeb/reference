#include <iostream>
using namespace std;
#include <unistd.h>

main(int argc, char ** argv)
{
    cout << "main starting..." << endl;

	string ssh_path = argv[1];
	string ssh_version_cmd = ssh_path + " -v";
	system(ssh_version_cmd.c_str());

    int fdCOut[2];
    int fdCErr[2];

    pipe(fdCOut);
    pipe(fdCErr);


    pid_t pid = fork();
    if ( 0 == pid )
    {
        // in child
        // close read-pipes
        close(fdCOut[0]);
        close(fdCErr[0]);

        // redirect stdout and stderr to write-pipes
        // so that the parent can read them
        dup2(fdCOut[1], STDOUT_FILENO);
        dup2(fdCErr[1], STDERR_FILENO);

        execl(ssh_path.c_str(), "ssh", "-T", "-x", "-n", "localhost", "/home/fred/reference/C++/ssh_block_problem/t.sh", argv[2], (char *)0);
        cout << "never here" << endl;
    }
    else
    {
        // in parent
        // close write-pipes
        close(fdCOut[1]);
        close(fdCErr[1]);

        char tmp1[1024];
        int nb;
        memset(tmp1, 0, 1024);
        // the parent reads what is coming from the child
        while ((nb = read(fdCOut[0], tmp1, 1024)) > 0)
        {
            cout << "parent received " << nb << " bytes: " << tmp1 << endl;
            memset(tmp1, 0, 1024);
        }
        while ((nb = read(fdCErr[0], tmp1, 1024)) > 0)
        {
            cout << "ERROR received: " << nb << " bytes: " << tmp1 << endl;
            memset(tmp1, 0, 1024);
        }
        cout << "parent completed." << endl;
    }
}
