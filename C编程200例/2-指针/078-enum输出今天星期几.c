#include <stdio.h>

enum Week{Sun, Mon, Tue, Wed, Thu, Fri, Sat};

int main(void) {
    int i;
    scanf("%d", &i);
    switch (i)
    {
    case Sun:
        printf("Sunday\n");
        break;
    case Mon:
        printf("Monday\n");
        break;
    case Tue:
        printf("Tuesday\n");
        break;
    case Wed:
        printf("Wednesday\n");
        break;
    case Thu:
        printf("Thursday\n");
        break;
    case Fri:
        printf("Friday\n");
        break;
    case Sat:
        printf("Saturday\n");
        break;
    default:
        break;
    }
}