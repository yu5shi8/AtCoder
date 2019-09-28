# -*- coding: utf-8 -*-
# C - Go to School
# https://atcoder.jp/contests/abc142/tasks/abc142_c

N = int(input())
A = list(map(int, input().split()))
ans = [0] * N

for i in range(len(A)):
    ans[A[i] - 1] += (i + 1)

print(*ans, sep=' ')

# 21:08 - 21:14（AC）
