# -*- coding: utf-8 -*-
# B - Algae
# https://atcoder.jp/contests/abc127/tasks/abc127_b

r, d, x = map(int, input().split())
ans = [0] * 10

for i in range(10):
    if i == 0:
        calc = r * x - d
        ans[i] = calc
    else:
        calc = r * ans[i-1] - d
        ans[i] = calc

print(*ans, sep='\n')


# 21:03 - 21:22
