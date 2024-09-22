class Matrix:
    def __init__(self, M: list[list[int]]):
        self.M = M
        self.n = len(M)
        self.m = len(M[0])
    
    def flatten(self) -> list[int]:
        ret = []
        for row in self.M:
            ret.extend(row)
        return ret
    
    def reshape(self, p: int, q: int) -> None:
        flatten = self.flatten()
        self.n = p
        self.m = q
        length = p * q # len(flatten)
        self.M = [flatten[i:i+q] for i in range(0, length, q)]
    
    def print(self) -> None:
        for row in self.M:
            print(' '.join(map(str, row)))


if __name__ == '__main__':
    n, m, p, q = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append([int(i) for i in input().split()])
    M = Matrix(matrix)
    M.reshape(p, q)
    M.print()
