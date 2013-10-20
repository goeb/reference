
main(){

	char s[50];
	const char * pointeur;
	char * ptr;
	strcpy(s, "toto et titi");
	pointeur = s;
	ptr = pointeur;
	ptr[2] = 'R';
	printf("%s\n", pointeur);

}
