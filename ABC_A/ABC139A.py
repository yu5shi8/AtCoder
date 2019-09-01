# -*- coding: utf-8 -*-
# A - Tenki
# https://atcoder.jp/contests/abc139/tasks/abc139_a

s = input()
t = input()
ans = 0

for i in range(3):
    if s[i] == t[i]:
        ans += 1

print(ans)

# 21:00 - 21:02（AC）
