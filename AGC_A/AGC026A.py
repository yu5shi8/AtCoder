# -*- coding: utf-8 -*-
# A - Colorful Slimes 2
# https://atcoder.jp/contests/agc026/tasks/agc026_a

n = int(input())
a = list(map(int, input().split()))

l = a[0]
cnt = 1
ans = 0

for i in range(1, n):
    if l == a[i]:
        cnt += 1
    else:
        ans += cnt // 2
        l = a[i]
        cnt = 1

ans += cnt // 2

print(ans)

# 17:45 - 17:59（AC）
