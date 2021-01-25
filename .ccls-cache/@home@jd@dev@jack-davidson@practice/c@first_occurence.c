#include <stdio.h>

char first_occurence(char *letters)
{
	int occurence_table[256];
	int i = 0;
	while(letters[i] != '\0') {
		occurence_table[(int)letters[i]]++;
		printf("%i", occurence_table[i]);
		if (occurence_table[(int)letters[i]] > 1) {
			return letters[i];
		}
		i++;
	}
	return 0;
}

int main()
{
	printf("%c", first_occurence("hello"));
}
