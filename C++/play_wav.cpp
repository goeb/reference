#ifdef _WIN32
#include <windows.h>
#endif

#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <iostream>
using namespace std;

extern "C"
{
#include "sox.h"
}

#define BUFSZ 16384

class Sound
{
        string dspPath;
        string file;
        unsigned char sampbuf[BUFSZ];
    public:
        Sound(string filename)
        {
            file = filename;
            dspPath = "/dev/dsp";
        }
        void play()
        {
#ifdef _WIN32
            PlaySound(file.c_str(), NULL, SND_FILENAME | SND_SYNC);
#else

            if (sox_init() != SOX_SUCCESS)
            {
                cerr << "error sox_init()" << endl;
            }

            sox_format_t * in, * out;
            in = sox_open_read(file.c_str(), 0, 0, 0);
            out = sox_open_write(dspPath.c_str(), &in->signal, 0, "oss", 0, 0);

            sox_sample_t ibuf[BUFSZ];
            int n;
            while ( (n = sox_read(in, ibuf, BUFSZ)) )
            {
            cout << "n=" << n << endl;
                size_t len = sox_write(out, ibuf, n);
            }
            cout << "n=" << n << endl;
            sox_close(out);
            sox_close(in);
            sox_quit();
#endif
        }
};

main(int argc, char **argv)
{
    if (argc < 2) exit(1);

    string soundfile = argv[1];

    cout << "playing " << soundfile << endl;

    Sound s(soundfile);
    s.play();


}
