# -*- coding: utf-8 -*-
# B - K-th Common Divisor
# https://atcoder.jp/contests/abc120/tasks/abc120_b
# 15:02 - 15:46

a, b, k = map(int, input().split())
ab = []

if a >= b:
    i = b
else:
    i = a

while i > 0:
    if a % i == 0 and b % i == 0:
        ab.append(i)
    i -= 1

print(ab[k - 1])

# 解説を見ての別解
# a, b, k = map(int, input().split())
# 
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         k -= 1
#         if k == 0:
#             print(i)
#             break
