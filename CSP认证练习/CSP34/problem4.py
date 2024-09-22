from collections import namedtuple

Repo = namedtuple("Repo", ["b", "c"])
Stuff = namedtuple("Stuff", ["a", "t"])

repo = []
stuff = []
repo_selected = []

n, m, v = map(int, input().split())

for j in range(n):
    b, c = map(int, input().split())
    repo.append(Repo(b, c))
    repo_selected.append(False)

for i in range(m):
    a, t = map(int, input().split())
    stuff.append(Stuff(a, t))

current_value = 0
current_cost = 0
min_cost = float("inf")

def dfs(i):
    global current_value
    global current_cost
    global min_cost
    if current_value >= v and current_cost < min_cost:
        min_cost = current_cost
        return
    if i >= m:
        return
    
    # select stuff[i]
    cost = repo[stuff[i].t].c
    select_flag = False
    if not repo_selected[stuff[i].t]:
        repo_selected[stuff[i].t] = True
        select_flag = True
        cost += repo[stuff[i].t].b
    current_value += stuff[i].a - cost
    current_cost += cost
    dfs(i+1)

    if select_flag:
        repo_selected[stuff[i].t] = False
    current_value -= stuff[i].a - cost
    current_cost -= cost
    dfs(i+1)

dfs(0)

print(min_cost)
