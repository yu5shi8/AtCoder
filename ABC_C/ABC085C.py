# -*- coding: utf-8 -*-
# C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c

n, y = map(int, input().split())

for a in range(n+1):
    for b in range(n-a+1):
        c = n - (a+b)
        if y == 10000*a + 5000*b + 1000*c:
            print(a, b, c)
            exit()

print(-1, -1, -1)

# 18:04 - 18:28
