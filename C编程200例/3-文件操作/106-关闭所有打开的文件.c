#include <stdio.h>
#include <stdlib.h>

#define f0 "106-closeall_0.txt"
#define f1 "106-closeall_1.txt"
#define f2 "106-closeall_2.txt"

int main(void) {
    FILE *fp[3];
    fp[0] = fopen(f0, "r");
    fp[1] = fopen(f1, "r");
    fp[2] = fopen(f2, "r");

    int count;
    if ((count = _fcloseall()) != EOF)  //fcloseall会报错
        printf("%d files closed.", count);
    else {
        perror("closeall Error");
        exit(-1);
    }
}