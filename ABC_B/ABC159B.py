# -*- coding: utf-8 -*-
# B - String Palindrome
# https://atcoder.jp/contests/abc159/tasks/abc159_b

S = input()
N = len(S)
ans = 0

if S == S[::-1]:
    ans += 1

i = (N-1) // 2
if S[:i] == S[:i:-1]:
    ans += 1

j = (N+3) // 2 - 1
if S[j:] == S[N:j-1:-1]:
    ans += 1

if ans == 3:
    print('Yes')
else:
    print('No')

# 22:21 - 22:40（AC）
