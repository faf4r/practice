#include <stdio.h>
#include <stdlib.h>

#define fn1 "103-old_name.txt"
#define fn2 "103-new_name.txt"

int main(void) {
    FILE *fp = fopen(fn1, "w");
    fclose(fp);
    if (rename(fn1, fn2) != 0) {
        perror("Rename Error");
        exit(-1);
    }
}