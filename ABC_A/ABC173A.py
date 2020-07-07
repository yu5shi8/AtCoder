# -*- coding: utf-8 -*-
# A - Payment
# https://atcoder.jp/contests/abc173/tasks/abc173_a

N = int(input())
i = 0

while N > i * 1000:
    i += 1

ans = i * 1000 - N
print(ans)

# 16:32 - 16:34（AC）
