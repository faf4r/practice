#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int a = 1, b = 5;
    swap(&a, &b); //注意传地址
    printf("Now a=%d, b=%d\n", a, b);
}