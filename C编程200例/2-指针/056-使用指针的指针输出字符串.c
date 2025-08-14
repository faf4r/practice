#include <stdio.h>

int main(void) {
    char *strings[] = {
        "C language",
        "Basic",
        "World wide",
        "Olympic",
        "Great Wall"
    };
    char **p = strings;
    for (int i = 0; i < 5; i++) {
        puts(*(p+i));
    }
}