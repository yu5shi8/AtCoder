# -*- coding: utf-8 -*-
# ABC087B - Coins
# https://atcoder.jp/contests/abs/tasks/abc087_b

a = int(input()) + 1
b = int(input()) + 1
c = int(input()) + 1
x = int(input())
ans = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            if 500*i + 100*j + 50*k == x:
                ans += 1
print(ans)

# わからなかったので他の人の解答を見ました
