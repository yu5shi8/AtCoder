# -*- coding: utf-8 -*-
# C - GeT AC
# https://atcoder.jp/contests/abc122/tasks/abc122_c

n, q = map(int, input().split())
s = input()
t = [0] * (n+1)

for i in range(n):
    t[i+1] = t[i] + (1 if s[i:i+2] == 'AC' else 0)

for i in range(q):
    l, r = map(int, input().split())
    print(t[r-1] - t[l-1])

# 19:44 - 20:07
