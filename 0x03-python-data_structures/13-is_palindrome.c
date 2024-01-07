#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int dec = 65489, i = 0;
	char *bin_str = malloc(sizeof(char) * 50);

	if (bin_str == NULL)
		return 1;
	while (dec > 0)
	{
		bin_str[i++] = dec % 2 + '0';
		dec /= 2;
	}
	bin_str[i] = '\0';
	for (i = i - 1; i >= 0; i--)
		printf("%c", bin_str[i]);

	printf("\n");
	free(bin_str);
	return 0;
}
/*
	10 / 2 = 5 __ 0
	5 / 2 = 2__ 1
*/