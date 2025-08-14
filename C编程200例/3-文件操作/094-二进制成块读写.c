#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "094-binary_block.bin"

typedef struct {
    char name[10];
    int num;
    float Chinese;
    float Math;
    float English;
} score_t;

void save(char *filename, score_t *ar, int n) {
    FILE *fp;
    if ((fp = fopen(filename, "wb")) == NULL) {
        fprintf(stderr, "Can not open file \"%s\"", filename);
        exit(1);
    }
    // for (int i = 0; i < n; i++) {
    //     if ((fwrite(&ar[i], sizeof(score_t), 1, fp)) != 1)
    //     printf("Error when writing.\n");
    // }
    int ret = fwrite(ar, sizeof(score_t), n, fp);
    if (ret != n) {
        fprintf(stderr, "Error when writing.\n", filename);
        fclose(fp);
        exit(2);
    }
    fclose(fp);
}

void load(char *filename, score_t *ar, int n) {
    FILE *fp;
    if ((fp = fopen(filename, "rb")) == NULL) {
        fprintf(stderr, "Can not open file \"%s\"", filename);
        exit(1);
    }
    fread(ar, sizeof(score_t), n, fp);
    fclose(fp);
}

void show(score_t *ar, int n) {
    printf("id\tname\tChinese\tMath\tEnglish\n");
    for (int i = 0; i < n; i++) {
        printf("%2d\t%s\t%.2f\t%.2f\t%.2f\n", ar[i].num, ar[i].name, ar[i].Chinese, ar[i].Math, ar[i].English);
    }
}


int main(void) {
    score_t score[5];
    //init
    strcpy(score[0].name, "Amy"), score[0].num = 1, score[0].Chinese = 89, score[0].Math = 97, score[0].English = 92.5;
    strcpy(score[1].name, "Jack"), score[1].num = 2, score[1].Chinese = 97, score[1].Math = 79, score[1].English = 89;
    strcpy(score[2].name, "Mike"), score[2].num = 3, score[2].Chinese = 88.5, score[2].Math = 93, score[2].English = 90.5;
    strcpy(score[3].name, "John"), score[3].num = 4, score[3].Chinese = 77, score[3].Math = 78, score[3].English = 66;
    //show & save
    show(score, 4);
    save(FILENAME, score, 4);
    //load & save
    score_t score_copy[5];
    load(FILENAME, score_copy, 4);
    show(score_copy, 4);
}