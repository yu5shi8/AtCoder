# -*- coding: utf-8 -*-
# A - Ice Tea Store
# https://atcoder.jp/contests/agc019/tasks/agc019_a

Q, H, S, D = map(int, input().split())
N = int(input())
Q *= 4
H *= 2
l = min(Q, H, S)

if N >= 2:
    n = N // 2
    price = min(2*l*n, D*n) + l*(N%2)
else:
    price = N * l

print(price)

# 9:31 - 10:02 / 10:32 - 10:39（AC）
