#include <stdio.h>

void invert(int *ar, int n) {
    int *p = ar + n - 1;
    int t;
    while (ar < p) {
        t = *ar;
        *ar++ = *p;
        *p-- = t;
    }
}

int main(void) {
    int ar[5] = {0, 1, 2, 3, 4};
    for (int i = 0; i < 5; i++)
        printf("%d ", ar[i]);
    putchar('\n');
    invert(ar, 5);
    for (int i = 0; i < 5; i++)
        printf("%d ", ar[i]);
    putchar('\n');
}