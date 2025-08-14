#include <stdio.h>
#include <stdlib.h>

#define filename "104-delete.txt"

int main(void) {
    // FILE *fp = fopen(filename, "w");
    // fclose(fp);

    if (remove(filename) != 0) { //== -1
        perror("Remove Error");
        exit(-1);
    }
}