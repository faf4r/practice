#include <stdio.h>

int main() {
    int ar[5] = {0, 1, 2, 3, 4};
    int *p = ar;
    *p = &ar[0];  //二者等效
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(p+i));
    }
    putc('\n', stdout);
    putchar('\n');
}