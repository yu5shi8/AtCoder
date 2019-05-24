# -*- coding: utf-8 -*-
# B - 754
# https://atcoder.jp/contests/abc114/tasks/abc114_b

s = input()
temp = 753
ans = []

for i in range(3, len(s)+1):
    ans.append(abs(int(s[i-3:i]) - temp))

print(min(ans))


# 16:08 - 16:20
