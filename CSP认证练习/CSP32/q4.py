from collections import deque
left = 0
right = 1

class Deque(deque):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last = []

    def append(self, *args, **kwargs):
        super().append(*args, **kwargs)
        self.last.append(right)

    def appendleft(self, *args, **kwargs):
        super().appendleft(*args, **kwargs)
        self.last.append(left)

    def pop(self):
        super().pop()
        assert self.last[-1] == right
        self.last.pop()

    def popleft(self):
        super().popleft()
        assert self.last[-1] == left
        self.last.pop()


class Matrix:
    def __init__(self, li):
        self.matrix = [
            [li[0], li[1]],
            [li[2], li[3]],
        ]

    def __getitem__(self, item):
        i, j = item
        return self.matrix[i][j]

    def __imul__(self, other):
        ret = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ret[i][j] += self.matrix[i][k] * other.matrix[k][j]
        self.matrix = ret
        return self

    def __imod__(self, other):
        for i in range(2):
            for j in range(2):
                self.matrix[i][j] %= other
        return self

    def __str__(self):
        return ' '.join(str(val) for row in self.matrix for val in row)


class Command:
    def __init__(self, li):
        match li[0]:
            case 1:
                self.cmd = self.append_left(Matrix(li[1:]))
            case 2:
                self.cmd = self.append_right(Matrix(li[1:]))
            case 3:
                self.cmd = self.pop_last

    def exec(self, dq):
        self.cmd(dq)

    def append_left(self, mat):
        def func(dq):
            dq.appendleft(mat)
        return func

    def append_right(self, mat):
        def func(dq):
            dq.append(mat)
        return func

    def pop_last(self, dq):
        if not dq:
            return
        if dq.last[-1] == left:
            dq.popleft()
        else:
            dq.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    cmd_list = []
    # dq = Deque()
    for i in range(n):
        cmd_list.append(Command([int(s) for s in input().split()]))
        # cmd_list[i].exec(dq)
    for _ in range(m):
        v, *inp = map(int, input().split())
        if v == 1:
            i = inp[0] - 1
            cmd_list[i] = Command(inp[1:])
        else:
            l, r = inp
            dq = Deque()
            for i in range(l-1, r):
                cmd_list[i].exec(dq)
            ans = Matrix([1, 0, 0, 1])
            for mat in dq:
                ans *= mat
            ans %= 998244353
            print(ans)
