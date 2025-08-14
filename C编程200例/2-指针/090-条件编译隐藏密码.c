#include <stdio.h>

#define PWD 1 //为1则隐藏密码，0不隐藏

int main(void) {
    char pwd[10] = "abcdefg";
    #if PWD
        printf("******\n");
    #else
        printf("%s\n", pwd);
    #endif
}