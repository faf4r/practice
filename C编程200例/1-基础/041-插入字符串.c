#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void insert(char *str1, char *str2, int pos) {
    if (pos < 0 || pos > strlen(str1)) {
        printf("Error: pos bigger than length of str1.");
        exit(1);
    }
    char t[100] = {0};
    strcpy(t, str1+pos);
    strcpy(str1+pos, str2);
    strcat(str1, t);
}


int main(void) {
    char s1[100] = "abcdefg", s2[100] = "123456";
    insert(s1, s2, 2);
    puts(s1);
}