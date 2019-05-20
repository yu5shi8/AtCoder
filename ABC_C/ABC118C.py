# -*- coding: utf-8 -*-
# C - Monsters Battle Royale
# https://atcoder.jp/contests/abc118/tasks/abc118_c

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

n = int(input())
a = list(map(int, input().split()))
num = 0

for i in range(n):
    num = gcd(num, a[i])

print(num)

# 21:11 - 21:15
