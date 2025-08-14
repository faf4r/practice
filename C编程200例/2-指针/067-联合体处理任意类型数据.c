#include <stdio.h>

typedef union {
    int i;
    char c;
    float f;
    double d;
} _item;

typedef struct {
    char type;
    _item item;
} List;

int main(void){
    List ar[5];
    ar[0].type = 'i', ar[0].item.i = 5;
    ar[1].type = 'c', ar[1].item.c = 'm';
    ar[2].type = 'f', ar[2].item.f = 22.33;
    ar[3].type = 'd', ar[3].item.d = 9e5;
    ar[4].type = 'i', ar[4].item.i = -16;

    for (int i = 0; i < 5; i++) {
        switch (ar[i].type) {
            case 'i':
                printf("%c:%d\n", ar[i].type, ar[i].item.i);
                break;
            case 'c':
                printf("%c:%c\n", ar[i].type, ar[i].item.c);
                break;
            case 'f':
                printf("%c:%f\n", ar[i].type, ar[i].item.f);
                break;
            case 'd':
                printf("%c:%lf\n", ar[i].type, ar[i].item.d);
                break;
            default:
                printf("Unkown type %c\n", ar[i].type);
                break;
            }
    }
}