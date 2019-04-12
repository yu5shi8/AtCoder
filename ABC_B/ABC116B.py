# -*- coding: utf-8 -*-
# B - Collatz Problem
# https://atcoder.jp/contests/abc116/tasks/abc116_b

def calc(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int((n*3) + 1)

s = int(input())
a = [s]
m = 1

while True:
    num = calc(a[m-1])
    if num not in a:
        a.append(num)
        m += 1
    else:
        print(len(a) + 1)
        break
