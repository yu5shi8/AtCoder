# -*- coding: utf-8 -*-
# C - 入れ替え
# https://atcoder.jp/contests/abc004/tasks/abc004_3

N = int(input())
num = N % 30
arr = [1, 2, 3, 4, 5, 6]

for i in range(num):
    L = (i % num) % 5
    R = (i % num + 1) % 5
    if (i+1) % 5 == 0:
        R = L + 1
    arr[L], arr[R] = arr[R], arr[L]

print(*arr, sep='')

# 21:59 - 22:13 / 11:44 - 12:10 / 13:25 - 14:12（AC）
