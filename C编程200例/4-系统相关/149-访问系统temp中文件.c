#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *tempDir = getenv("TEMP");
    puts(tempDir);
    char tempFile[256];
    strcpy(tempFile, tempDir);
    strcat(tempFile, "\\tempfile.txt");

    FILE *fp = fopen(tempFile, "w");
    if (fp == NULL) {
        perror("Failed to open file");
        return EXIT_FAILURE;
    }
    fprintf(fp, "This is a temporary file.\n");
    fclose(fp);
    if (remove(tempFile) != 0) {
        perror("Failed to delete file");
        return EXIT_FAILURE;
    }
}