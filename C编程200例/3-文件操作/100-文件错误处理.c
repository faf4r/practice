/**
 * @file 100-文件错误处理.c
 * @date 2025-08-06
 * 
 * @brief fopen_s返回0为正常读取，ferror检查错误，perror输出错误
 * 
 */

#include <stdio.h>
#include <stdlib.h>

#define filename "100-file.txt"

int main(void) {
    FILE *fp;
    char str[10] = {0};

    if (fopen_s(&fp, filename, "a") == 0) {
        str[0]= fgetc(fp);  //a模式是读不了的
        perror("Read file");
        if (ferror(fp)) {  //这里实际error了，但是perror会说No error
            perror("File read");
            printf("Actually error occurred.\n");
        }
        fclose(fp);
    } else {
        perror("File open");
        exit(1);
    }

    int count, total = 0;
    if ((fp = fopen(filename, "r")) != NULL) {
        while (!feof(fp)) {
            count = fread(str, sizeof(char), 10, fp);
            //每次读取都检查是否错误
            if (ferror(fp)) {
                perror("Read Error");
                break;
            }
            total += count;
        }
        fclose(fp);
        printf("Number of bytes read = %d\n", total);
    } else {
        perror("File open");
        exit(1);
    }
}