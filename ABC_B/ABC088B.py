# -*- coding: utf-8 -*-
# B - Card Game for Two
# https://atcoder.jp/contests/abc088/tasks/abc088_b

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += int(a[i])
    else:
        bob += int(a[i])

print(alice - bob)

# 17:40 - 18:01

