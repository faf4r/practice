#include <stdio.h>
#include <windows.h>

int main()
{
    SYSTEMTIME st;
    GetLocalTime(&st);
    printf("current time is: %d-%d-%d %02d:%02d:%02d\n", st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond);

    // 修改本地时间（管理员权限）
    st.wYear = 2026;
    // st.wHour = 8;
    if (SetLocalTime(&st)) {
        puts("Successfully.");
    } else {
        puts("Failed.");
    }
    // 系统时间是GetSystemTime和SetSystemTime，这个是UTC时间，LocalTime=UTC+时区偏移
}