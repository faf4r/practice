#include <stdlib.h>
#include <stdio.h>

#define FILENAME "096-row.bin"

int main(void) {
    FILE *fp;
    char str[100], s[50];
    printf("Please input content, enter to submit:");
    gets(str);  //会自动丢弃'\n'不存入字符串，不需要手动清空缓冲区(不安全，可能溢出，用fgets或gets_s)
    if ((fp = fopen(FILENAME, "wb")) != NULL) {
        fputs(str, fp);
        fputs("...", fp);  //不会输出换行符
        fclose(fp);
    } else {
        fprintf(stderr, "File open error.");
        exit(1);
    }

    if ((fp = fopen(FILENAME, "rb")) != NULL) {
        fgets(s, sizeof(s), fp);  //参数_MaxCount为字符串数组的长度，计数包括了'\0'，所以实际最多能读n-1个字符(包括'\n')，因为最后一个字符必须是'\0'
        fclose(fp);
    } else {
        fprintf(stderr, "File open error.");
        exit(1);
    }
    puts(s);
}