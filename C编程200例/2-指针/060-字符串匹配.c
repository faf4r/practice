#include <stdio.h>
#include <string.h>

int match(const char *str1, const char *str2) {
    /*返回str2在str1中的起始位置，不存在则返回-1*/
    const char * p = str1, *p1, *p2;
    int i = 0;
    while (*p) {
        p1 = p;
        p2 = str2;
        while (*p1 && *p2 && *p1==*p2)
            p1++, p2++;
        if (*p2 == '\0')
            return p - str1;
        else
            p++;
    }
    return -1;
}

int match2(const char *str1, const char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    for (int start = 0; start < len1-len2; start++) {
        int i = start, j = 0;
        for (; j < len2 && str1[i] == str2[j]; i++, j++);
        if (j == len2) return start;
    }
    return -1;
}

int main(void) {
    char s1[] = "One world, one dream", s2[] = "world";
    int p1 = match(s1, s2);
    int p2 = match2(s1, s2);
    printf("match1 is %d\nmatch2 is %d", p1, p2);
}