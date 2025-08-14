#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *fp = fopen("092-write.txt", "w");
    if (fp == NULL) {
        fprintf(stderr, "Can not open file `92-write.txt`");
        exit(1);
    }

    puts("Please input file content. (end with #)");
    char ch;
    while ((ch = getchar()) != '#')
        fputc(ch, fp);
    // fprintf(fp, "%c", ch);
    fclose(fp);
}