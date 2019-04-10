# -*- coding: utf-8 -*-
# B - Digital Gifts
# https://atcoder.jp/contests/abc119/tasks/abc119_b

#19:53 - 20:02
N = int(input())
rate = 380000.0
ans = 0.0

for i in range(N):
    x, u = input().split()
    x = float(x)
    ans += x * rate if u =='BTC' else x

print('{:.7f}'.format(ans))


# 16:14 - 16:59
'''
# WA
N = int(input())
n = {}
ans = 0

while N > 0:
    key_and_value = input()
    key, value = key_and_value.split()
    n[key] = value
    N -= 1

for i in n:
    if n[i] == 'JPY':
        ans += int(i)
    else:
        ans += 380000 * float(i)

print(ans)
'''
