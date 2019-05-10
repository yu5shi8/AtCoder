# -*- coding: utf-8 -*-
# B - 文字列大好きいろはちゃんイージー / Iroha Loves Strings (ABC Edition)
# https://atcoder.jp/contests/abc042/tasks/abc042_b

n, l = map(int, input().split())
s = [input() for _ in range(n)]
ans = sorted(s)
print(*ans, sep='')

# 18:09 - 18:16
