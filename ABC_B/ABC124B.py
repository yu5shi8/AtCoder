# -*- coding: utf-8 -*-
# B - Great Ocean View
# https://atcoder.jp/contests/abc124/tasks/abc124_b

n = int(input())
h = list(map(int, input().split()))
ans = 1

for i in range(1, n):
    if h[0] <= h[i] and max(h[:i]) <= h[i]:
        ans += 1

print(ans)

# 10:13 - 10:36
