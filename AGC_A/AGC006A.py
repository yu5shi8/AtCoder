# -*- coding: utf-8 -*-
# A - Prefix and Suffix
# https://atcoder.jp/contests/agc006/tasks/agc006_a

N = int(input())
s = input()
t = input()
num = 0

if s == t:
    print(N)
    exit()

for i in range(1, N):
    if s[-i:] == t[:i]:
        num += 1 * i

print(N * 2 - num)

# 8:24 - 9:40（AC）
