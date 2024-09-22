class Array:
    def __init__(self, array: list[int]):
        self.array = array

    def __mul__(self, other: int|float):
        return Array([i*other for i in self.array])

    def __rmul__(self, other):
        self.__mul__(other)

    def __imul__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val * other

    def __truediv__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val / other

    def __itruediv__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val / other

    def __sub__(self, other):
        # array - array
        return [self.array[i]-other.array[i] for i in range(len(self.array))]

    def __isub__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val - other.array[i]

    def __add__(self, other):
        # array - array
        return [self.array[i] + other.array[i] for i in range(len(self.array))]

    def __iadd__(self, other):
        for i, val in enumerate(self.array):
            self.array[i] = val + other.array[i]

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
        k = self.matrix[j][col] / self.matrix[i][col]
        self.matrix[j] *= k
        self.matrix[j] -= self.matrix[i]

    def nonzero_col(self, j):
        for i in range(self.m):
            if self.matrix[i][j]:
                return i
        return -1


a = Array([1, 2, 3, 4])
a /= 1
print(a)