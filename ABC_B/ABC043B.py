# -*- coding: utf-8 -*-
# B - バイナリハックイージー / Unhappy Hacking (ABC Edit)
# https://atcoder.jp/contests/abc043

s = input()
ans = ''

for i in s:
    if i != 'B':
        ans += i
    elif i == 'B':
        ans = ans[:-1]

print(ans)

# 16:51 - 18:07
