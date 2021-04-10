# __description__ = '先解压再检测密码，文件越大，耗时越久'

from unrar import rarfile
import time

x = 0
def pwd_length():
    global x
    try:
        x = int(input('请输入密码位数：'))
        length = 10**x
        return length
    except Exception as e:
        print('输入的位数必须是正整数！！')
        pwd_length()


def rar_pass(path):
    bfound = False
    fp = rarfile.RarFile(path)

    start = 0
    stop = pwd_length()

    for i in range(start, stop):
        pwd = str(i).zfill(x)
        starttime = time.time()
        try:
            fp.extractall(pwd=pwd)
            print('\n爆破成功，密码：'+pwd)
            bfound = True
        except Exception as e:
            print('\r已尝试{:.0%}'.format((i-start)/(stop-start)), end='')
        if bfound:
            endtime = time.time()
            print(u'共用时:', endtime - starttime, '秒')
            break

if __name__ == '__main__':
    print('注意：只适用于数字密码')
    path = input('rarpath')
    try:
        fp_try = rarfile.RarFile(path)
        fp_try.extractall()
        print('该文件无密码')
    except RuntimeError as e:
        rar_pass(path=path)
