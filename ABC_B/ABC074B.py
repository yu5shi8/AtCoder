# -*- coding: utf-8 -*-
# B - Collecting Balls (Easy Version)
# https://atcoder.jp/contests/abc074/tasks/abc074_b

n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0

for i in range(n):
    type_a = abs(x[i]-0) * 2
    type_b = abs(x[i]-k) * 2
    ans += min(type_a, type_b)
print(ans)

# 22:59 - 23:16
