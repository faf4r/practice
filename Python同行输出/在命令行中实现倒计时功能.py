# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在一行中不断刷新倒计时

import time

count_down = 10  # 设置倒计时时间，单位：秒
for i in range(count_down, 0, -1):
    msg = u"\r系统将在 " + str(i) + "秒 内自动退出"
    print(msg, end="")
    time.sleep(1)
end_msg = "结束" + "  "*(len(msg)-len("结束"))  # 如果单纯只用“结束”二字，无法完全覆盖之前的内容
print(u"\r"+end_msg)