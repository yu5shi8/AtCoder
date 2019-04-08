# -*- coding: utf-8 -*-
# A - Maximize the Formula
# https://atcoder.jp/contests/abc110/tasks/abc110_a

# この回答はWAです
# a, b, c = reversed(input().split())
# ans = eval(a + b) + int(c)
# print(ans)

# 解説を見ました
a, b, c = map(int, input().split())
ans = max(a*10+b+c, a+b*10+c, a+b+c*10)
print(ans)