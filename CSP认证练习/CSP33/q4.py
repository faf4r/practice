# c, m, n = map(int, input().split())
#
# cup = [0] * c
# for _ in range(m):
#     x, w = map(int, input().split())
#     cup[x-1] = w
#
#
# def explode_once(index):
#     if cup[index] == 0:  # 防重复
#         return []
#
#     ret = []
#     cup[index] = 0
#
#     left = index - 1
#     while left >= 0:
#         if not cup[left]:
#             left -= 1
#             continue
#         cup[left] += 1
#         if cup[left] >= 5:
#             ret.append(left)
#         break
#
#     right = index + 1
#     while right < c:
#         if not cup[right]:
#             right += 1
#             continue
#         cup[right] += 1
#         if cup[right] >= 5:
#             ret.append(right)
#         break
#     return ret
#
# for _ in range(n):
#     p = int(input()) - 1
#     cup[p] += 1
#     if cup[p] < 5:
#         print(m)
#         continue
#
#     # 第p格要爆开
#     explode_index_list = [p]
#     while explode_index_list:
#         ret = explode_once(explode_index_list.pop(0))
#         m -= 1
#         explode_index_list.extend(ret)
#         explode_index_list.sort()
#
#     print(m)

c, m, n = map(int, input().split())

# 只记录有水的格子
cup = []
cup_index = []

li = []
for _ in range(m):
    x, w = map(int, input().split())
    li.append((x, w))
li.sort(key=lambda item: item[0])  # 初始未被排序

for x, w in li:
    cup_index.append(x)
    cup.append(w)


def explode_once(i):
    ret = []
    cup.pop(i)
    cup_index.pop(i)
    # 此时i即为爆开格子右边有水的格子
    left = i-1
    right = i
    if left >= 0:
        cup[left] += 1
        if cup[left] >= 5:
            ret.append(left)
    if right < len(cup):
        cup[right] += 1
        if cup[right] >= 5:
            ret.append(right)
    return ret

for _ in range(n):
    p = int(input())
    i = cup_index.index(p)
    cup[i] += 1
    if cup[i] < 5:
        print(m)
        continue

    # 第p格要爆开
    explode_index_list = [i]
    while explode_index_list:
        # 每次从左边开始爆，每次只有相邻两个可能加入列表
        # 但删除左边位置后，右边位置会替代被删除位置
        explode_index_list = explode_once(explode_index_list[0])
        m -= 1

    print(m)

