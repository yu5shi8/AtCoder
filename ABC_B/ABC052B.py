# -*- coding: utf-8 -*-
# B - Increment Decrement
# https://atcoder.jp/contests/abc052/tasks/abc052_b

n = int(input())
s = input()
x = 0
ans = 0

for i in range(n):
    if s[i] == 'I':
        x += 1
        if ans < x:
            ans = x
    else:
        x -= 1

print(ans)

# 22:41 - 22:51
