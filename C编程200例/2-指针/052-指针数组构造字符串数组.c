#include <stdio.h>

char *Week[7] = {
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
};

int main(void) {
    int n;
    printf("Please input the day of this week:");
    scanf("%d", &n);
    printf("%s\n", Week[n%7]);
}