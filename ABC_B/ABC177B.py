# -*- coding: utf-8 -*-
# B - Substring
# https://atcoder.jp/contests/abc177/tasks/abc177_b

S = input()
T = input()

N = len(S)
M = len(T)
cnt = len(T)

for i in range(N-M+1):
    check = S[i:i+M]
    ck = 0
    for j in range(M):
        if check[j] != T[j]:
            ck += 1
    if ck < cnt:
        cnt = ck

print(cnt)

# 21:03 - 21:16（AC）
