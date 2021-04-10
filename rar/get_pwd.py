import itertools as its
import time


def get_password(min_digits, max_digits, words):
    """
    密码生成器
    :param min_digits: 密码最小长度
    :param max_digits: 密码最大长度
    :param words: 密码可能涉及的字符
    :return: 密码生成器
    """
    while min_digits <= max_digits:
        pwds = its.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
        min_digits += 1

# 密码范围
# words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 涉及到生成密码的参数
words = '0123456789'
start = time.time()
pwds = get_password(4, 4, words)
# 开始查找密码

t = 0
while t <= 9999:
    pwd = next(pwds)
    print(pwd)
    t += 1
end = time.time()
print('程序耗时{}'.format(end - start))
