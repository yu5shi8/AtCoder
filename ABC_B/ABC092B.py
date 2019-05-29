# -*- coding: utf-8 -*-
# B - Chocolate
# https://atcoder.jp/contests/abc092/tasks/abc092_b

n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
choco = [0] * n

for i in range(n):
    count = d
    while count > 0:
        count -= a[i]
        choco[i] += 1

ans = sum(choco) + x
print(ans)

# 20:05 - 20:24
