#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    time_t start, end;
    start = time(NULL);
    _sleep(1000);
    end = time(NULL);
    printf("runtime is: %.0lfs\n", difftime(end, start));
}