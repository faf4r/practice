#include <stdio.h>

int * find(int *a, int an, int *b, int bn) {
    /*有序数组找出第一个相同值*/
    int *pa = a, *pb = b;
    while (pa < a+an && pb < b+bn) {
        if (*pa < *pb)
            pa++;
        else if (*pa > *pb)
            pb++;
        else// if (*pa == *pb)
            return pa;
    }
}

int main(void) {
    int a[5] = {0, 1, 2, 3, 4}, b[4] = {1, 3, 5, 7};
    int *p = find(a, 5, b, 4);
    printf("The first same value of array a and b is %d.\n", *p);
}