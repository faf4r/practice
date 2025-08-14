#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    const char str[5] = "ab";
    char *s = strdup(str);  //在heap根据字符串长度分配内存并复制str内容，返回指向该内存的指针
    printf("str%ss, str=%X, s=%X\n", s==str ? "==" : "!=", str, s);
    char *pstr = str;
    pstr[1] = 'c';
    s[1] = 'd';
    puts(str);
    puts(s);
    free(s);    //注意用后释放，小心内存溢出
    puts(s);    //!悬空指针
    printf("s[0]=%d\n", *s);
    s = NULL;  //将悬空指针置为NULL，避免后续误用

    //查询子字符串
    const char *str1 = "hello world with tail";
    const char *str2 = "world";
    const char *str3 = "he";
    char *p = strstr(str1, str2); //返回指向str1中第一次出现str2的指针，没有返回NULL
    if (p) {
        printf("Found substring: %s\n", p);
    } else {
        printf("Substring not found.\n");
    }

    //strspn寻找第一个不匹配位置的索引
    int i = strspn(str1, str2);
    int j = strspn(str1, str3);
    printf("str12: %d, str13: %d\n", i, j);

    //查询子串并获取长度长度
    p = strstr(str1, str2);
    int length = strspn(p, str2);
    printf("Length of substring '%s' in '%s': %d\n", str2, str1, length);

    //查询第一个出现的字符位置指针
    const char *str4 = "hello world";
    char *ps = strchr(str4, 'o');
    printf("First occurrence of 'o' in '%s': %s\n", str3, ps ? ps : "not found");
}