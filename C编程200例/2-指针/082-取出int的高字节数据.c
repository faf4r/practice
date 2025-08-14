#include <stdio.h>

int main(void) {
    int a = 0x1234; //34 12 00 00 大端序，高字节存储在低地址
    int copy = a;
    printf("a=0x%x, high bytes is 0x%x\n", a, copy >> 8);
    union {
        char ch[4];
        int num;    //real int
    } number;
    number.num = 0x1234;
    printf("a=0x%x, high bytes is 0x%x\n", number.num, number.ch[1]);
    number.ch[1] = 0x56; //修改高字节
    printf("a=0x%x, high bytes is 0x%x\n", number.num, number.ch[1]);
}