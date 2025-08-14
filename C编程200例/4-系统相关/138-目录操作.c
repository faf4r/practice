#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>  //目录操作

int main(void) {
    //输出current working directory
    char dir[256];
    getcwd(dir, sizeof(dir));
    if (dir == NULL) {
        perror("getcwd failed");
        return EXIT_FAILURE;
    }
    puts(dir);

    char *s = getcwd(NULL, 0);
    puts(s);

    //新建和删除目录
    if (mkdir("138-directory") == -1) {
        perror("mkdir failed");
        return EXIT_FAILURE;
    }
    if (rmdir("138-directory") == -1) {  //只能删除空目录
        perror("rmdir failed");
        return EXIT_FAILURE;
    }

    //获取目录信息
    if (mkdir("138-directory") == -1) {
        perror("mkdir failed");
        return EXIT_FAILURE;
    }
    struct stat st;
    if (stat("138-directory", &st) == -1) {
        perror("stat failed");
        return EXIT_FAILURE;
    }
    printf("Directory size: %lld bytesn", (long long)st.st_size);

    //更改当前工作目录
    if (chdir("138-directory") == -1) {
        perror("chdir failed");
        return EXIT_FAILURE;
    }
    puts(getcwd(NULL, 0));
    chdir("..");  //返回上一级目录
    puts(getcwd(NULL, 0));

    rmdir("138-directory");  //清理创建的目录
}