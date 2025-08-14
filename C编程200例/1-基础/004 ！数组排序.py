ar = [3, 2, 1]

for j in range(len(ar)):
    for k in range(len(ar)-j-1):
        if ar[k]> ar[k+1]:
            ar[k], ar[k+1] = ar[k+1], ar[k]

print(ar)
# 这里有问题，k+1那里会超范围，我的笔记有错误
# 正确写法是range那里还要再-1
