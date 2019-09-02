# -*- coding: utf-8 -*-
# C - pushpush
# https://atcoder.jp/contests/abc066/tasks/arc077_a

n = int(input())
a = list(map(int, input().split()))
even = []
odd = []
b = []

for i in range(n):
    if i % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

if n % 2 != 0:
    even.reverse()
    b = even + odd
else:
    odd.reverse()
    b = odd + even

print(*b, sep=' ')

# 9:47 - 9:50（TLE）- 9:59（TLE）- 10:07（AC）
