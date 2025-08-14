/**
 * 文件加密就是读取每个字节(char)内容与密钥key进行异或
 * src ^ key得到密文
 * src ^ key ^ key，因为key ^ key为0, src ^ 0为src,从未解密
 */
#include <stdio.h>
#include <stdlib.h>

#define filename "109-plain.txt"
#define filename_encrypted "109-plain_encrypted.txt"
#define filename_decrypted "109-plain_decrypted.txt"
#define pwd "abcdefg"

void encrypt(char *srcfile, char *key, char *encrypted) {
    FILE *in, *out;
    if ((in = fopen(srcfile, "r")) == NULL) {
        perror("srcfile open error");
        exit(-1);
    }
    if ((out = fopen(encrypted, "w")) == NULL) {
        perror("encrypted file open error");
        exit(-1);
    }
    
    char ch;
    int i = 0;  //key是个字符串，每次只与一个字符异或
    ch = fgetc(in);
    while (!feof(in)) {
        ch = ch ^ *(key+i);
        fputc(ch, out);
        ch = fgetc(in); //注意feof是判断文件指针位置的，而不是判断字符内容，它是ch读取到EOF后，才能判断为空，所以最后会有个EOF不能要
            i++;
        if (*(key+i) == '\0')
            i = 0;
    }

    fclose(in);
    fclose(out);
}

void decrypt(char *encrypted, char *key, char *decrypted)
{
    FILE *in, *out;
    if ((in = fopen(encrypted, "r")) == NULL) {
        perror("encrypted file open error");
        exit(-1);
    }
    if ((out = fopen(decrypted, "w")) == NULL) {
        perror("decrypted file open error");
        exit(-1);
    }
    char ch;
    int i = 0;  //key是个字符串，每次只与一个字符异或
    ch = fgetc(in);
    while (!feof(in)) {
        ch = ch ^ *(key+i);
        fputc(ch, out);
        ch = fgetc(in);
        i++;
        if (*(key+i) == '\0')
            i = 0;
    }

    fclose(in);
    fclose(out);
}

int main(void) {
    encrypt(filename, pwd, filename_encrypted);

    decrypt(filename_encrypted, pwd, filename_decrypted);
}