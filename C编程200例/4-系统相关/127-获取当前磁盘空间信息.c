// #include <stdio.h>
// #include <dos.h> //这是以前给dos系统用的，现在只剩一个_getdiskfree函数了

// int main(void) {
//     struct _diskfree_t df;
//     int state = _getdiskfree(0, &df);  //_Drive参数：0为当前，1为A，2为B...
//     if (state != 0) {
//         printf("Error getting disk free space: %d\n", state);
//         return 1;
//     }
//     printf("Total clusters: %ld\n", df.total_clusters);
//     printf("Sectors per cluster: %ld\n", df.sectors_per_cluster);
//     printf("Bytes per sector: %ld\n", df.bytes_per_sector);
//     printf("Available clusters: %ld\n", df.avail_clusters);
// }

#include <stdio.h>
#include <Windows.h>

int main(void) {
    DWORD dw = GetLogicalDrives(); // 获取逻辑驱动器
    if (dw == 0) {
        printf("Error getting logical drives: %lu\n", GetLastError());
        return 1;
    }
    printf("Logical drives bitmask: %lu\n", dw);
    for (char drive = 'A'; drive <= 'Z'; drive++) {
        if (dw & 1) { // 检查当前驱动器是否存在
            char rootPath[4] = {drive, ':', '\\', '\0'};
            ULARGE_INTEGER freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
            if (GetDiskFreeSpaceEx(rootPath, &freeBytesAvailable, &totalNumberOfBytes, &totalNumberOfFreeBytes)) {
                printf("Drive %c: Total space: %llu GB, Available space: %llu GB\n", drive, totalNumberOfBytes.QuadPart>>30, freeBytesAvailable.QuadPart>>30);
            } else {
                printf("Error getting disk space for drive %c: %lu\n", drive, GetLastError());
            }
        }
        dw >>= 1; // 移动到下一个驱动器
    }
}