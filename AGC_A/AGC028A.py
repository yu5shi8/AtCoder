# -*- coding: utf-8 -*-
# A - Two Abbreviations
# https://atcoder.jp/contests/agc028/tasks/agc028_a

from fractions import gcd

def lcm(a, b):
    return (a*b) // gcd(a, b)

N, M = map(int, input().split())
S = input()
T = input()

n = N // gcd(N, M)
m = M // gcd(N, M)
k = gcd(N, M)

for i in range(k):
    if S[i * n] != T[i * m]:
        print(-1)
        exit()

print(lcm(N, M))

# 10:47 - 11:41（RE / 解説を閲覧）- 12:19（AC）
