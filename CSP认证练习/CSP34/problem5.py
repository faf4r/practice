import sys
sys.stdin = open('52.in', 'r')
sys.stdout = open('52.out', 'w')


def relu(x):
    return x if x > 0 else 0

n, m = map(int, input().split())
V = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    x1, x2, y1, y2, v = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            V[i][j] = v + relu(V[i][j] - v)

for _ in range(m):
    x1, x2, y1, y2 = map(int, input().split())
    ans = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            ans = max(ans, V[i][j])
    print(ans)
