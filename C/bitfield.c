
typedef struct Preferences {
	int likesIceCream : 1;
    int playsGolf     : 1;
    int watchesTv     : 1;
    int readsBooks    : 1;
	int xxx;
} Preferences; 
 
main() 
{
	Preferences fred;
	fred.likesIceCream = 1;
	fred.playsGolf     = 0;
	fred.watchesTv     = 2;
	fred.readsBooks    = 3;

}
