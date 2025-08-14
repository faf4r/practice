#include <stdio.h>

#define swap(a, b) {int _t; _t = a, a = b, b = _t;}


int main(void) {
    int a[5] = {0,1,2,3,4}, b[5] = {5,6,7,8,9};
    for (int i = 0; i < 5; i++)
        swap(a[i], b[i]);
    for (int i = 0; i < 5; i++)
        printf("%d ", a[i]);
        printf("\n");
    for (int i = 0; i < 5; i++)
        printf("%d ", b[i]);
        printf("\n");
}