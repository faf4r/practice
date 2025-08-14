#include <stdio.h>

#define Even(x) ((x)%2==0)

int main(void) {
    int sum = 0;
    for (int i = 0; i <=100; i++) {
        if (Even(i))
            sum += i;
    }
    printf("Sum=%d\n", sum);
}