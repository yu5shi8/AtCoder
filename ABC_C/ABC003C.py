# -*- coding: utf-8 -*-
# C - AtCoderプログラミング講座
# https://atcoder.jp/contests/abc003/tasks/abc003_3

N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
C = 0

for i in range(N-K, N):
    C = (C + R[i]) / 2

print('{:.10f}'.format(C))

# 10:03 - 10:19（WA）- 10:37（AC）
