#include <stdio.h>
#include <stdlib.h>


int main(void) {
    FILE *fp = fopen("091-read.txt", "r");
    char ch;
    while ((ch = fgetc(fp)) != EOF)
        putchar(ch);
    fclose(fp);
}