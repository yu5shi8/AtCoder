# -*- coding: utf-8 -*-
# A - 名刺交換
# https://atcoder.jp/contests/arc010/tasks/arc010_1

N, M, A, B = map(int, input().split())

for m in range(M):
    if N <= A:
        N += B
    c = int(input())
    N -= c
    if N < 0:
        print(m+1)
        exit()

print('complete')

# 20:17 - 20:21（AC）
