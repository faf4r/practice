#include <stdio.h>

int is_leap_year(int year);
int day_of_year(int y, int m, int d);


int main(void) {
    int year, month, day, result=0;
    printf("输入年月日，格式为“年/月/日”：\n");
    scanf("%d/%d/%d", &year, &month, &day);
    printf("%d的第%d天\n", year, day_of_year(year, month, day));
}


int day_of_year(int y, int m, int d) {
    int ar[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int ret = 0;
    if (is_leap_year(y))
        ar[1] = 29; // 闰年处理
    for (int i = 1; i < m; i++) {
        ret += ar[i - 1];
    }
    ret += d;
    return ret;
}

int is_leap_year(int year) {
    if (year % 100 == 0 && year % 400 == 0)
        return 1;
    else if (year % 100 != 0 && year % 4 == 0)
        return 1;
    else
        return 0;
}
