# -*- coding: utf-8 -*-
# B - Buffet
# https://atcoder.jp/contests/abc140/tasks/abc140_b

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = 0
check = -1

for i in range(N):
    eat = A[i] - 1
    count += B[eat]
    if 1 <= i <= (N-1):
        if check == eat - 1:
            count += C[check]
    check = eat

print(count)

# 21:02 - 21:11（AC）
