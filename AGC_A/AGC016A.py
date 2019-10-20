# -*- coding: utf-8 -*-
# A - Shrinking
# https://atcoder.jp/contests/agc016/tasks/agc016_a

s = list(input())
t = []
ans = 10**9 + 10

if s.count(s[0]) == len(s):
    print(0)
    exit()

for i in set(s):
    c = i
    j = 0
    n = s
    t = []
    while j >= 0:
        for k in range(1, len(n)):
            if c == n[k-1] and c != n[k]:
                t.append(c)
            elif c != n[k-1] and c == n[k]:
                t.append(c)
            elif c != n[k-1] != n[k]:
                t.append(n[k-1])
            else:
                t.append(n[k])
        if t.count(c) == len(t):
            cnt = j + 1
            if cnt < ans:
                ans = cnt
            break
        else:
            n = t
            t = []
        j += 1

print(ans)

# 13:03 - 14:16（解説を閲覧）- 15:37（AC）
