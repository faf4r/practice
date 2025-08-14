#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(void) {
    time_t now = time(NULL);    //time(&now)也可，直接赋值给now
    puts(ctime(&now));           //ctime

    struct tm *time_pointer = localtime(&now);
    puts(asctime(time_pointer));    //asctime

    //自定义输出
    printf("%d/%d/%d %d:%d:%d\n",
        time_pointer->tm_year+1900, time_pointer->tm_mon+1, time_pointer->tm_mday, 
        time_pointer->tm_hour, time_pointer->tm_min, time_pointer->tm_sec);
}