# -*- coding: utf-8 -*-
# B - Golden Apple
# https://atcoder.jp/contests/abc134/tasks/abc134_b

n, d = map(int, input().split())

calc = (n + 1) // (d * 2 + 1)
mod = (n + 1) % (d * 2 + 1)

if mod <= 1:
    ans = calc
else:
    ans = calc + 1

print(ans)

# 22:47 -（解法を閲覧）- 22:56
# 14:17 - 14:45（AC）
