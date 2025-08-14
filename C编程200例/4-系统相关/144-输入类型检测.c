#include <stdio.h>
#include <ctype.h>

int main(void) {
    char ch;
    char s[11] = "As5/*- `!$";
    for (int i = 0; i < 11; i++) {
        ch = s[i];
        putchar(ch);
        if (isalnum(ch))
            if (isalpha(ch))
                puts("alpha");
            else
                puts("digit");
        else if (isdigit(ch))
            puts("digit但不会触发");
        else if (isblank(ch))
            puts("blank");
        else if (iscntrl(ch))
            puts("control");
        else
            puts("other type");
    }
}