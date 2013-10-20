
playSound:

playSound.o: playSound.c
	gcc -g -c playSound.c

playSound: playSound.o
	#gcc -g -o playSound playSound.o -lSDL -lSDL_mixer
	#gcc -g -o playSound playSound.o /usr/lib/libSDL_mixer.a /usr/lib/libSDL.a -ldl -lmikmod
#	gcc -g -o playSound playSound.o /home/fred/SDL_mixer-1.2.8-install/lib/libSDL_mixer.a /usr/lib/libSDL.a \
		   	-lasound \
			-lartsc \
			-lesd \
			-lpulse-simple \
			-laudio
	gcc -g -o playSound playSound.o /home/fred/SDL_mixer-1.2.8-install/lib/libSDL_mixer.a /home/fred/SDL-1.2.13-install/lib/libSDL.a -lpthread

clean:
	rm -f core *.o playSound

playSound2.o: playSound2.c
	gcc -g -c playSound2.c -I/home/fred/SDL-1.2.13-install/include/SDL

playSound2 : playSound2.o
	gcc -g -o  playSound2 playSound2.o /home/fred/SDL-1.2.13-install/lib/libSDL.a -lpthread
