# -*- coding: utf-8 -*-
# B - Christmas Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_b

n = int(input())
l = [0] * n

for i in range(n):
    p = int(input())
    l[i] = p
max_p = max(l) // 2
ans = sum(l) - max_p
print(ans)
