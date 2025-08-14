#include <stdio.h>
#include <stdlib.h>
#include <io.h> //create函数创建文件

#define filename "101-create.txt"

int main(void) {
    int fh;  //create返回文件句柄
    if ((fh = creat(filename, 0)) == -1) {  //_PermissionMode查文档
        perror("Create Error");
        exit(-1);
    }
    else {
        puts("Create successfully.");
        close(fh); //相当于fclose，关闭文件句柄
    }
}