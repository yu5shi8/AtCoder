# -*- coding: utf-8 -*-
# B - ... (Triple Dots)
# https://atcoder.jp/contests/abc168/tasks/abc168_b

K = int(input())
S = input()
cnt = '...'

if len(S) <= K:
    print(S)
else:
    print(S[:K] + str(cnt))

# 17:33 - 17:37（AC）
