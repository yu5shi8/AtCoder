# -*- coding: utf-8 -*-
# B - Palindrome-philia
# https://atcoder.jp/contests/abc147/tasks/abc147_b

S = input()
cnt = 0

if len(S) % 2 == 0:
    n = len(S) // 2
    s1 = S[:n]
    s2 = S[:n-1:-1]
else:
    n = len(S) // 2 + 1
    s1 = S[:n-1]
    s2 = S[:n-1:-1]

for i in range(len(S)//2):
    if s1[i] != s2[i]:
        cnt += 1

print(cnt)

# 21:01 - 21:09（AC）
