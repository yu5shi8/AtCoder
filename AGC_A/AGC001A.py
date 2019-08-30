# -*- coding: utf-8 -*-
# A - BBQ Easy
# https://atcoder.jp/contests/agc001/tasks/agc001_a

n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
ans = 0

for i in range(0, n*2, 2):
    ans += min(l[i:i+2])

print(ans)

# 15:33 - 15:38（AC）
