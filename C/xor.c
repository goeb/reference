main()
{
	char *text="The cat is there.";
	char *key="underground";
	int i, l, KL, r;

	l=strlen(text);
	KL=strlen(key);
	for (i=0; i<l; i++) {
		r=text[i]^key[i%KL];
		printf("%c[%02x] XOR %c[%02x] = %c[%02x]\n", text[i], text[i], key[i%KL], key[i%KL], r, r);
	}
}
