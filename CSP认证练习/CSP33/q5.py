from collections import defaultdict

n, m = map(int, input().split())

tree = [0] * (n+1)
dic = defaultdict(set)
dic[0].add(1)
for i, father in enumerate(input().split()):
    i = i + 2
    father = int(father)
    tree[i] = father
    dic[father].add(i)

storage = [0]
storage.extend([int(i) for i in input().split()])


def merge(x):
    sub_dir_num = 0
    new_sub_dir = set()
    for sub_dir in dic[x]:
        storage[x] += storage[sub_dir]
        for i in dic[sub_dir]:
            tree[i] = x
            new_sub_dir.add(i)
            sub_dir_num += 1
        tree[sub_dir] = 0
        # dic[sub_dir].clear()
    dic[x] = new_sub_dir
    return sub_dir_num, storage[x]

# def merge(x):
#     sub_dir_num = 0
#     sub_dir_set = set()
#     for i in range(1, n+1):
#         if tree[i] == x:
#             sub_dir_set.add(i)
#             storage[x] += storage[i]
#             tree[i] = 0
#     for i in range(1, n+1):
#         if tree[i] in sub_dir_set:
#             tree[i] = x
#             sub_dir_num += 1
#     return sub_dir_num, storage[x]


def visit(x):
    ans = 1
    while tree[x] != 0:
        x = tree[x]
        ans += 1
    return ans


for _ in range(m):
    op, x = map(int, input().split())
    if op == 1:  # merge directory
        print(*merge(x))
    else:  # op == 2: visit file
        print(visit(x))
