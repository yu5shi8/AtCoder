# -*- coding: utf-8 -*-
# C - Takahashi's Information
# https://atcoder.jp/contests/abc088/tasks/abc088_c

C = [list(map(int, input().split())) for _ in range(3)]

a = [C[0][0] - C[0][0]]
b = [C[0][0] - a[0]]

for i in range(1, 3):
    a.append(C[i][0] - b[0])
    b.append(C[0][i] - a[0])

for i in range(3):
    for j in range(3):
        num = a[i] + b[j]
        if num != C[i][j]:
            print('No')
            exit()

print('Yes')

# 14:26 - 15:05（AC）
