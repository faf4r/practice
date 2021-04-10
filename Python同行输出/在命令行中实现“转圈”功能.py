# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在一行中不断刷新转圈

import time

count_down = 10  # 设置倒计时时间，单位：秒
interval = 0.25  # 设置屏幕刷新的间隔时间，单位：秒
for i in range(0, int(count_down/interval)):
    ch_list = ["\\", "|", "/", "-"]
    index = i % 4
    msg = "\r程序运行中 " + ch_list[index]
    print(msg, end="")
    time.sleep(interval)
print(u"\r结束" + "  "*len(msg))