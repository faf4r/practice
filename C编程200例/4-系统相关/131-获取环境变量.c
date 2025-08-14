#include <stdio.h>
#include <stdlib.h>

int main() {
    char *path = getenv("PATH");
    puts(path ? path : "Environment variable PATH is not set.");
    
    extern char **environ;
    while (*environ) {
        puts(*environ++);
    }
}