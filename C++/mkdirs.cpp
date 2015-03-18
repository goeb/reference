
       #include <sys/stat.h>
       #include <sys/types.h>

#include <stdio.h>
#include <string>

bool isDir(const std::string &path)
{
    struct stat fileStat;

    int r = stat(path.c_str(), &fileStat);
    if (r == 0 && S_ISDIR(fileStat.st_mode) ) return true;
    else return false;
}

/** Create the given directory (create all intermediate directories if needed)
  */
int mkdirs(const std::string &path)
{
    if (path.empty()) return -1;

    int i = 0;
    size_t offset = 0;
    size_t pos = 0;
    while (pos != std::string::npos) {
        pos = path.find_first_of("/", offset);
        std::string subpath;
        if (pos == std::string::npos) {
            subpath = path;

        } else {
            subpath = path.substr(0, pos);
            offset = pos+1;

        }

        if (!isDir(subpath)) {
            int r = mkdir(subpath.c_str(), 0777);
            if (r != 0) return -1;
        }
    }
    return 0;
}

int main(int argc, char **argv)
{
    int r = mkdirs(argv[1]);
    printf("mkdirs(%s) => %d\n", argv[1], r);
}
