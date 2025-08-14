#include <stdio.h>

float *search(float (*p)[4], int n) {
    float *pt = *(p+n);
    return pt;
}


int main(void) {
    float * (*func)() = search;
    float ar[3][4] = {{0,66,77,88}, {1, 77,88,66}, {2,88,66,77}};
    float *p = func(ar, 1);
    for (int i = 0; i < 4; i++) {
        printf("%.2f ", *(p+i));
    }
    putchar('\n');
}