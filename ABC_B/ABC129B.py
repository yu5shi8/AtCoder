# -*- coding: utf-8 -*-
# B - Balance
# https://atcoder.jp/contests/abc129/tasks/abc129_b

n = int(input())
w = list(map(int, input().split()))
ans = 1000

for t in range(1, n):
    left = w[:t]
    right = w[t:]
    calc = abs(sum(left) - sum(right))
    if calc < ans:
        ans = calc

print(ans)

# 21:03 - 21:16
