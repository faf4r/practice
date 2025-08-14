#include <stdio.h>
#include <ctype.h>  //tolower, toupper
#include <string.h> //strlwr, strupr

int main() {
    // 字符大小写转换
    char ch = 'a';
    putchar(ch);
    ch = toupper(ch);
    putchar(ch);
    ch = tolower(ch);
    putchar(ch);

    // 字符串大小写转换
    char str[] = "Hello World!";
    puts(str);
    strlwr(str); // 转换为小写
    puts(str);
    strupr(str); // 转换为大写
    puts(str);
}