# -*- coding: utf-8 -*-
# B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b

a = int(input()) + 1
b = int(input()) + 1
c = int(input()) + 1
x = int(input())
ans = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            if i*500 + j*100 + k*50 == x:
                ans += 1

print(ans)

# 9:23 - 9:52
