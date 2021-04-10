'''
# first demo
s = 0
e = 9999


for i in range(s, e):
    print('\r已尝试{:.0%}'.format((i-s)/(e-s)), end='')


for u in range(0,9999):
    print('\ru', end='')
'''

''' # second demo
x = 0
def pwd_length():
    global x
    x = int(input('请输入密码位数：'))
    try:
        length = 10**int(x)
        return length
    except Exception as e:
        print('输入的位数必须是正整数！！')
        pwd_length()

start = 0
stop = pwd_length()
for i in range(start, stop):
    pwd = str(i).zfill(x)
    print(i)
'''
