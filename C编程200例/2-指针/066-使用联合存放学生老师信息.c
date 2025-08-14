#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char name[10];
    char type;
    union class_position
    {
        int class;
        char position[10];
    }job;
} person;

int main(void) {
    person teacher = {25, "王薇", 't'}, stu = {3, "张明", 's'};
    strcpy(teacher.job.position, "teacher"); //不能直接赋值
    stu.job.class = 3;
    printf("%d\n", stu.job.class);
    printf("%s\n", teacher.job.position);
}