#include <stdio.h>

int main(void){
    int day=9, total=1;
    while (day > 0) {
        total = (total+1) * 2;
        day--;
    }
    printf("total: %d\n", total);
}