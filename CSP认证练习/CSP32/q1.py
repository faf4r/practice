class Repo(list):
    def __init__(self, i, li):
        self.i = i
        super().__init__(li)

    def __lt__(self, other):
        for j, val in enumerate(self):
            if val >= other[j]:
                return False
        return True
        # return all(self[j] < other[j] for j in range(len(self)))

    def __eq__(self, other):
        return self.i == other.i

    def __gt__(self, other):
        return all(self[j] > other[j] for j in range(len(self)))

n, m = map(int, input().split())

repo_list = []
for i in range(n):
    repo_list.append(Repo(i+1, [int(j) for j in input().split()]))

def upper(repo):
    for i in range(n):
        if repo < repo_list[i]:
            return repo_list[i].i
    return 0

for repo in repo_list:
    print(upper(repo))
