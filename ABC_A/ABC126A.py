# -*- coding: utf-8 -*-
# A - Changing a Character
# https://atcoder.jp/contests/abc126/tasks/abc126_a

n, k = map(int, input().split())
s = input()
s_k = s[k-1].lower()
print(s[:k-1]+s_k+s[k:])

# 21:00 - 21:07
