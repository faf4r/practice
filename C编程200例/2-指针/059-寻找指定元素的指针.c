#include <stdio.h>
#include <stdlib.h>


int *search(int ar[], int n, int val) {
    int *p;
    for (p = ar; p < ar+n; p++){
        if (*p == val)
            return p;
    }
    return NULL;
}

int main(void) {
    int ar[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    printf("The address of ar[0] is %u.\n", &ar[0]);
    int val;
    printf("Please enter the number you want to search:");
    scanf("%d", &val);
    int *p = search(ar, sizeof(ar)/sizeof(ar[0]), val);
    if (!p) {
        fprintf(stderr, "Error: the value is not in ar.");
        exit(1);
    }
    printf("ar[%d]=%d, address:%u\n", (p-ar), val, p);
}