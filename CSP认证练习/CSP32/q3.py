from functools import lru_cache
from queue import Queue

class Node:
    def __init__(self, i, w):
        self.i = i
        self.w = w
        self.children = []
        self.parent = None

    def is_leaf(self):
        return not self.children

# @lru_cache
def w_of(node, exc):
    ret = node.w
    for child in node.children:
        if child.i in exc:
            continue
        ret += w_of(child, exc)
    return ret

def get_w_list(root, exc):
    ret = []
    q = Queue()
    q.put(root)
    last_one = True
    while not q.empty():
        node = q.get()
        ret.append((node.i, w_of(node, exc)))
        for child in node.children:
            if child.i not in exc:
                last_one = False
                q.put(child)

    ret.sort(key=lambda x: x[1])
    return ret, last_one


n, m = map(int, input().split())
node_list = []
for i, w in enumerate(map(int, input().split())):
    node_list.append(Node(i+1, w))
root = node_list[0]
for i, p in enumerate(map(int, input().split())):
    node_list[i+1].parent = node_list[p-1]
    node_list[p-1].children.append(node_list[i+1])

for _ in range(m):
    test_val = int(input())
    exc = set()
    node = root
    last_one = False
    result = []
    while True:
        ans, last_one = get_w_list(node, exc)
        ans = ans[0][0]
        if ans == test_val:
            node = node_list[ans-1]
        else:
            exc.add(ans)
        if last_one:
            break
        else:
            result.append(ans)
    print(' '.join(str(i) for i in result))
