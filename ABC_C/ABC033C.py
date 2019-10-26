# -*- coding: utf-8 -*-
# C - 数式の書き換え
# https://atcoder.jp/contests/abc033/tasks/abc033_c

S = input()
ans = 0

check = S.split('+')

for i in check:
    if i != '0':
        ans += 1
        j = list(i.split('*'))
        if '0' in j:
            ans -= 1

print(ans)

# 18:57 - 19:09（AC）
