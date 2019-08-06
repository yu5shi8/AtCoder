# -*- coding: utf-8 -*-
# A - Transfer
# https://atcoder.jp/contests/abc136/tasks/abc136_a

a, b, c = map(int, input().split())
ans = c - (a - b)
print(max(ans, 0))

# 14:42 - 14:49（AC）
