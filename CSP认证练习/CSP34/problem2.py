class Matrix:
    def __init__(self, M: list[list[int]]):
        self.M = M
        self.n = len(M)
        self.m = len(M[0])
        self.__flatten = None
        self.__T = None

    def flatten(self) -> list[int]:
        if self.__flatten is not None:
            return self.__flatten
        ret = []
        for row in self.M:
            ret.extend(row)
        self.__flatten = ret
        return ret

    def reshape(self, p: int, q: int) -> None:
        flatten = self.flatten()
        self.n = p
        self.m = q
        length = p * q  # len(flatten)
        self.M = [flatten[i : i + q] for i in range(0, length, q)]
        self.__T = None

    def print(self) -> None:
        for row in self.M:
            print(" ".join(map(str, row)))

    def T(self):
        if self.__T is None:
            self.__T = [[self.M[i][j] for i in range(self.n)] for j in range(self.m)]
        self.__T, self.M = self.M, self.__T
        self.m, self.n = self.n, self.m

    def __getitem__(self, key: tuple[int, int]) -> int:
        i, j = key
        return self.M[i][j]


if __name__ == "__main__":
    n, m, t = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append([int(i) for i in input().split()])
    M = Matrix(matrix)

    for _ in range(t):
        op, a, b = map(int, input().split())
        match op:
            case 1:
                M.reshape(a, b)
            case 2:
                M.T()
            case 3:
                print(M[a, b])
