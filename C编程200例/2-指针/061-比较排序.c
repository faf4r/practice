#include <stdio.h>

#define N 5

struct order {
    int num;
    int con;
} a[N];

int main(void) {
    int ar[5] = {24, 52, 78, 31, 21};
    for (int i = 0; i < N; i++){
        a[i].num = ar[i];
        a[i].con = 0;
    }
    for (int i = 0; i < N; i++)
        for (int j = i + 1; j < N; j++) {
            if (a[i].num >= a[j].num)
                a[i].con++;
            else
                a[j].con++;
        }
    for (int i = 0; i < N; i++) {
        printf("%d %d\n", a[i].num, a[i].con);
    }
}