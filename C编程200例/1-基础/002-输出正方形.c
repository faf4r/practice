#include <stdio.h>

#define a 5  //边长

int main(void) {
    char space[a-2], star[a];
    for (int i = 0; i < a; i++) {
        star[i] = '*';
        if (i < a-2) space[i] = ' ';
    }
    printf("%s\n", star);
    for (int i = 0; i < a-2; i++)
        printf("*%s*\n", space);
    printf("%s\n", star);
}
