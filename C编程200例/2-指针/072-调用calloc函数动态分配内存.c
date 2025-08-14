#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

#define N 15

int main(void) {
    int *ar = (int *)calloc(N, sizeof(int));
    if (!ar) {
        fprintf(stderr, "Error: callloc fault.");
        exit(1);
    }
    for (int i = 0; i < N; i++)
        ar[i] = i;
    for (int i = 0; i < N; i++)
       printf("%d ", ar[i]);
    putchar('\n');
    free(ar);
    ar = NULL;
}