# -*- coding: utf-8 -*-
# A - Fourtune Cookies
# https://atcoder.jp/contests/arc105/tasks/arc105_a

A = list(map(int, input().split()))

total = sum(A)

for i in range(2**4):
    check = []
    for j in range(4):
        if ((i >> j) & 1):
            check.append(A[j])
    c_total = sum(check)
    num = total - c_total
    if c_total == num:
        print('Yes')
        exit()

print('No')

# 22:30 - 22:40（AC）
