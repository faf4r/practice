#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "095-random_io.bin"

typedef struct {
    char name[10];
    int num;
    int age;
} student;

void save(char *filename, student *ar, int n)
{
    FILE *fp;
    if ((fp = fopen(filename, "wb")) == NULL) {
        fprintf(stderr, "Can not open file \"%s\"", filename);
        exit(1);
    }
    for (int i = 0; i < n; i++) {
        if ((fwrite(&ar[i], sizeof(student), 1, fp)) != 1) {
            fprintf(stderr, "Error when writing.\n", filename);
            fclose(fp);
            exit(2);
        }
    }
    // int ret = fwrite(ar, sizeof(student), n, fp);
    // if (ret != n)
    //     printf("Error when writing.\n");
    fclose(fp);
}

/*使用fseek移动文件内位置指针进行读取*/
void load(char *filename, student *ar, int n)
{
    FILE *fp;
    if ((fp = fopen(filename, "rb")) == NULL) {
        fprintf(stderr, "Can not open file \"%s\"", filename);
        exit(1);
    }
    for (int i = 0; i < n; i++) {
        fseek(fp, i * sizeof(student), SEEK_SET); //SEEK_SET是文件首，cur是当前，end是末尾
        fread(ar+i, sizeof(student), 1, fp);
    }
    fclose(fp);
}

void show(student *ar, int n)
{
    printf("id\tname\tage\n");
    for (int i = 0; i < n; i++) {
        printf("%2d\t%s\t%2d\n", ar[i].num, ar[i].name, ar[i].age);
    }
}

int main(void)
{
    student score[5];
    // init
    strcpy(score[0].name, "Amy"), score[0].num = 1, score[0].age = 16;
    strcpy(score[1].name, "Jack"), score[1].num = 2, score[1].age = 19;
    strcpy(score[2].name, "Mike"), score[2].num = 3, score[2].age = 17;
    strcpy(score[3].name, "John"), score[3].num = 4, score[3].age = 14;
    // show & save
    show(score, 4);
    save(FILENAME, score, 4);
    // load & save
    student score_copy[5];
    load(FILENAME, score_copy, 4);
    show(score_copy, 4);
}