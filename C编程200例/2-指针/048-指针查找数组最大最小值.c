#include <stdio.h>


void max_min(int ar[], int n, int *max, int *min) {
    *max = *min = *ar;  // ar[0] === *ar, ar[1] === *(ar+1)
    for (int *p = ar; p < ar+n; p++) {
        if (*p > *max) *max = *p;
        if (*p < *min) *min = *p;
    }
}

int main(void) {
    int ar[5] = {1, 3, 5, 7, 9};
    int max, min;
    max_min(ar, 5, &max, &min);
    printf("size: %d\nmax=%d, min=%d\n", sizeof(ar)/sizeof(*ar), max, min);
}