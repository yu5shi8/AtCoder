# -*- coding: utf-8 -*-
# B - Two Colors Card Game
# https://atcoder.jp/contests/abc091/tasks/abc091_b

n = int(input())
s = sorted([input() for i in range(n)])

m = int(input())
t = sorted([input() for j in range(m)])

ans = 0

for i in range(n):
    name = s[i]
    count = s.count(name) - t.count(name)
    if count > ans:
        ans = count

print(ans)

# 17:24 - 17:38（WA）- 17:40（AC）
