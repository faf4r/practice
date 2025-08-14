#include <stdlib.h>
#include <stdio.h>
#include <Windows.h>

void gotoxy(int x, int y) {
    COORD pos;
    pos.X = x;
    pos.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

int main(void) {
    FILE *fp1 = fopen("107-both_show_1.txt", "r");
    FILE *fp2 = fopen("107-both_show_2.txt", "r");
    char ch;

    gotoxy(3, 8);
    puts("File 1:");
    ch = fgetc(fp1);
    while (!feof(fp1)) {    //注意feof是判断文件指针后是否还有内容，所以最后ch一定会读取到EOF，这个要剔除
        putchar(ch);
        ch = fgetc(fp1);
    }

    gotoxy(3, 13);
    puts("File 2:");
    ch = fgetc(fp2);
    while (!feof(fp2)) {
        putchar(ch);
        ch = fgetc(fp2);
    }

    _fcloseall();
}