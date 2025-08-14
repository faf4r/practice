#include <stdio.h>
#include <string.h>

void sort(char *strings[], int n) {
    char *temp;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (strcmp(strings[i], strings[j]) > 0) {
                temp = strings[i];
                strings[i] = strings[j];
                strings[j] = temp;
            }
        }
    }
}


int main(void) {
    char *strings[5] = {
        "abcd",
        "abc",
        "bcd",
        "kjfodjs",
        "adfdfcv"
    };
    sort(strings, 5);
    for (int i = 0; i < 5; i++) {
        puts(strings[i]);
    }
}