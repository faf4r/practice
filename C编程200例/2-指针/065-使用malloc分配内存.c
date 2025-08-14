#include <stdio.h>
#include <malloc.h>

typedef struct node {
    int n;
    struct node *next;
} node;

int main(void) {
    node *p = (node *)malloc(sizeof(node));
    p->n = 5;
    p->next = NULL;
    printf("p->n=%d\tp->next=%x\n", p->n, p->next);
}