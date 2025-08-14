#include <stdio.h>
#include <stdlib.h>

#define FILENAME "093-format_read_write.txt"


int main(void) {
    FILE *fp;
    //写
    if ((fp = fopen(FILENAME, "w")) == NULL) {
        fprintf(stderr, "Can not open file `%s`\n", FILENAME);
        exit(1);
    }
    int a = 9, b = 1l;
    fprintf(fp, "%d, %d", a, b);
    fclose(fp);

    //读
    a = 0, b = 1;
    if ((fp = fopen(FILENAME, "r")) == NULL) {
        fprintf(stderr, "Can not open file `%s`\n", FILENAME);
        exit(1);
    }
    fscanf(fp, "%d, %d", &a, &b);
    fclose(fp);
    printf("a=%d, b=%d", a, b);
}