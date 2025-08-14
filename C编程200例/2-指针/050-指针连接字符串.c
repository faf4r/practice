#include <stdio.h>

char *concatenate(char *str1, char *str2) {
    char *str = str1;
    while (*str1) str1++;
    while (*str2) *str1++ = *str2++;
    *str1 = '\0';
    return str;
}

int main(void) {
    char str1[10]="123", str2[5]="abc";
    char *str = concatenate(str1, str2);
    puts(str);
    puts(str1);
    puts(str2);
}