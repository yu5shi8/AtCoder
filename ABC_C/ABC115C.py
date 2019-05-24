# -*- coding: utf-8 -*-
# C - Christmas Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_c

n, k = map(int, input().split())
h = sorted(list(int(input()) for _ in range(n)))
ans = []

for i in range(n-k+1):
    ans.append(h[i+k-1]-h[i])

print(min(ans))

# 15:50 - 15:59
