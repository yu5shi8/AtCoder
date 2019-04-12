# -*- coding: utf-8 -*-
# B - 754
# https://atcoder.jp/contests/abc114/tasks/abc114_b

s = input()
master = 753
ans = []

for i in range(len(s)):
    x = int(s[i:i+3])
    calc = abs(master - x)
    ans.append(calc)

print(min(ans))
