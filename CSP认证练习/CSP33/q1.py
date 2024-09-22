n, m = map(int, input().split())

word_freq = [0] * (m+1)
word_appear = [0] * (m+1)

for _ in range(n):
    _, *line = map(int, input().split())
    current_appear_flag = [0] * (m+1)
    for i in line:
        word_freq[i] += 1
        if not current_appear_flag[i]:
            word_appear[i] += 1
            current_appear_flag[i] = 1

for i in range(1, m+1):
    print(word_appear[i], word_freq[i])
