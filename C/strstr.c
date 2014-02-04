
#include <stdio.h>
#include <string.h>

int main()
{
	const char* text = "toto\na\nla\npiscine\n";
	const char *startOfLine = text;
	const char *endOfLine = 0;
	while (startOfLine) {
		endOfLine = strstr(startOfLine, "\n");
		int length;
		if (endOfLine) length = endOfLine - startOfLine;
		else length = strlen(startOfLine);

		char line[1000];
		memset(line, 0, 1000);
		memcpy(line, startOfLine, length);
		printf("line: %s\n", line);

		if (!endOfLine) break;
		if (endOfLine == startOfLine + strlen(startOfLine) - 1) break;
		startOfLine = endOfLine + 1;
	}
}
