# -*- coding: utf-8 -*-
# B - ROT N
# https://atcoder.jp/contests/abc146/tasks/abc146_b

N = int(input())
S = input()
ans = ''

for i in range(len(S)):
    c = ord(S[i]) + N
    if c > 90:
        c -= 26
    ans += chr(c)

print(ans)

# 20:22 - 20:40（AC）
