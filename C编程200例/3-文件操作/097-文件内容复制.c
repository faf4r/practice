#include <stdio.h>
#include <stdlib.h>

#define f_src "097-copy_src.txt"
#define f_dst "097-copy_dst.txt"

void copy(FILE *src, FILE *dst) {
    //重置文件指针位置
    fseek(src, 0, SEEK_SET);
    fseek(dst, 0, SEEK_SET);
    char ch;
    while ((ch = fgetc(src)) != EOF) {
        fputc(ch, dst);
    }
}

int main(void) {
    FILE *src = fopen(f_src, "r");
    FILE *dst = fopen(f_dst, "w");
    copy(src, dst);
    fclose(src);
    fclose(dst);
}