# -*- coding: utf-8 -*-
# B - Cut and Count
# https://atcoder.jp/contests/abc098/tasks/abc098_b

n = int(input())
s = input()
ans = 0

for i in range(1, n):
    count = 0
    left = list(set(s[:i]))
    right = list(set(s[i:]))
    for i in left:
        if right.count(i) == 1:
            count += 1
    if count > ans:
        ans = count

print(ans)

# 19:42 - 20:03
