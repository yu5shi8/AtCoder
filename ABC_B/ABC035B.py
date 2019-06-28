# -*- coding: utf-8 -*-
# B - ドローン
# https://atcoder.jp/contests/abc035/tasks/abc035_b

s = input()
t = int(input())

x = s.count('R') - s.count('L')
y = s.count('U') - s.count('D')
num   = s.count('?')

if t == 1:
    ans = abs(x) + abs(y) + num
elif t == 2:
    ans = max(len(s) % 2, abs(x) + abs(y) - num)

print(ans)

# 14:36 - 15:07（WA）
#（解説を閲覧）- 15:25（WA）- 15:29（AC）
