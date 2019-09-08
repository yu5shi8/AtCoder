# -*- coding: utf-8 -*-
# C - Lining Up
# https://atcoder.jp/contests/abc050/tasks/arc066_a

N = int(input())
A = list(map(int, input().split()))
A.sort()
B = []
mod = 10**9 + 7

if N % 2 == 0:
    for i in range(1, N, 2):
        B.append(i)
        B.append(i)
else:
    B.append(0)
    for i in range(2, N, 2):
        B.append(i)
        B.append(i)

if A != B:
    ans = 0
else:
    ans = 2 ** (N // 2) % mod

print(ans)

# 23:37 - 23:58（考え方をまとめた）
# （コードを書いていく）11:38 - 12:15（WA）-（解説を閲覧）12:25（AC）
