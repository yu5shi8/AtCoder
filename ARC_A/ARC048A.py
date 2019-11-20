# -*- coding: utf-8 -*-
# A - 階段の下
# https://atcoder.jp/contests/arc048/tasks/arc048_a

A, B = map(int, input().split())

if (0 < A and 0 < B) or (A < 0 and B < 0):
    ans = abs(A - B)
else:
    ans = abs(A - B) - 1

print(ans)

# 17:28 - 17:34（AC）
