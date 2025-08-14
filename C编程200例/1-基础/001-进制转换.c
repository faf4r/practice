#include <stdio.h>


int main(void) {
    int num;
    char bin[33] = {0};
    printf("Please input a 10-based number:");
    scanf("%d", &num);
    for (int i = 31; i >= 0; i--) {
        bin[i] = (num & 1) ? '1' : '0';
        num >>= 1;
    }
    for (int i = 0; i < 32; i++) {
        printf("%c", bin[i]);
        if (i>0 && i<31 && (i+1)%4==0)
            printf(" ");
    }
    printf("\n");
    // puts(bin);
}