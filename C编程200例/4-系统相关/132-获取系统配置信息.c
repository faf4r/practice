#include <stdio.h>
#include <Windows.h>

int main(void) {
    SYSTEM_INFO sysInfo;
    GetSystemInfo(&sysInfo);
    printf("Processor Architecture: %u\n", sysInfo.wProcessorArchitecture);
    printf("Number of Processors: %u\n", sysInfo.dwNumberOfProcessors);
    printf("Page size: %u\n", sysInfo.dwPageSize);
    printf("Processor type: %u\n", sysInfo.dwProcessorType);

    MEMORYSTATUSEX memInfo;
    memInfo.dwLength = sizeof(memInfo);
    GlobalMemoryStatusEx(&memInfo);
    printf("Total Physical Memory: %llu MB\n", memInfo.ullTotalPhys >> 20);
    printf("Available Physical Memory: %llu MB\n", memInfo.ullAvailPhys >> 20);
    printf("Total Virtual Memory: %llu MB\n", memInfo.ullTotalVirtual >> 20);
    printf("Available Virtual Memory: %llu MB\n", memInfo.ullAvailVirtual >> 20);
}