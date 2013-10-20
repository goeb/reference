#include <unistd.h>

#include <SDL/SDL_mixer.h>


main(int argc, char **argv)
{
        char * filename;
        if (argc >= 2) filename = argv[1];
        else filename = "ding.wav";

        if (Mix_OpenAudio(16000, AUDIO_S16SYS, 2, 2048) < 0)
        {
            printf("Error: Couldn't set 44100 Hz 16-bit audio\n"
                   "Reason: %s\n", SDL_GetError());
        }

        Mix_Chunk *sound = 0;
        printf("Loading %s...\n", filename);
        sound = Mix_LoadWAV(filename);

        if (!sound)
        {
            printf("Error: could not load %s! (%s)\n", filename, SDL_GetError());
            exit(1);
        }

        printf("Playing %s...\n", filename);
        Mix_PlayChannel(-1, sound, 0); // -1 for any channel

        //usleep(50000);
        sleep(1);
        Mix_PlayChannel(-1, sound, 0); // -1 for any channel

        sleep(2);
        Mix_CloseAudio();
}
