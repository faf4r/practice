#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}


int main(void) {
    int arr[] = {5, 2, 9, 1, 5, 6};
    size_t n = sizeof(arr) / sizeof(arr[0]);

    // 使用qsort进行快速排序
    qsort(arr, n, sizeof(int), compare); //a-b，小的在前，升序排序

    // 输出排序后的数组
    printf("Sorted array: ");
    for (size_t i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}