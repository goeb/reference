
/* this causes a bus error on sparc processors */

main() {
	char s[] = "1234";
	int *i;
	i = (int*)(s+1);
	printf("%x\n", *i);
}
