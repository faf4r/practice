# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在命令行中实现进度条功能

import time

count_down = 10  # 设置倒计时时间，单位：秒
interval = 1  # 设置屏幕刷新的间隔时间，单位：秒
for i in range(0, int(count_down/interval)+1):
    print("\r"+"▇"*i+" "+str(i*10)+"%", end="")
    time.sleep(interval)
print("\n加载完毕")