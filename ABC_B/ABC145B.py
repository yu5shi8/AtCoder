# -*- coding: utf-8 -*-
# B - Echo
# https://atcoder.jp/contests/abc145/tasks/abc145_b

N = int(input())
S = input()

T1 = S[0:N//2]
T2 = S[N//2:]

if T1 == T2:
    print('Yes')
else:
    print('No')

# 21:01 - 21:05（AC）
