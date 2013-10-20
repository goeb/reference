#include <stdio.h>
/* MAXLEN is 5 because we use int (256^4 possibilities)
 * and we use 64^5 possibilities
 */
#define MAXLEN 5

int convert2num(char *s) {
	int num=0;
	int i, val;
	for (i=0; i<strlen(s); i++) {
		if (s[i]>='a' && s[i] <= 'z') {
			val=s[i]-'a';
		} else if (s[i]>='A' && s[i] <= 'Z') {
			val=s[i]-'A'+26;
		} else if (s[i]>='0' && s[i] <= '9') {
			val=s[i]-'0'+52;
		} else {
			fprintf(stderr, "ERROR: forbidden character (%c)\n", s[i]);
			exit(1);
		}
		num = num*62+val;
	}
	return num;
}
void convert2char(char *s, int num) {
	int r, d, i;
	int wnum, val;
	wnum = num;
	for (i=4; i>=0; i--) {
		d = wnum/62;
		r = wnum-d*62;
		if (r<26) val = 'a'+r;
		else if (r<52) val = 'A'+r-26;
		else if (r<62) val = '0'+r-52;
		else {
			fprintf(stderr, "ERROR: invalid value (%d)\n", num);
			exit(1);
		}
		s[i] = val;
		wnum = d;
	}
	s[5] = 0;
}
int main(int argc, char **argv) {
	int len;
	int num;
	char s[MAXLEN+1];
	if (argc != 2) {
		fprintf(stderr, "Usage:\n\t%s current_sequence\nExample: %s aabd\n", argv[0], argv[0]);
		return 1;
	}
	len=strlen(argv[1]);
	if (len>MAXLEN) {
		fprintf(stderr, "argument is too long (max is %d)\n", MAXLEN);
		return 1;
	}
	/* characters are a-z, 0-9, A-Z */
	num=convert2num(argv[1]);
	num++;
	convert2char(s, num);
	printf("%s\n", s);
	return 0;
}
