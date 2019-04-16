# -*- coding: utf-8 -*-
# ABC083B - Some Sums
# https://atcoder.jp/contests/abs/tasks/abc083_b

n, a, b = map(int, input().split())
ans = []

for i in range(1, n+1):
    num = sum(list(map(int, str(i))))
    if num >= a and num <= b:
        ans.append(i)
print(sum(ans))
