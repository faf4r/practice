#include <stdio.h>

#define N 3

int main(void) {
    int ar[N][N] = {{0, 1, 2}, {3, 4, 5}, {6, 7 ,8}};
    int *p, (*pt)[N] = ar;
    for (p = *ar; p < *ar+N*N; p++) {
        if ((p-*ar)%N == 0) putchar('\n');
        printf("%d ", *p);
    }
    int i, j;
    printf("please input i and j:");;
    scanf("%d%d", &i, &j);
    printf("ar[%d][%d] is %d", i, j, *(*(pt+i)+j));
}