# -*- coding: utf-8 -*-
# C - 座圧
# https://atcoder.jp/contests/abc036/tasks/abc036_c

N = int(input())
A = []
for i in range(N):
    a = int(input())
    b = i
    A.append([a, b])

A.sort()

ans = [[0, A[0][1]]]
num = 0
for i in range(1, N):
    if A[i-1][0] == A[i][0]:
        num += 0
    elif A[i-1][0] < A[i][0]:
        num += 1
    ans.append([num, A[i][1]])

ans = sorted(ans, key=lambda x: x[1])

for i in range(N):
    print(ans[i][0], sep='\n')

# 14:02 - 14:33（WA）- 14:36（AC）
