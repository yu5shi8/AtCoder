# -*- coding: utf-8 -*-
# B - Bingo
# https://atcoder.jp/contests/abc157/tasks/abc157_b

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = A1 + A2 + A3

N = int(input())

for i in range(N):
    b = int(input())
    if b in A:
        n = A.index(b)
        A[n] = '*'

if A[0] == A[1] == A[2] or A[3] == A[4] == A[5] or A[6] == A[7] == A[8]:
    print('Yes')
elif A[0] == A[3] == A[6] or A[1] == A[4] == A[7] or A[2] == A[5] == A[8]:
    print('Yes')
elif A[0] == A[4] == A[8] or A[2] == A[4] == A[6]:
    print('Yes')
else:
    print('No')

# 20:52 - 24:28（AC）
