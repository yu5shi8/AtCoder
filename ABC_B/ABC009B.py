# -*- coding: utf-8 -*-
# B - 心配性な富豪、ファミリーレストランに行く。
# https://atcoder.jp/contests/abc009/tasks/abc009_2

n = int(input())
a = [int(input()) for _ in range(n)]

ans = sorted(set(a))
print(ans[-2])

# 22:09 - 22:13（AC）
