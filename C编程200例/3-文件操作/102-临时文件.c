/**
 * @file 102-临时文件.c
 * @date 2025-08-07
 * 
 * @brief tmpfile创建临时文件, rewind文件指针重置到开头
 * 
 */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *tmp = tmpfile(); // 以wb+模式创建一个具有唯一自动生成文件名的临时文件，Windows需要系统权限
    if (tmp == NULL) {
        perror("Create temp file Error");
        exit(-1);
    }
    fputs("Hello world!", tmp);
    rewind(tmp);
    char s[50];
    fgets(s, sizeof(s), tmp);
    puts(s);
    fclose(tmp);    //关闭或程序终止(返回)时删除文件
}