#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define f1 "098-src1.txt"
#define f2 "098-src2.txt"
#define fm "098-merge.txt"

/*将fp2的内容合并到fp1(追加写入)*/
void merge(FILE *fp1, FILE *fp2, char *s) {
    fseek(fp1, 0, SEEK_SET);
    fgets(s, 50, fp1);  //读取fp1的内容到s

    fseek(fp1, 0, SEEK_SET); //即使是SEEK_SET也是追加，不会覆写
    fseek(fp2, 0, SEEK_SET);
    char ch;
    while ((ch = fgetc(fp2)) != EOF)
        // fputc(ch, fp1);
        fprintf(fp1, "%c", ch);  //将fp2的内容输出到标准输出
}

/*将一个文件指针数组合并到一个文件中*/
void merge2(FILE *dst, FILE *fp[], int n) {
    fseek(dst, 0, SEEK_SET);
    char ch;
    for (int i = 0; i < n; i++) {
        fseek(fp[i], 0, SEEK_SET);
        // rewind(fp[i]);  回到文件开头
        while ((ch = fgetc(fp[i])) != EOF)
            fputc(ch, dst);
    }
}

int  main(void) {
    FILE *fp1 = fopen(f1, "a+");  //a无论怎么写fseek(fp,0,SEEK_SET)都不会清空文件内容，只能在末尾追加，不过+可以从头读
    FILE *fp2 = fopen(f2, "r");
    // FILE *dst = fopen(fm, "w");
    // FILE *ar[2] = {fp1, fp2};
    // merge2(dst, ar, 2);

    char s[100] = {0};
    merge(fp1, fp2, s);
    puts(s);  //输出合并后的内容

    fclose(fp1);
    fclose(fp2);
    // fclose(dst);
}