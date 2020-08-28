# -*- coding: utf-8 -*-
# C - Step
# https://atcoder.jp/contests/abc176/tasks/abc176_c

N = int(input())
A = list(map(int, input().split()))

check = A[0]
ans = 0

for i in range(N):
    if check < A[i]:
        check = A[i]
    elif check > A[i]:
        ans += check - A[i]

print(ans)

# 18:15 - 18:22（AC）
