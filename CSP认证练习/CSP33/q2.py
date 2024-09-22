n, m = map(int, input().split())

a = set(s.lower() for s in input().split())
b = set(s.lower() for s in input().split())

aub = len(a.union(b))
aib = len(a.intersection(b))

print(aib)
print(aub)
