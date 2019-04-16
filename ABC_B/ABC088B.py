# -*- coding: utf-8 -*-
# ABC088B - Card Game for Two
# https://atcoder.jp/contests/abs/tasks/abc088_b

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

ans = alice - bob
print(ans)
