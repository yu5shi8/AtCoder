# -*- coding: utf-8 -*-
# B - Resale
# https://atcoder.jp/contests/abc125/tasks/abc125_b

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = []

for i in range(n):
    if v[i] > c[i]:
        ans.append(v[i] - c[i])

print(sum(ans))

# 18:26 - 18:35
