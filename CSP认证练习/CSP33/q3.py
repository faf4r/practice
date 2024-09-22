class Array:
    def __init__(self, array: list[int]):
        self.array = array

    def __mul__(self, other: int|float):
        return Array([i*other for i in self.array])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val * other
        return self

    def __truediv__(self, other):
        return Array([i/other for i in self.array])

    def __itruediv__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val / other
        return self

    def __sub__(self, other):
        # array - array
        return [self.array[i]-other.array[i] for i in range(len(self.array))]

    def __isub__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val - other.array[i]
        return self

    def __add__(self, other):
        # array - array
        return [self.array[i] + other.array[i] for i in range(len(self.array))]

    def __iadd__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val + other.array[i]
        return self

    def is_zero(self):
        return all(i==0 for i in self.array)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __repr__(self):
        return str(self.array)


class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = [[]]
            self.m = 0
            self.n = 0
        else:
            self.matrix = matrix
            self.m = len(matrix)
            self.n = len(matrix[0])

    def exchange(self, i, j):
        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]

    def normalize(self, i, j):
        self.matrix[i] /= self.matrix[i][j]

    def eliminate(self, i, j, col):
        if self.matrix[j][col] == 0:
            return
        k = self.matrix[j][col] / self.matrix[i][col]
        self.matrix[j] -= self.matrix[i] * k

    def nonzero_col(self, r, j):
        for i in range(r, self.m):
            if self.matrix[i][j]:
                return i
        return -1

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        return str(self.matrix)


def str_process(s: str) -> dict[str, int]:
    dic = {}

    li = []
    start = 0
    for i in range(1, len(s)):
        if s[i].isalpha() and s[i-1].isdigit() or s[i].isdigit() and s[i-1].isalpha():
            li.append(s[start:i])
            start = i
    li.append(s[start:])
    for i in range(0, len(li), 2):
        dic[li[i]] = int(li[i+1])
    return dic

def check(material: list[str]):
    li = [str_process(s) for s in material]
    dic = {}
    for d in li:
        for key in d.keys():
            dic[key] = []
    for d in li:
        for key in dic.keys():
            dic[key].append(d.get(key, 0))
    matrix = Matrix([Array(i) for i in dic.values()])

    if matrix.m < matrix.n:
        return True

    r = 0
    for j in range(matrix.n):
        row = matrix.nonzero_col(r, j)
        if row == -1:
            continue
        if row != r:
            matrix.exchange(r, row)
        matrix.normalize(r, j)
        for i in range(r+1, matrix.m):
            matrix.eliminate(r, i, j)
        r += 1
    if r < matrix.n:
        return True
    else:
        return False


n = int(input())

for _ in range(n):
    m, *mat = input().split()
    print("Y" if check(mat) else "N")

'''
1
4 al2s3o12 n1h5o1 al1o3h3 n2h8s1o4

'''