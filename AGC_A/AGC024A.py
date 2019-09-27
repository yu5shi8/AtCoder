# -*- coding: utf-8 -*-
# A - Fairness
# https://atcoder.jp/contests/agc024/tasks/agc024_a

A, B, C, K = map(int, input().split())
num = 10**18

if K % 2 == 0:
    ans = A - B
else:
    ans = B - A

print(A, B, C)

if ans > num:
    print('Unfair')
else:
    print(ans)

# 15:35 - 15:46（TLE）- 16:43（解説を閲覧）- 16:47（AC）
