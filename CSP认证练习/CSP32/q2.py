#! 被骗了，没必要判断素数，直接分解因子，每个因子全部个数记录下来取完，必然每个因子都被分解彻底，就不含非素数的了

from collections import defaultdict
from math import sqrt

def get_factors(n):
    ret = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            ret.append(i)
    return ret

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def f(n, k):
    factors = filter(is_prime, get_factors(n))
    dic = defaultdict(int)
    for i in factors:
        while n % i == 0:
            dic[i] += 1
            n /= i
        if dic[i] < k:
            del dic[i]
    ret = 1
    for i in dic:
        ret *= i ** dic[i]
    return ret

q = int(input())

for _ in range(q):
    n, k = map(int, input().split())
    print(f(n, k))
