#include <stdio.h>

int *FindMax(int *ar, int n) {
    int *max = ar;
    for (int i = 0; i < n; ++i) {
        max = *max < ar[i] ? max+i : max;
    }
    return max;
}


int main(void) {
    int ar[5] = {0, 9, 7, 5, 8};
    int *max = FindMax(ar, 5);
    printf("max: %d\n", *max);
}