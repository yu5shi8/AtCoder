# -*- coding: utf-8 -*-
# C - Minimization
# https://atcoder.jp/contests/abc101/tasks/arc099_a

n, k = map(int, input().split())
a = list(map(int, input().split()))
min_num = 10**9 + 10
count = 0

for i in range(0, n, k-1):
    check = a[i:i+k]
    num = min(a[i:i+k])
    if len(check) > 1:
        count += 1
    if num < min_num:
        min_num = num

print(count)

# 17:07 - 17:25（AC）
