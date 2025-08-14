#include <stdio.h>
#include <math.h>
#include <conio.h>


int main(void) {
    for (int n = 100; n < 1000; n++) {
        int i = n % 10;
        int j = n / 10 % 10;
        int k = n / 100;
        if (pow(i, 3) + pow(j, 3) + pow(k, 3) == n)
            printf("%d\n", n);
    }
}