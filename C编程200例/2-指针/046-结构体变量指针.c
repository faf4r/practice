#include <stdio.h>


typedef struct {
    int num;
    char name[20];
    char sex;
    int age;
    float score;
} student;

int main(void) {
    student stu = {1, "tmf", 'M', 22, 88.5};
    student *p;
    p = &stu;
    printf("name: %s\nsex: %c\nage: %d\nscore: %.2f\n", p->name, p->sex, p->age, p->score); //使用->取指针指向结构体的成员变量
}