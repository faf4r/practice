import random

def guess_number():
    level = input('请输入困难程度\n（0：退出、1：简单、2：中等、3：困难）：')
    r = 1

    try:
        lev = int(level)
    except:
        print('您的输入有误，请再次输入')
        guess_number()
    else:

        if lev==0:
            return
        elif lev==1:
            x = 5
        elif lev==2:
            x = 10
        elif lev==3:
            x = 20
        else:
            print('您的输入有误，请再次输入')
            guess_number()

    answer = random.randint(1,x)

    def number_input():

        n = input('这是一个1到{}之间的整数(包括)，你猜它是几（输入0可退出）：'.format(x))
        try:
            number = int(n)
        except:
            print('您的输入有误，请再次输入')
            number_input()
        else:
            if number==answer:
                print('你猜对了！！！')
            else:
                print('你猜错了')
    number_input()
    print(answer)

if __name__=='__main__':
    guess_number()
